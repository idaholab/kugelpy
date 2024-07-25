'''
@authors: balep, stewryan, ethan-fowler

Copyright 2024, Battelle Energy Alliance, LLC, ALL RIGHTS RESERVED
'''

import copy
import os
import random 
import shutil
import csv
import time
import numpy as np
from scipy.interpolate import interp1d
import _pickle as pickle
import json

from kugelpy.kugelpy.kugelpy.maelstream import GenPBDist
import kugelpy.kugelpy.kugelpy.pebble_bed_reactor as pbr
from kugelpy.kugelpy.sea_serpent.reactor import SerpentReactor
import kugelpy.kugelpy.kugelpy.pebble as pbl
from kugelpy.kugelpy.mutineer import serpentutils as su
from kugelpy.kugelpy.mutineer import logutils
import subprocess

main_dir = os.path.dirname(os.path.realpath(__file__))
data_path = os.path.join(main_dir, 'data')

class PebbleSorter(SerpentReactor):
    """
    Pebble shuffeling class which wraps around Serpent to perfom fuel shuffeling in the core
    
    Parameters
    ----------
    
    Attributes
    ----------
    mesh_dict: dict
        ...
    kernel_data: dict
        Dictionary which holds geometry information for the fuel kernels (in cm):
        {'fuel': fuel_radius, 'buffer': buffer_radius, 'inner_pyc': inner_pyc_radius, 'sic': sic_radius, 'outer_pyc':  outer_pyc_radius, 'kernels_per_pebble': kernels_per_pebble}
    pebble_data: dict
        Dictionary which holds information for the pebble (in cm):
        {'inner': pebble_inner_radius, 'outer': pebble_pouter_radius}
    graphite_height: float
        Initial height for graphite pebbles, all pebbles with centroid below this height will be graphite
    burnstep: int
        Number of steps the burn up process has gone through
    graphite_fraction: float
        Fraction of pebbles ablve the grahpite_height which are graphite pebbles
    burnup_materials: dict
        Dictionary of burnup materaial for pebbles in their previous location
    burnup_limit: float
        Limit for burnup by which pebbles will not be passed through the core again (currently not implemented)
    """

       
    def __init__(self, **kwargs):
        super().__init__()
        self._pebble_array = []
        self._kernel_data = {}
        self._unloaded_pebbles = []
        self._unloaded_fuel_pebbles = []
        self.graphite_height = 0.0
        self.graphite_fraction = 0.0
        self._burnup_materials = {}
        self._efpd_tracker = 0.0 # days
        self.day_limit = 10000
        self._burnstep = 0
        self.critical_timestep = 1 # Should be selected automatically
        self.power_level = 1E+6 # Power level is in Watts 
        self.create_dimples = True
        self.simple_core = False
        self.serpent_version = '2.2'
        self._power_days = 0.
        self.random_seed = 2
        self.nbuf = 50

        # Variables required for Griffin/Pronghorn coupling
        self.multiphysics_run = False
        self.path_to_micro_xs = ''
        self.path_to_moose_mesh = ''
        self.minimum_temperature_difference = 50
        
        # Flags and variables associated with reactor temperatures
        self.create_temperature_profile_flag = False
        self.temperature_axial_zones = None
        self.axial_heights = None
        self.max_fuel_temperature = None # K
        self.min_fuel_temperature = None # K
        self.max_pebble_temperature = None # K
        self.min_pebble_temperature = None # K
        
        self.fixed_reactor_temperature = 900.0 # K
        self.fuel_temperature = self.fixed_reactor_temperature
        self.pebble_temperature = self.fixed_reactor_temperature
        self.core_inlet_temperature = self.fixed_reactor_temperature
        self.core_outlet_temperature = self.fixed_reactor_temperature
        self.cr_insertion_depth = 0.0
        self.sr_insertion_depth = -25.0
        

        # Automatically detect when the graphite pebbles are gone and transition to fuel to self.equilibrium_fuel_material
        self.automatic_fuel_transition = True
        self.transition_fuel_flag = False
        
        # Parameters assopciated with burning the core
        self.refine_burnstep = False        
        self.depletion_steps = [11]
        self.temp_depletion_steps = [1]        
        self.target_keff = 1.005 # k-eff we want to end up at after each burnstep, and for the critical height calculations
        self.allowable_keff = 1.0025
        self.burnup_limit = 160.0 # MWd/kg
        self.pass_limit = 6

        # Serpent run parameters.
        self.num_particles = 40000
        self.num_generations = 200
        self.skipped_generations = 40
        
        self.fuel_material = None
        self.equilibrium_fuel_material = None
        self.atom_density_limit = 1E-20
        self.pebble_distribution_file = 'pebble_distribution'
        self._step_pebble_distribution_file = ''
        self.pebble_surface_file = 'pebble_surfaces.inp'
        self.pebble_material_file = 'pebble_materials.inp'
        self.pebble_cell_file = 'pebble_cells.inp'
        self.reactor_file_name = 'serpent.inp'
        self.detector_file = 'material_detectors.inp'
        self.keep_files = True
        self.start_step = 1
        self.load_step = 1
        self.homogenize_passes = True
        
        self.core_materials = {'control_rod':    {'temperature': 300.0, 'moder': 'moder', 'moder_nuclide': 6000, 'nuclides':{ '6000': 2.74680E-2, '5010': 8.799626E-2, '5011': 2.18617E-2}},
                               'safety_rod':     {'temperature': 300.0, 'moder': 'moder', 'moder_nuclide': 6000, 'nuclides':{ '6000': 2.74680E-2, '5010': 8.799626E-2, '5011': 2.18617E-2}},
                               'reflector':      {'temperature': 300.0, 'moder': 'moder', 'moder_nuclide': 6000, 'nuclides':{ '6000': 8.82418E-2, '5010': 9.42800E-8,  '5011': 3.79489E-7}},
                               'outlet_channel': {'temperature': 300.0, 'moder': 'moder', 'moder_nuclide': 6000, 'nuclides':{ '6000': 6.61814E-2, '5010': 7.07100E-8,  '5011': 2.84617E-7}},
                               'outlet_plenum':  {'temperature': 300.0, 'moder': 'moder', 'moder_nuclide': 6000, 'nuclides':{ '6000': 5.82396E-2, '5010': 6.22248E-8,  '5011': 2.50463E-7}},
                               'pebble_shoot':   {'temperature': 300.0, 'moder': 'moder', 'moder_nuclide': 6000, 'nuclides':{ '6000': 8.82418E-2, '5010': 7.07100E-8,  '5011': 2.84617E-7}},
                               'pebshell':       {'temperature': 300.0, 'moder': 'moder', 'moder_nuclide': 6000, 'nuclides':{ '6000': 6.61814E-2, '5010': 2.23273E-8,  '5011': 9.04368E-7}},
                               'graphite':       {'temperature': 300.0, 'moder': 'moder', 'moder_nuclide': 6000, 'nuclides':{ '6000': 8.67416E-2, '5010': 2.23273E-8,  '5011': 9.04368E-7}},
                               'helium':         {'temperature': 300.0, 'moder': '',      'moder_nuclide': '',   'nuclides':{ '2004': 5.28437E-4}}}

        self._path_to_data_files = data_path
        self.triso_dist_name = 'triso_7grHM_1.triso'
        self.output_dir = './'
        self.template_files = ['serpent.pbs']
        self.save_state_point = False
        self.save_state_point_frequency = 10
        
        self.equilibrium_core = False
        self.equilibrium_materials = None
        self._homogenized_materials_dict = {}
        self.volume_powers = {}
        
        self.fuel_temperature_profile = None
        self.pebble_temperature_profile = None
        
        self.run_in_steps = {} 
        self.lost_pebbles = 0
        self._homogenization_group = 0
        self._pebble_number = 0
        self.current_efpd = 0
        self.steps = 10
        self.allow_sub_crit_flag = False
        self.final_pass_limit = self.pass_limit
        self.final_homogenization_group = self._homogenization_group
        
        # Generation of critical height parameters
        self.critical_keff_tolerance = 0.0005
        self.critical_height_fractions = [0.25,0.5,0.75]
        
        # Pebble bed reactor geometry
        self.pebble_bed_radius = 120.0
        self.pebble_bed_height = 893.0
        self.discharge_chute_radius = 24.0
        self.pebble_bed_axial_offset = 170.0
        
        self.one_run = True
        self.burnup_flag = False

        for k,v in kwargs.items():
            setattr(self, k, v)
            
        self._step_pebble_distribution_file = f'{self.pebble_distribution_file}_Step{self.load_step}.pbed'
        self.discarded_pebbles = {k: [] for k in range(1000)}
        self.log = logutils.LogTracker(log_path=f'{self.output_dir}logger.out')
        self.log.start()

        self.xs_dict = {1500: {'graphite': 'grph1500', 'xs_set': '15c'},
                        1200: {'graphite': 'grph1200', 'xs_set': '12c'},
                         900: {'graphite':  'grph900', 'xs_set': '09c'},
                         600: {'graphite':  'grph600', 'xs_set': '06c'},
                         300: {'graphite':  'grph300', 'xs_set': '03c'},}
        self.core_xs_library, self.core_scattering_library = self.set_xs_set(self.fixed_reactor_temperature)
        self.core_inlet_xs_library, self.core_inlet_scattering_library = self.set_xs_set(self.core_inlet_temperature)
        self.core_outlet_xs_library, self.core_outlet_scattering_library = self.set_xs_set(self.core_outlet_temperature)
        self.pebble_xs_library, self.pebble_scattering_library = self.set_xs_set(self.pebble_temperature)

        if not os.path.isdir(self.output_dir):
            os.makedirs(self.output_dir)

        if self.multiphysics_run:

            path_to_griffin_data = os.path.join(os.path.join(self.output_dir, 'data'))
            if os.path.isdir(path_to_griffin_data) == False:
                os.mkdir(path_to_griffin_data)
            if os.path.isfile(os.path.join(self.output_dir, 'os200mw_gcpbr_7ge15_microxs.xml')) == False:
                shutil.copy(os.path.join(self.path_to_micro_xs, 'os200mw_gcpbr_7ge15_microxs.xml'), os.path.join(path_to_griffin_data, 'os200mw_gcpbr_7ge15_microxs.xml'))

    def assign_fuel_pebble(self, x, y, z, r, p_r, channel, volume, recycled_pebble):
        """
        Determine what happens to a pebbles after it has been unloaded.

        x: float
            x-coordinate of pebble
        y: float
            y-coordinate of pebble
        z: float
            z-coordinate of people
        r: float
            Radius of pebble
        p_r: ?
            ?
        channel: ?
            Radial flow channel that pebble is located in
        volume: ?
            ID of volume where pebble is located?
        recycled_pebble: bool
            If True...

        """
        # Assign all of our previously passed pebbles, and then assign new pebbles if we still need pebbles     
        # Add a function to remove pebble groups that have very few pebbles??
        
        if self.filter_by_pass(recycled_pebble) or self.filter_by_burnup(recycled_pebble):
            fuel_temp, pebble_temp = self.get_temperature(channel,volume)
            self._pebble_number += 1
            self.discarded_pebbles[self._burnstep].append(recycled_pebble)
            return pbl.FuelPebble(x, y, z, r, p_r, channel, volume, fuel_material=self.fuel_material, homogenization_group=self._homogenization_group, pass_limit=self.pass_limit, temperature=pebble_temp, fuel_temperature=fuel_temp, pebble_number=self._pebble_number, kernel_data=self._kernel_data)
        else:
            # We update the previous universe to ensure we maintain tracability of the pebble as it is refueled
            # If we did not do this, each pebble would only every stay in one channel
            new_pebble = recycled_pebble
            if self.homogenize_passes: # If we homogenize the pass, we need to udpate the universe again to account for the homogenization
                uni = f'f{new_pebble._homogenization_group}_' + '_'.join([f'c0v0' for n in range(0,new_pebble._num_passes)])
                new_pebble.set_previous_universe(uni)
                new_pebble._material['fuel'] = self._homogenized_materials_dict[new_pebble._num_passes][new_pebble._homogenization_group]['mats']
            new_pebble.update_position(x, y, z, r, channel, volume, shuffled=True)    
        return new_pebble
        
    def assign_pebble_dist_variables(self, pbcyll=893.0, pblwconl=54.0, pbupconl=0.0, pbr=120.0, 
                       dcr=24.0, axial_offset=0.0, idistrfile='rawdist.txt', odistrfile='findist.txt',
                       chcurvs=None, log=None, trgtchnv=None):
        """
        Assign the variables for the pebble distribution reader.
        """
        self.pebble_bed_height = pbcyll
        self.pblwconl = pblwconl
        self.pbupconl = pbupconl
        self.pbttlen = pbcyll + pblwconl + pbupconl
        self.discharge_chute_radius = dcr
        self.pebble_bed_radius = pbr
        self.pebble_bed_axial_offset = axial_offset
        self.pebble_bed_dimple_radius = pbr + 6.0
        self.idistrfile = idistrfile
        self.odistrfile = odistrfile
        self.chcurvs = chcurvs
        self.trgtchnv = trgtchnv        

    def build_pbr_core(self):
        self.pbr_core = pbr.PebbleBedReactor(output_dir=self.output_dir, pebble_bed_name=self._step_pebble_distribution_file, pebble_bed_height=self.pebble_bed_height,
                                             block_inner_radius=self.pebble_bed_radius, pebble_shoot_radius=self.discharge_chute_radius, 
                                             cr_insertion_depth=self.cr_insertion_depth, sr_insertion_depth=self.sr_insertion_depth, 
                                             create_dimples=self.create_dimples, simple_core=self.simple_core)
        self.pbr_core.build_pbr_core()
        self.pbr_core.write_pbr_core()

    def calculate_average_pebble_feature(self, feature):
        """
        Loop over the array to calculate the average value for a feature based on the fuel type and pass
        """
        feature_dict = {k: {k1: [] for k1 in range(self.final_homogenization_group + 1)} for k in range(self.final_pass_limit)}
        final_feature_dict = {k: {k1: 0. for k1 in range(self.final_homogenization_group + 1)} for k in range(self.final_pass_limit)}
        for ch in self._pebble_array:
            for vol in ch:
                for pebble in vol:
                    if pebble._pebble_type == 'fuel':
                        feature_dict[pebble._num_passes][pebble._homogenization_group].append(getattr(pebble, feature))
        
        for pass_num, pass_group in feature_dict.items():
            for group_num, group in pass_group.items():
                group = list(filter(lambda x: x!=0, group)) # Filter out pebbles which have a 0 for the feature
                avg = sum(group) / len(group) if len(group) > 0 else 0 
                final_feature_dict[pass_num][group_num] = avg
                
        return final_feature_dict
        
    def calculate_discharge_bu(self):
        """
        Calculate the average burnup of the discharged pebbles based on the fuel type
        """
        feature_dict = {k: [] for k in range(self.final_homogenization_group + 1)}
        final_feature_dict = {'max': {}, 'min': {}, 'average': {}}

        for pebble in self.discarded_pebbles[self._burnstep]:
            feature_dict[pebble._homogenization_group].append(pebble._burnup)
        
        for group_num, group in feature_dict.items():
            final_feature_dict['average'][group_num] = sum(group) / len(group) if len(group) > 0 else 0
            final_feature_dict['max'][group_num] = max(group) if len(group) > 0 else 0
            final_feature_dict['min'][group_num] = min(group) if len(group) > 0 else 0
            
        return final_feature_dict
    
    def calculate_maximum_pebble_power(self):
        """
        Read in the pbed.out file and determine the maximum pebble power in the core, along with the universe it is in.
        """
        pebble_power_file = f'{self._step_pebble_distribution_file}_pow{self.critical_timestep}' if self.serpent_version == '2.2' else self._step_pebble_distribution_file

        file_name = os.path.join(self.output_dir, f'step_{self._burnstep}', f'{pebble_power_file}.m')
        f = open(file_name) 
        power = []
        power_err = []
        universe = []
        for line in f:
            split_line = line.split(' ')
            power.append(float(split_line[-2])/ 1000) #Convert this from W to kW
            power_err.append(float(split_line[-1])/ 1000)
            universe.append(split_line[-4])
        max_power = max(power)
        index = power.index(max_power)
        return (max_power, power_err[index], universe[index])
            
    def create_temperature_profile(self, min_temp, max_temp, profile, axial_zones=None, axial_heights=None):
        """
        Generates a new temperature profile for the fuel and/or pebble materials. 
        The temperature is based on a linear temperature rise though the core. 
        The number of axial zones determines how many different temperature will be used. 
        Axial heights can be set by the user to enforce temperature zones, or they can be generated automatically by cutting the core into equal parts based on the number of axial zones.
        """
        delta_t = self.core_outlet_temperature - self.core_inlet_temperature

        if axial_heights:
            axial_zones = len(axial_heights)
            axial_heights = [(height, round(delta_t / (len(axial_heights)-1) * num)) for num, height in enumerate(axial_heights)] 
        else:
            axial_heights = [(self.pbttlen / axial_zones * num, round(delta_t / (axial_zones-1) * num)) for num in range(axial_zones)]


        if delta_t == 0.:
            print(f'Warning: Temperature increase over core is 0 (inlet temp: {self.core_inlet_temperature}, outlet temp: {self.core_outlet_temperature}), profile should have varying inlet/outlet temperature; use "fixed_temperature_profile", "fuel_temperature", and/or "pebble_temperature". Temperature for {profile} will be set to the min_{profile}_temperature.\n')
        if profile != 'fuel' and profile != 'pebble':
            raise Exception(f'Temperature profile ({profile}) is not recognized, please select from "fuel" or "pebble"')

        # We fix the initial zone to the inlet temperature and final zone to the outlet temperature
        # If we are only given a series of heights, we need to add the temperature associated with each height.

        temp_dict = {}
        for channel, num_volumes in enumerate(self.trgtchnv):
            channel_height_increment = self.pbttlen / num_volumes
            volumes = list(reversed(range(num_volumes)))
            heights = [self.pbttlen - channel_height_increment * num for num in volumes]
            for volume in volumes:
                for lower_height, temp in axial_heights:
                    if heights[volume] >= lower_height:
                        temp_frac = temp / (delta_t) if delta_t > 0 else 0
                        temp_dict[f'{channel}{volume}'] = round(temp_frac * (max_temp - min_temp)) + min_temp
        return temp_dict

    def create_griffin_file(self):
        """
        Utilize the cartographer mapping module to create a Griffin input file
        """
        from kugelpy.kugelpy.kugelpy_open_source.cartographer.griffin_mapper import GriffinMap

        pebble_file_path = os.path.join(self.output_dir, self._step_pebble_distribution_file)

        self.gmap = GriffinMap(path_to_output_files = self.output_dir,
                          pebble_dictionary = self.pebble_material_volume_data,
                          pebble_distribution = pebble_file_path,
                          step=self._burnstep,
                          power_level=self.power_level,
                          pebble_temperature=self.pebble_temperature,
                          reflector_temperature=self.core_outlet_temperature
                          )               
        self.gmap.map_to_griffin()
        self.gmap.create_griffin_input()

        path_to_griffin_data = os.path.join(os.path.join(self.output_dir, 'data'))

        # grab the remaining files required for Griffin
        files = ['gpbr200_mesh_gfnk.e', 'gpbr200_mesh_phth.e', 'void.xml', 'os200mw_gcpbr_mesh_msht_cntr.txt']    
        for file in files:
            if os.path.isfile(os.path.join(path_to_griffin_data, file)) == False:
                shutil.copy(os.path.join(self.gmap.data_path, file), os.path.join(path_to_griffin_data, file))

    def run_griffin(self,step):
        """
        Run the coupled Griffin/Pronghon simulation to get the temperature profile
        """
        #fin = open(os.path.join(self.gmap.data_path, 'griffin_run.pbs'), 'r')
        fin = open(os.path.join(self.gmap.data_path, 'run_griffin.sh'), 'r')
        #fout = open(os.path.join(self.output_dir, 'griffin_run.pbs'), 'w')
        fout = open(os.path.join(self.output_dir, 'run_griffin.sh'), 'w')
        for line in fin:
            fout.write(line.replace('input_name', f'gpbr200_ri_griffin_step{self._burnstep}.i') )
        fin.close()
        fout.close()

        cwd = os.getcwd()
        os.chdir(self.output_dir)
        print(f'Starting Griffin/Pronghorn Step {self._burnstep}')
        os.system('chmod +rwx run_griffin.sh ')
        os.system('./run_griffin.sh')
        #os.system('qsub -W block=true griffin_run.pbs')
#        os.system(f'blue_crab-opt -i gpbr200_ri_griffin_step{self._burnstep}.i')
        os.chdir(cwd)        

    def determine_data_path(self):
        if os.path.isdir(os.path.join(self.output_dir, f'step_{self._burnstep}')) == True and self.refine_burnstep == False:
            dir_ = os.path.join(self.output_dir, f'step_{self._burnstep}')
        else:
            dir_ = self.output_dir
        return dir_

    def determine_pebble_type(self, graphite_height, graphite_fraction, z):
        """
        Determine if we have a fuel pebble or graphite pebble based on the graphite height set by the user, and the graphite fraction in the core
        """
        peb_type = 'graphite' if z < graphite_height or random.random() < graphite_fraction else 'fuel'
        return peb_type

    def determine_reactor_state(self):
        """
        Determine the state of the reactor based on k-eff. 
        If we don't care about criticality, set k-eff to our last value in the list.
        If we are above the target k-eff, select the smallest k-eff that is above the target k-eff.
        If we are below the target k-eff, but above our allowable k-eff, select the largest k-eff that is below the target k-eff
        If we are have failed to find an acceptable k-eff, and we have already refined the burnstep, select the um-burned k-eff.
        If we are have failed to find an acceptable k-eff, and we have not already refined the burnstep, set the flag to refine the burnstep.
        Update the number of days.
        """
        self.read_keff()
        print("Finished reading in res file")

        initial_keff = self.keff[0]
        max_keff = self.keff[1:].max()

        if self.allow_sub_crit_flag == True:
            val_keff = self.keff[-1]
        elif max_keff >= self.target_keff:
            val_keff = self.keff[self.keff >= self.target_keff].min()
        elif max_keff >= self.allowable_keff:
            val_keff = max_keff
        elif self.refine_burnstep:
            val_keff = initial_keff
        else:
            print('Warning: Core failed to create a viable time step, refining the time step and trying again.')
            val_keff = None
            self.refine_burnstep = True
            return

        self.critical_timestep = np.where(self.keff == val_keff)[0][0]
        depletion_steps = self.temp_depletion_steps if self.refine_burnstep else self.depletion_steps
        self.current_efpd = sum(depletion_steps[:self.critical_timestep]) if self.critical_timestep > 0 else 0 
        self._efpd_tracker += self.current_efpd
        print(f'Selecting k-eff of {val_keff} from position {self.critical_timestep} given list of k-eff {self.keff}')
        print(f'Current time step: {self.current_efpd}; total days {self._efpd_tracker}\n')
        return

    def equilibrium_pebble_generator(self,x,y,z,r,pr,channel_num,volume_num,fuel_temp,pebble_temp):
        """
        Create a fuel pebble based on equilibrium fuel material
        """
        fuel_material, pebble_pass = random.choice(self.equilibrium_materials[f'c{channel_num}v{volume_num}'])
        pebble = pbl.FuelPebble(x,y,z,r,pr,channel_num,volume_num, homogenization_group=self._homogenization_group, fuel_material=fuel_material, temperature=pebble_temp, pass_limit=self.pass_limit, fuel_temperature=fuel_temp, pebble_number=self._pebble_number, kernel_data=self._kernel_data)
        pebble._num_passes = pebble_pass
        uni = f'f{self._homogenization_group}_' + '_'.join(['c0v0' for n in range(0,pebble_pass)])
        pebble._universe = f'{uni}_c{channel_num}v{volume_num}' if pebble_pass > 0 else f'{uni}c{channel_num}v{volume_num}'
        pebble.set_previous_universe(uni)
        pebble._shuffled = True if pebble_pass > 0 else False
        return pebble

    def filter_by_burnup(self, pebble):
        """
        Flag pebbles that have accrued a BU greater than the BU limit
        """
        if pebble._burnup >= self.burnup_limit:
            return True
        return False
        
    def filter_by_pass(self, pebble):
        """
        Glag pebbles that have taken more passes through the core than the pass limit
        """
        if pebble._num_passes >= pebble._pass_limit:
            return True
        return False

    def get_number_of_pebbles_in_volume(self, universe):
        """
        Get the number of pebbles of the same burnup group in a volume
        """
        last_uni = universe.split('_')[-1]
        volume_num = int(last_uni.split('v')[1])
        channel_num = int(last_uni.split('v')[0].split('c')[1])
        return len([x for x in self._pebble_array[channel_num][volume_num] if x._universe == universe])
    
    def get_temperature(self, channel_num, volume_num):
        """
        Grab the temperature of the fuel and pebble based on a 2D temperature profile
        """
        fuel_temp = self.round_temperature(self.fuel_temperature_profile[f'{channel_num}{volume_num}'], base=self.minimum_temperature_difference) if self.fuel_temperature_profile else self.fuel_temperature
        pebble_temp = self.round_temperature(self.pebble_temperature_profile[f'{channel_num}{volume_num}'], base=self.minimum_temperature_difference) if self.pebble_temperature_profile else self.pebble_temperature

        return fuel_temp, pebble_temp
    
    def round_temperature(self, x, base=50):
        return int(base * round(x / base))

    def homogenize_materials(self):
        """
         To homogenzie the material, we need to multiply the volume by the atom density for each region and each pass
         These atom densities are summed over the channels and divided by the total volume of pebbles being discharged
        """
        new_mat_dict = {k: {} for k in range(1,self.pass_limit+1)}
        for univ_pass in range(1, self.pass_limit+1):
            total_vol = {}
            for pebble_homog_group in range(self._homogenization_group+1):
                homog_material = {}
                total_vol[pebble_homog_group] = 0
                for channel in range(0,len(self._pebble_array)):
                    discharge_volume_num = len(self._pebble_array[channel]) - 1
                    prev_univ = '_'.join([f'c0v0' for n in range(1,univ_pass)])
                    univ = f'f{pebble_homog_group}_{prev_univ}_c{channel}v{discharge_volume_num}' if prev_univ else f'f{pebble_homog_group}_c{channel}v{discharge_volume_num}'
                    new_mat_dict[univ_pass][pebble_homog_group] = {}
                    if univ in self._burnup_materials[self.critical_timestep].keys():
                        old_mat = self._burnup_materials[self.critical_timestep][univ]
                        volume = old_mat['volume']
                        total_vol[pebble_homog_group] += volume
                        homog_mat = {isotope: (a_dens * volume) for isotope, a_dens in old_mat.items() if 'volume' not in isotope}
                        homog_material = self.combine_dicts(homog_material, homog_mat)
                    new_mat_dict[univ_pass][pebble_homog_group]['mats'] = homog_material
                    new_mat_dict[univ_pass][pebble_homog_group]['vol'] = total_vol[pebble_homog_group]
                    
        for num_pass, new_pass_dict in new_mat_dict.items():
            for pebble_homog_group in range(self._homogenization_group+1):
                temp_dict = {isotope: a_dens / new_pass_dict[pebble_homog_group]['vol'] for isotope, a_dens in new_pass_dict[pebble_homog_group]['mats'].items()}
                new_pass_dict[pebble_homog_group]['mats'] = temp_dict
        
        self._homogenized_materials_dict = new_mat_dict

    def homogenize_materials_by_burnup_group(self):
        bu_groups = [0,25,50,75,100,125,150,175]
        new_mat_dict = {k: {} for k in bu_groups}
        
        total_vol = {}
        for pebble_homog_group in range(self._homogenization_group+1):
            homog_material = {}
            total_vol[pebble_homog_group] = 0
            for channel in range(0,len(self._pebble_array)):
                discharge_volume_num = len(self._pebble_array[channel]) - 1
 
    def update_time_stepper(self, step):
        """
        If we fail to create a burned core with a viable k-eff, refined our depletion steps and perform our run again.
        """
        min_step1 = self.depletion_steps[0] / 4
        min_step2 = self.depletion_steps[0] / 2
        self.temp_depletion_steps = [min_step1, min_step2]
        self.write_serpent_input()
        self.run_serpent(step)
        self.determine_reactor_state()

    def perform_burnstep(self, step=0):
        """
        Read in output files from the current step, shift pebbles in the core, and reassign materials for pebbles.
        """
        self._burnstep = step
        if self.save_state_point and self._burnstep % self.save_state_point_frequency == 0:
            self.save(step)

        self.determine_reactor_state()
        if self.refine_burnstep == True:
           self.update_time_stepper(step)
        self.refine_burnstep = False
        
        if self.keep_files:
            self.keep_solutions(step)
   
        self.update_temperature_profile()
        self.read_volume_powers()
        self.update_run_in_step()
        self.update_core_temperatures()
        self.read_burn_material(step=step)
        self.shift_pebbles()
        self.refuel_pebbles()
        if not self.one_run:
            self.write_serpent_pbs()
        num_mats = len(self._burnup_materials[0])
        self.update_solution_file()
        self._step_pebble_distribution_file = f'{self.pebble_distribution_file}_Step{step+1}.pbed'
        print(f'Executing Run-In Step {step}, at {self._efpd_tracker} EFPDs, with {num_mats} materials')
                
    def perform_criticality_search(self):
        """
        Determine the height of graphite pebbles required to obtain a critical core.
        
        Parameters
        ----------
        initial_graphite_height : float
            Initial height of graphite pebbles in the core, can be a height (cm) of fraction of the total height (fraction)
        graphite_height_perturbation : float
            Initial guess for increasing/decreasing the graphite height of the core to determine the next step
        """
        criticality_keff = []
        criticality_heights = []
        tolerance = 1.0
        self.create_solutions_file()
        
        for height in self.critical_height_fractions:
            self.graphite_height = (self.pebble_bed_height) * height
            self._burnstep = self.graphite_height
            self.read_in_pebble_dist()
            self.setup_core()
            self.run_serpent(f'crit - {height}')
            self.read_keff()
            criticality_keff.append(float(self.keff[0]))
            criticality_heights.append(copy.copy(self.graphite_height))
            if self.keep_files:
                self.keep_solutions(self.graphite_height)
#            self.update_solution_file()

        while tolerance > self.critical_keff_tolerance:
            reg_model = interp1d(criticality_keff, criticality_heights, kind='linear', fill_value='extrapolate')
            est_crit_height = reg_model(self.target_keff)
            self.graphite_height = est_crit_height
            self._burnstep = self.graphite_height
            self.read_in_pebble_dist()
            self.setup_core()
            self.run_serpent(f'crit - {height}')
            self.read_keff()
            criticality_keff.append(float(self.keff[0]))
            criticality_heights.append(copy.copy(self.graphite_height))
            if self.keep_files:
                self.keep_solutions(self.graphite_height)
 #           self.update_solution_file()
            tolerance = abs(self.keff[0] - self.target_keff) / (self.keff[0] * self.target_keff)
            print(f'Estimated CR Height: {est_crit_height}, k-eff: {self.keff[0]}, Tolerance: {tolerance}')
        self.load_step = 1
        self._burnstep = 0
            
    def perform_run_in(self):
        """
        Perform a set number of steps for a core simulation.
        """
        
        if self.load_step == 1:
            self.create_solutions_file()
            self.update_temperature_profile()
            self.read_in_pebble_dist()

        for step in range(self.load_step,self.steps+1):
            print(f'Setting up Core Configuration for Step {step}')
            self.setup_core()
            print(f'Running Serpent Calculation for Step: {step}\n')
            print(f'Reactor Power: {self.power_level} W, Current EFPD: {self._efpd_tracker}')
            time1 = time.time()
            if step >= self.start_step:
                self.run_serpent(step)
                if self.multiphysics_run:
                    self.create_griffin_file()
                    self.run_griffin(step)
            time_ = time.time() - time1
            print(f'Serpent calculation for step {step} complete, took {time_}s to complete\n\n')
            self.perform_burnstep(step=step)
            self.graphite_height = 0.0
            if self._efpd_tracker > self.day_limit:
                break

        print(f'Completed run-in with {self._burnstep} steps.')

    def read_burn_material(self, step=0):
        """
        Read in the materials from the .bumat file from the current step to create a new material for the next step/
        """
        dir_ = self.determine_data_path()

        temp_dict = su.bu_reader(dir_)
            
        for step_, step_dict in temp_dict.items():
            self._burnup_materials[step_] = {}
            for mat, mat_dict in step_dict.items():
                mat_split = mat.split('_')
                material = ''.join([f'{mat_temp}_' for mat_temp in mat_split if 'c' in mat_temp])
                material = mat_split[1] + '_' + material.split('p')[0]
                self._burnup_materials[step_][material] = self.prune_burn_material(mat_dict)
           
    def read_burn_material_restart(self):
        """
        Create the burnup materials for each material in each axial zone based on a previous run's materials
        """
        start_step_path = os.path.join(self.output_dir, f'step_{self.start_step}')
        if not os.path.isdir(start_step_path):
            print('Error: Path to restart materials does not exist.')
        temp_dict = su.bu_reader(start_step_path) 
            
        for step, step_dict in temp_dict.items():
            self._burnup_materials[step] = {}
            for mat, mat_dict in step_dict.items():
                mat_split = mat.split('_')
                material = ''.join([f'{mat_temp}_' for mat_temp in mat_split if 'c' in mat_temp])
                material = material.split('p')[0]
                current_block = material.split('_')[-1]
                num_passes = len(material.split('_')) -  1# We subtract off 1 becuase the pebbles have not gone through the full pass yet, the last value is their current pass

                if current_block in self._burnup_materials[step].keys():
                    self._burnup_materials[step][current_block].append((num_passes, self.prune_burn_material(mat_dict)))
                else:
                    self._burnup_materials[step][current_block] = [(num_passes, self.prune_burn_material(mat_dict))]

    def read_keff(self):
        """
        Read k-eff from the output file and return a list with all of the keff values based on BU
        """
        dir_ = self.determine_data_path()
        depletion_steps = self.temp_depletion_steps if self.refine_burnstep else self.depletion_steps
        print(f"Checking material IDs: {self.refine_burnstep}, {self.temp_depletion_steps}, {self.depletion_steps}")
        total_steps = len(depletion_steps) + 1 # we add 1 to account for the range method
        path_serpent_output = os.path.join(dir_, f'{self.reactor_file_name}_res.m')
        k_name = 'COL_KEFF' if self.serpent_version == '2.2' else 'IMP_KEFF'
        keff = su.serpent_rd(path_serpent_output,[k_name],[x for x in range(0,total_steps)])
        self.keff = np.array([float(x) for x in keff[k_name]])       
                        
    def read_in_pebble_dist(self):
        """
        Create the pebble distribution file using GenPBDist
        
        Note: We have to make a copy of chcurvs because it gets updated in GenPBDist, if we don't copy it will update self.chcurvs as well
        """
        self.pebble_dist = GenPBDist(pbcyll=self.pebble_bed_height, pblwconl=self.pblwconl, pbupconl=self.pbupconl, pbr=self.pebble_bed_radius, pbdr=self.pebble_bed_dimple_radius,
                                     dcr=self.discharge_chute_radius, axial_offset=self.pebble_bed_axial_offset, idistrfile=self.idistrfile, odistrfile=self.odistrfile,
                                     chcurvs=copy.deepcopy(self.chcurvs), log=self.log, trgtchnv=self.trgtchnv)
        
        self.pebble_dist.gen_distr()
        self.pebble_dist.divide_channels()
        self.pebble_dist.divide_sort_volumes()
        
        self.pebble_mesh = self.pebble_dist.chanvolpart
        self._pebble_array = []
        for channel_num, channel in enumerate(self.pebble_mesh):
            self._pebble_array.append([])
            for volume_num, volume in enumerate(channel):
                self._pebble_array[channel_num].append([])
                for peb_pos, pebble in enumerate(volume):
                    x,y,z,r,pr = self.pebble_dist.xv[pebble], self.pebble_dist.yv[pebble], self.pebble_dist.zv[pebble], self.convert_xy_to_r(self.pebble_dist.xv[pebble], self.pebble_dist.yv[pebble]), self.pebble_dist.pr
                    fuel_temp, pebble_temp = self.get_temperature(channel_num,volume_num)
                    self._pebble_number += 1
                    if self.determine_pebble_type(self.graphite_height, self.graphite_fraction, z) == 'fuel':
                        peb_class = self.equilibrium_pebble_generator(x,y,z,r,pr,channel_num,volume_num,fuel_temp,pebble_temp) if self.equilibrium_core else pbl.FuelPebble(x,y,z,r,pr,channel_num,volume_num,homogenization_group=self._homogenization_group,fuel_material=self.fuel_material, pass_limit=self.pass_limit, temperature=pebble_temp, fuel_temperature=fuel_temp, pebble_number=self._pebble_number, kernel_data=self._kernel_data)
                    else:
                        peb_class = pbl.Pebble(x,y,z,r,pr,channel_num,volume_num,temperature=pebble_temp,pebble_number=self._pebble_number)
                    self._pebble_array[channel_num][volume_num].append(peb_class)
                self._pebble_array[channel_num][volume_num].sort(key=lambda pebble : pebble._z, reverse=True) # Order the pebbles based on based on pebble height
    
    def read_volume_powers(self):
        """
        Read in the power detection file to grab the total power in each volume of the core.
        Power is reported in MW.
        """
        correct_line = False
        dir_ = self.determine_data_path()
        print(f'Reading volume power for step {self._burnstep} in {dir_}')
        #depletion_steps = self.temp_depletion_steps if self.refine_burnstep else self.depletion_steps
        ## loop over all of the steps in the depletion steps
        ## we include an additional one for the first time step that does not deplete
        #for depletion_step in range(len(depletion_steps) + 1): 
        self.volume_powers = {}
        power_file = os.path.join(dir_, f'{self.reactor_file_name}_det{self.critical_timestep}.m')
        ignore = ['detE', 'detR', 'detPHI', 'detX', 'detY', 'detZ', 'mesh']
        include = ['DET']
        record_detector = False
        with open(power_file,'r') as f:
            for num, line in enumerate(f):
                if correct_line:
                    split_line = line.split(' ')
                    power, power_unc = split_line[-3], split_line[-2]
                    self.volume_powers[volume] = (float(power), float(power_unc))
                    correct_line = False
                # only pull out power densities, not detector mesh
                for prefix in include:
                    if prefix in line:
                        record_detector = True
                for suffix in ignore:
                    if suffix in line:
                        record_detector = False
                if record_detector:
                    split_line = line.split(' ')[0]
                    volume = split_line.split('DET')[1]
                    record_detector = False
                    correct_line = True
                
    def refuel_pebbles(self):
        """
        Place pebbles that were shifted out of the core back into the top of the core. We filter based on BU/# of passses and add fresh fuel/graphite pebbles if necesssary.
        """
        random.shuffle(self._unloaded_pebbles)
        self._unloaded_fuel_pebbles = [pebble for pebble in self._unloaded_pebbles if pebble._pebble_type == 'fuel']
        self.pebbles_per_volume_unload = {}
        for pebble in self._unloaded_fuel_pebbles:
            if pebble._universe in self.pebbles_per_volume_unload.keys():
                self.pebbles_per_volume_unload[pebble._universe] += 1
            else:
                self.pebbles_per_volume_unload[pebble._universe] = 1
                       
        reload_volume = []
        new_channel = {}
        for channel_num, channel in enumerate(self.pebble_mesh):
            new_channel[channel_num] = []
            for pebble in channel[0]:
                reload_volume.append((channel_num, copy.copy(pebble)))
        random.shuffle(reload_volume)

        for channel_num, pebble in reload_volume:
            x,y,z,r,pr = self.pebble_dist.xv[pebble], self.pebble_dist.yv[pebble], self.pebble_dist.zv[pebble], self.convert_xy_to_r(self.pebble_dist.xv[pebble], self.pebble_dist.yv[pebble]), self.pebble_dist.pr
            if len(self._unloaded_fuel_pebbles):
                recycle_pebble = self._unloaded_fuel_pebbles.pop()
                recycle_pebble.increase_pass()
                pebble_power_days = self.volume_powers[recycle_pebble._universe] 
                pebbles_per_volume = self.pebbles_per_volume_unload[recycle_pebble._universe]
                recycle_pebble.update_burnup((pebble_power_days[0] / pebbles_per_volume), self.current_efpd)
                new_pebble = self.assign_fuel_pebble(x, y, z, r, pr, channel_num, 0, recycle_pebble)
                fuel_temp, pebble_temp = self.get_temperature(channel_num, 0)
                new_pebble.update_pebble_temperature(pebble_temp, fuel_temp=fuel_temp)
            else:
                peb_type = self.determine_pebble_type(self.graphite_height, self.graphite_fraction, z)
                self._pebble_number += 1
                fuel_temp, pebble_temp = self.get_temperature(channel_num, 0)
                if peb_type == 'graphite':
                    new_pebble = pbl.Pebble(x, y, z, r, pr, channel_num, 0, temperature=pebble_temp,pebble_number=self._pebble_number) 
                elif self.equilibrium_core:
                    new_pebble = self.equilibrium_pebble_generator(x,y,z,r,pr,channel_num,0,fuel_temp,pebble_temp)
                else:
                    new_pebble = pbl.FuelPebble(x, y, z, r, pr, channel_num, 0, homogenization_group=self._homogenization_group, fuel_material=self.fuel_material, pass_limit=self.pass_limit, temperature=pebble_temp, fuel_temperature=fuel_temp, pebble_number=self._pebble_number, kernel_data=self._kernel_data)
            new_channel[channel_num].append(new_pebble) 

        
        for channel_num, channel in enumerate(self.pebble_mesh):    
            self._pebble_array[channel_num][0] = new_channel[channel_num]
            self._pebble_array[channel_num][0].sort(key=lambda pebble : pebble._z, reverse=True) # Order the pebbles based on based on pebble height
 
    def set_xs_set(self, temperature):
        """
        Set the cross-section set based on the temperature of the component.
        """
        dict_array = np.array([x for x in self.xs_dict.keys()])
        temp = dict_array[dict_array<temperature].max() if temperature not in self.xs_dict.keys() else temperature
        return self.xs_dict[temp]['xs_set'], self.xs_dict[temp]['graphite']

    def setup_kernel(self, fuel_radius=0.02125, buffer_radius=0.03125, inner_pyc_radius=0.03525, sic_radius=0.03875, outer_pyc_radius=0.04275, kernels_per_pebble=18687):
        """
        Set up the fuel kernel data
        """
        self._kernel_data['fuel'] = fuel_radius
        self._kernel_data['buffer'] = buffer_radius
        self._kernel_data['inner_pyc'] = inner_pyc_radius
        self._kernel_data['sic'] = sic_radius
        self._kernel_data['outer_pyc'] = outer_pyc_radius
        self._kernel_data['kernels_per_pebble'] = kernels_per_pebble            

    def setup_core(self):
        """
        Set up all necessary files for running a serpent job
        """      
        self.update_core_temperatures()
        self.write_pebble_data()
        self.write_pebble_location_file()
        self.build_pbr_core()
        self.write_serpent_input()
        self.write_materials_file()
        if not self.one_run:
            self.write_serpent_pbs()
        
    def shift_pebbles(self):
        """
        Shift pebbles in each channel down one volume. Volumes at the bottom of the core will be stored in the unloaded_pebbles list to be refueled.
        """
        self.pebbles_per_volume = {}
        self._unloaded_pebbles = []

        new_mesh = [[[] for volume in column] for column in self._pebble_array]
        for channel_num, channel in enumerate(self._pebble_array):
            for prev_vol_num, volume in enumerate(channel[1:]): #Skip the first axial volume, as this will be refilled with discharged pebbles
                volume_num = prev_vol_num + 1
                prev_vol = self._pebble_array[channel_num][prev_vol_num]
                for peb_pos, pebble in enumerate(prev_vol):
                    if pebble._universe not in self.pebbles_per_volume.keys():
                        self.pebbles_per_volume[pebble._universe] = self.get_number_of_pebbles_in_volume(f'{pebble._universe}')
                    pebble = copy.deepcopy(pebble) # Grab each pebble in the current volume
                    if peb_pos < len(volume): # Make sure the previous volume has enough pebbles to pull from 
                        if pebble._pebble_type =='fuel': # Update fuel pebbles with material compositions from the previous volume
                            pebble_power_days = self.volume_powers[pebble._universe]
                            num_pebbles_in_volume = self.pebbles_per_volume[pebble._universe]
                            pebble.update_burnup((pebble_power_days[0] / num_pebbles_in_volume), self.current_efpd)
                            fuel_temp, pebble_temp = self.get_temperature(channel_num,volume_num)
                            self.update_fuel_pebble(pebble, fuel_temp, pebble_temp)
                        new_pebble = volume[peb_pos]
                        pebble.update_position(new_pebble._x, new_pebble._y, new_pebble._z, new_pebble._r, new_pebble._channel_num, new_pebble._volume_num)
                        new_mesh[channel_num][volume_num].append(pebble)
                    else:
                        self.lost_pebbles += 1
                if volume_num == len(channel)-1: # If we are in the last volume, unload pebbles for refuel/discharge
                    self._unloaded_pebbles += volume 

        print(f'Warning: Lost pebble due to inconsistent volumes. Total Lost Pebbles: {self.lost_pebbles}')
        self._pebble_array = new_mesh
        if self.homogenize_passes:
            self.homogenize_materials()
        
    def update_core(self):
        """
        Update the pebble location file (pbed file) and pebble files
        """
        self.write_pebble_location_file()
        self.write_pebble_data()

    def update_core_temperatures(self):
        """
        Update the non-fuel components temperatures based on the core inlet and oulet temperature
        """
        
        self.core_materials['control_rod']['temperature'] = self.core_inlet_temperature
        self.core_materials['safety_rod']['temperature'] = self.core_inlet_temperature
        self.core_materials['reflector']['temperature'] = self.core_inlet_temperature
        self.core_materials['outlet_channel']['temperature'] = self.core_outlet_temperature
        self.core_materials['outlet_plenum']['temperature'] = self.core_outlet_temperature
        self.core_materials['pebble_shoot']['temperature'] = self.core_outlet_temperature
        self.core_materials['pebshell']['temperature'] = self.pebble_temperature
        self.core_materials['helium']['temperature'] = self.pebble_temperature
        self.core_materials['graphite']['temperature'] = self.pebble_temperature
        
    def update_fuel_pebble(self, pebble, fuel_temp, pebble_temp):
        """
        Update the universe, material, and temperatures for fuel pebbles
        """
        prev_univ = pebble._universe
        pebble.set_previous_universe(prev_univ)
        pebble.update_fuel_material(self._burnup_materials[self.critical_timestep][f'{prev_univ}'])
        pebble.update_pebble_temperature(pebble_temp, fuel_temp=fuel_temp)
        #return pebble
        
    def update_run_in_step(self):
        """
        Look at the set of steps and update and state parameters as necessary.
        We perform this by looking for the last applicable time step and setting our attibutes.
        """
        if len(self.run_in_steps) == 0:
            return

        for day, updates in self.run_in_steps.items():
            if self._efpd_tracker >= day:
                for k,v in updates.items():
                    setattr(self,k,v)
                self.pebble_xs_library, self.pebble_scattering_library = self.set_xs_set(self.pebble_temperature) 
                
        # If the fuel needs to be transitioned, update the homogenization group and fuel material
        if self.transition_fuel_flag:
            self.fuel_material = self.equilibrium_fuel_material 
            self._homogenization_group = 1
            self.equilibrium_core =  False

    def update_temperature_profile(self):
        """
        Update the temperature profile based on the current temperature limits in the simulation
        """
        
        if self.create_temperature_profile_flag:
            self.fuel_temperature_profile = self.create_temperature_profile(self.min_fuel_temperature, self.max_fuel_temperature, 'fuel', axial_zones=self.temperature_axial_zones,  axial_heights=self.axial_heights)
            self.pebble_temperature_profile = self.create_temperature_profile(self.min_pebble_temperature, self.max_pebble_temperature, 'pebble', axial_zones=self.temperature_axial_zones,  axial_heights=self.axial_heights)
        elif self.multiphysics_run and self._burnstep != 0:
            serpent_dict, self.griffin_temperature_dict = self.gmap.read_griffin_temperature()
            self.fuel_temperature_profile = self.griffin_temperature_dict
            self.pebble_temperature_profile = self.griffin_temperature_dict

    def create_solutions_file(self):
        solution_path = os.path.join(self.output_dir, 'reactor_status.csv')

        discharge_bu = self.calculate_discharge_bu()
        bu = self.calculate_average_pebble_feature('_burnup')
        power = self.calculate_average_pebble_feature('_power_density')

        if not os.path.isfile(solution_path):
            with open(solution_path, 'w',  encoding='UTF8') as f:
                writer = csv.writer(f)
                row_1 = ['total_days', 'day_time_step', 'fuel_temp', 'pebble_temp', 'control_rod_insertion_depth', 'power', 'power_days', 'fuel_type', 'initial_graphite_height', 'graphite_fraction_added', 'graphite_fraction_left', 
                         'keff_initial', 'keff_final', 'reactivity_loss', 'fuel_pebble_discard_rate', 'total_pebble_discharge_rate']
                row_2 = [f'avg_discharge_bu_group{group}' for group in discharge_bu['average'].keys()]
                row_3 = [f'min_discharge_bu_group{group}' for group in discharge_bu['min'].keys()]
                row_4 = [f'max_discharge_bu_group{group}' for group in discharge_bu['max'].keys()]
                row_5 = [f'avg_bu_group{group}_pass{pass_}' for pass_, passes in bu.items()
                                                             for group in passes.keys()
                                                            ]
                row_6 = [f'avg_power_density_group{group}_pass{pass_}' for pass_, passes in power.items()
                                                                         for group in passes.keys()
                                                            ]
                row_7 = ['max_pebble_power', 'max_pebble_power_err', 'max_pebble_power_universe']
                row = row_1+row_2+row_3+row_4+row_5+row_6+row_7
                writer.writerow(row)

    def calculate_pebble_fractions(self):
        """
        Calculate the pebble type and pass in each universe.
        """
        pebble_file_path = os.path.join(self.output_dir, f'step_{self._burnstep}', self._step_pebble_distribution_file)
        pebble_file =  open(pebble_file_path, 'r')
        pass_dict = {'f0': {x:0 for x in range(1,7)},
                     'f1': {x:0 for x in range(1,7)},
                     'g':  {x:0 for x in range(1,7)}}
        
        pebbles = 0
        for pebble in pebble_file:
            x, y, z, radius, univ = float(pebble[:11]), float(pebble[12:22]), float(pebble[23:32]), float(pebble[33:36]), pebble[37:]
            if '_' in univ:
                split_u = univ.split(' ')
                split_u = [x for x in split_u if '_' in x]
                split_u = split_u[0].split('_')[0]
                split_u = ''.join(split_u.split())
                passes = len([x for x in univ.split('_') if 'c' in x])
                pass_dict[split_u][passes] += 1 
                pebbles += 1     
        return pass_dict, pebbles

    def update_solution_file(self):
        """
        Write down important information to a csv file for ease of reading
        """        
        solution_path = os.path.join(self.output_dir, 'reactor_status.csv')

        power = self.calculate_average_pebble_feature('_power_density')
        max_power, max_power_err, max_univ = self.calculate_maximum_pebble_power()
        bu = self.calculate_average_pebble_feature('_burnup')
        discharge_bu = self.calculate_discharge_bu()
        
        pass_dict, pebbles = self.calculate_pebble_fractions()
        graph_frac = round(pass_dict['g'][1]/pebbles,5)
        
        if graph_frac < 0.01 and self.automatic_fuel_transition:
            self.transition_fuel_flag = True
            if self.burnup_flag:
                self.burnup_limit = 150
                self.pass_limit = 15
            
        with open(solution_path, 'a', newline='',  encoding='UTF8') as f:
            rx_drop = (self.keff[0] - self.keff[self.critical_timestep]) / (self.keff[0] * self.keff[self.critical_timestep]) * 1E5
            self._power_days += self.current_efpd * self.power_level
            pebbles_discharged = len(self.discarded_pebbles[self._burnstep]) / self.current_efpd if self.current_efpd != 0 else 0
            total_pebbles_discharged = len(self._unloaded_pebbles) / self.current_efpd if self.current_efpd != 0 else 0
            writer = csv.writer(f)
            row_1 = [self._efpd_tracker, self.current_efpd, self.fuel_temperature, self.pebble_temperature, self.cr_insertion_depth, self.power_level, self._power_days, self._homogenization_group, self.graphite_height, self.graphite_fraction, graph_frac, 
                     self.keff[0], self.keff[self.critical_timestep], rx_drop, pebbles_discharged,total_pebbles_discharged]
            row_2 = [bu for bu in discharge_bu['average'].values()]
            row_3 = [bu for bu in discharge_bu['min'].values()]
            row_4 = [bu for bu in discharge_bu['max'].values()]
            row_5 = [bu for pass_, passes in bu.items()
                        for bu in passes.values()]
            row_6 = [power for pass_, passes in power.items()
                           for power in passes.values()]  
            row_7 = [max_power, max_power_err, max_univ]   
            row = row_1+row_2+row_3+row_4+row_5+row_6+row_7
            writer.writerow(row)
            
    def write_cells(self, f, pebble):
        """
        Write the pebble cells file
        """
        peb_type = pebble._pebble_type
        univ = pebble._universe
        if peb_type == 'graphite':
            f.write(f'cell pebble_{univ} {univ} matrix_{univ} -pebble_inner\n')
            f.write(f'cell shell_{univ} {univ} pebshell_{univ} pebble_inner -pebble_outer\n')
        else:
            f.write(f'cell pebble_{univ} {univ} fill triso_{univ} -pebble_inner\n')
            f.write(f'cell matrix_c{univ} matrix_u{univ} matrix_{univ} -inf_surf\n')
            f.write(f'cell pebble_{univ}_matrix {univ} pebshell_{univ} pebble_inner -pebble_outer\n')

    def create_pebble_detectors(self,pebble):
        """
        Create a material detector using the 'create_detector' function in sea_serpent
        """
        peb_type = pebble._pebble_type
        univ = pebble._universe
        if peb_type == 'fuel':
            self.create_detector(univ, particle_type='n', materials=[f'fuel_{univ}'], responses=['-8'], micro_xs=False)
        
    def write_detectors(self,f):
        """
        Write the detectors present in the detector dictionary
        """
        print("Writing detectors!!!")
        for det, values in self.user_detector_dict.items():
            f.write(f'%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n%%% User Detector {det}\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n')
            f.write(values['detector_str'] + '\n')
        print("Number of detectors: ", len(self._detector_dict))
        for det, values in self._detector_dict.items():
            f.write(f'%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n%%% Detector {det}\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n')
            f.write(values['detector_str'] + '\n')
    
    def write_energy_grids(self, f):
        """
        Write the energy grids present in the energy grid dictionary
        """
        for grid, values in self.energy_grid_dict.items():
            f.write(f'%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n%%% Energy Grid {grid}\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n')
            f.write(values['energy_grid_str'] + '\n')

                    
    def write_materials(self, f, pebble):
        """
        Write the materials for pebbles
        """
        u = pebble._universe
        num_pebbles = self.get_number_of_pebbles_in_volume(u) # Grab the number of fuel pebbles
        self.pebble_material_volume_data[u] = {'pebble_count': num_pebbles, 'burnup': [], 'power': []}

        for mat, mat_dict in pebble._material.items():
            volume = round(num_pebbles * pebble._geometry[mat]['volume'], 5) # grab the volume of the component and multpiply this by the number of pebbles to get the total volume
            if 'fuel' in mat:
                f.write(f'mat {mat}_{u} sum tmp {pebble._fuel_temperature} vol {volume} burn 1\n')
            elif mat in ['inner_pyc', 'outer_pyc', 'pebshell']:
                f.write(f'mat {mat}_{u} sum tmp {pebble._temperature} vol {volume} moder {pebble._scattering_library} 6000\n')               
            else:
                f.write(f'mat {mat}_{u} sum tmp {pebble._temperature} vol {volume}\n')
                
            self.pebble_material_volume_data[u][mat] = {'volume': volume, 'atom_densities': mat_dict}
            for elem, atom_den in mat_dict.items():
                if 'volume' not in elem:
                    if 'fuel' in mat:
                        f.write(f'  {elem}.{pebble._xs_fuel_library}      {atom_den:e}\n')
                    else:
                        f.write(f'  {elem}.{pebble._xs_library}      {atom_den:e}\n')       

    def write_pebble_data(self):
        """
        Write down the pebble data
        """            
        self._detector_dict = {}
        pebble_surface_input = os.path.join(self.output_dir,self.pebble_surface_file)
        pebble_material_input = os.path.join(self.output_dir,self.pebble_material_file)
        pebble_cell_input = os.path.join(self.output_dir,self.pebble_cell_file)
        detector_input = os.path.join(self.output_dir,self.detector_file)
        self.pebble_material_volume_data = {}

        f1 = open(pebble_surface_input, 'w')
        f1.write('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n%%% Pebble Surfaces\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n')
        f2 = open(pebble_material_input, 'w')
        f2.write('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n%%% Pebble Materials\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n')
        f3 = open(pebble_cell_input, 'w')
        f3.write('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n%%% Pebble Cells\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n')
        f4 = open(detector_input, 'w')
        f4.write('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n%%% Pebble Detectors\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n')
        pebble_list = []
        pebble_number = 1
        for channel_num, channel in enumerate(self._pebble_array):
            for volume_num, volume in enumerate(channel):
                self.write_region_header(f1, channel_num, volume_num)
                self.write_region_header(f2, channel_num, volume_num)
                self.write_region_header(f3, channel_num, volume_num)
                for peb_pos, pebble in enumerate(volume):
                    u = pebble._universe
                    peb_type = pebble._pebble_type
                    if u not in pebble_list:
                        if peb_type == 'fuel':
                            self.write_surfaces(f1, pebble, pebble_number)
                            pebble_number += 1
                        self.write_materials(f2, pebble)
                        self.write_cells(f3, pebble)
                        self.create_pebble_detectors(pebble)
                        pebble_list.append(u)
                    if peb_type == 'fuel' and self.multiphysics_run:
                        #self.pebble_material_volume_data[u]['burnup'].append(pebble._burnup)
                        #self.pebble_material_volume_data[u]['power'].append(pebble._power_density) # power density is power / pebble
                        self.pebble_material_volume_data[u]['burnup'].append(pebble._burnup_j_cm3)
        
        self.write_energy_grids(f4)    
        self.write_detectors(f4)
        f1.close()
        f2.close()
        f3.close()        
        f4.close()
        if self.multiphysics_run:
            with open(os.path.join(self.output_dir, 'pebble_dictionary.json'), 'w') as file:
                # Write the dictionary to the file
                json.dump(self.pebble_material_volume_data, file)         

    def write_pebble_location_file(self):
        """
        Write the pbed file based on the pebble array
        """

        pebble_input_path = os.path.join(self.output_dir,self._step_pebble_distribution_file)

        f = open(pebble_input_path, 'w')
        for channel_num, channel in enumerate(self._pebble_array):
            for volume_num, volume in enumerate(channel):
                for peb_pos, pebble in enumerate(volume):
                    x, y, z, radius, univ = pebble._x, pebble._y, pebble._z, pebble._radius, pebble._universe
                    f.write(f'{x:<10} {y:<10} {z:<10} {radius:<5} {univ:<31}\n')
        f.close()
        
    def write_region_header(self, f, channel, volume):
        """
        Header for each region to separate channels and zones
        """
        f.write(f'\n% Pebbles for Channel: {channel}, Volume Zone: {volume} \n\n')

    def write_serpent_input(self):
        """
        Write the base serpent input file.
        """

        serpent_input_path = os.path.join(self.output_dir,self.reactor_file_name)
        f = open(serpent_input_path, 'w')

        f.write('% Created by pebble_sorter found at: https://github.inl.gov/reactor-multiphysics/pyrates\n% Contact a member of the Griffin team for access.\n\n')
        for file_name in [self.pebble_surface_file, self.pebble_material_file, self.pebble_cell_file, self.pbr_core.core_file_name, self.detector_file, 'materials.inp']:
            f.write(f'include {file_name}\n')

#        f.write('ene htrpm_26_group 1 1.0E-11\n 1.0000E-08\n 2.0000E-08\n 5.0000E-08\n 8.0000E-08\n 1.3000E-07\n 2.0000E-07\n 3.5000E-07\n 8.2500E-07\n 1.2750E-06\n 2.3800E-06\n 3.9300E-06\n 8.3200E-06\n 1.7600E-05\n 2.9000E-05\n 6.1440E-05\n 1.3010E-04\n 2.7540E-04\n 9.6100E-04\n 1.5850E-03\n 3.3550E-03\n 1.9300E-02\n 1.8300E-01\n 6.7200E-01\n 3.6800E+00\n 7.4100E+00\n 1.4900E+01\n\n')
        f.write('ene htrpm_9_group 1 1e-11\n 1.37999E-07\n 8.20037E-07\n 1.29304E-06\n 2.33006E-06\n 3.88217E-06\n 1.75648E-05\n 0.000907501\n 0.195007703\n 19.6403\n\n')
        f.write(f'set seed {self.random_seed}\n')
#        f.write('det core_mesh n de htrpm_26_group dn 1 0.0 120.0 5 0.0 360.0 1 0.0 893.0 12\n') # This mesh aligns with the Griffin mesh
        f.write('det core_mesh_9grp n de htrpm_9_group dn 1 0.0 120.0 5 0.0 360.0 1 0.0 893.0 12\n') # This mesh aligns with the Griffin mesh
        f.write('det griffin_flux_mesh n dn 1 0.0 120.0 5 0.0 360.0 1 0.0 893.0 12\n') # This mesh aligns with the Griffin mesh with a single energy group
        if not self.simple_core:
            f.write('det cons_flux n du cone_u\n')
#        f.write('det quarter_core_mesh n de htrpm_26_group dn 1 0.0 120.0 1 0.0 360.0 1 0.0 893.0 4\n')
#        f.write('det total_core_mesh n de htrpm_26_group dn 1 0.0 120.0 1 0.0 360.0 1 0.0 893.0 1\n\n')
        f.write('% Data option and run information\n\n')
        f.write('% Geometry and output plotters\n')
        f.write('%plot 12 500  500\n%plot 31 500  500 1050\nmesh 1 500 1000\n\n')
        f.write('plot 22 1000  1500\n\n')
        for plot in self.geom_plots:
           f.write(f'plot {str(plot["type"])} {plot["xpix"]} {plot["ypix"]} {plot["pos"] if plot["pos"] else ""} {plot["min1"] if plot["min1"] else ""} {plot["max1"] if plot["max1"] else ""} {plot["min2"] if plot["min2"] else ""} {plot["max2"] if plot["max2"] else ""}\n')
        f.write('set acelib "/hpc-common/data/serpent/xsdata/endfb71_edep/endfb71_edep.xsdata"\n')
        f.write('set declib "/hpc-common/data/serpent/xsdata/sss_endfb7.dec"\n')
        f.write('set nfylib "/hpc-common/data/serpent/xsdata/sss_endfb7.nfy"\n\n')
        f.write('% Thermal scattering data\n\ntherm grph300 300 grph.03t grph.04t\ntherm grph600 600 grph.05t grph.06t\ntherm grph900 900 grph.08t grph.10t\ntherm grph1200 1200 grph.10t grph.12t')
        f.write('% Run Data\n')
        f.write(f'set pop {self.num_particles} {self.num_generations} {self.skipped_generations} 1.05\n')
        f.write(f'set power {self.power_level}\n')
        f.write(f'set nbuf {self.nbuf}\n')
        f.write('set opti 1\nset pcc 0\nset printm yes\nset depout 3\n')
        depletion_steps = self.temp_depletion_steps if self.refine_burnstep else self.depletion_steps
        dep = f'dep daystep ' + ' '.join([str(x) for x in depletion_steps]) if depletion_steps != [] else ''
        f.write(dep)
        f.close()

    def write_materials_file(self):
        file_path = os.path.join(self.output_dir, 'materials.inp')
        with open(file_path, 'w') as f:
            for material, mat_dict in self.core_materials.items():
                xs, scat = self.set_xs_set(mat_dict['temperature'])
                scat = '' if mat_dict["moder"] == '' else scat
                f.write(f'%%%%%% {material} %%%%%%\n\n')
                f.write(f'mat {material} sum tmp {mat_dict["temperature"]} {mat_dict["moder"]} {scat} {mat_dict["moder_nuclide"]}\n')
                for isotope, atom_density in mat_dict['nuclides'].items():
                    f.write(f'  {isotope}.{xs} {atom_density}\n')
                f.write('\n')
        
    def write_serpent_pbs(self):
        """
        If we are not running in a single run, create the PBS file for submission.
        """
        file_path = os.path.join(self.output_dir, 'serpent.pbs')
        
        with open(file_path, 'w') as f:
            f.write('#!/bin/bash\n')
            f.write('#PBS -l select=12:ncpus=48:mpiprocs=1\n')
            f.write('#PBS -N shuf\n')
            f.write('#PBS -l walltime=01:00:00\n')
            f.write('#PBS -ko\n#PBS -j oe\n#PBS -P neams\n#PBS -l software=Serpent\n#PBS -m abe\n#\n')
            f.write('cat $PBS_NODEFILE\n#\nsource /etc/profile.d/modules.sh\nmodule load use.exp_ctl\nmodule load serpent/2.1.32-intel-19.0\n#\ncd $PBS_O_WORKDIR\n#\n')
            f.write(r'JOB_NUM=${PBS_JOBID%\.*}\nif [ $PBS_O_WORKDIR != $HOME ]\nthen\nln -s $HOME/$PBS_JOBNAME.o$JOB_NUM $PBS_JOBNAME.o$JOB_NUM\nfi\n#\nexport TMPDIR=/tmp\n#\n')
            if self.nofatal:
                f.write(f'mpiexec sss2 {self.reactor_file_name} -nofatal -omp {self.num_threads}\n')
            else:
                f.write(f'mpiexec sss2 {self.reactor_file_name} -omp {self.num_threads}\n')
            f.write('if [ $PBS_O_WORKDIR != $HOME ]\nthen\nrm $PBS_O_WORKDIR/$PBS_JOBNAME.o$JOB_NUM\nmv $HOME/$PBS_JOBNAME.o$JOB_NUM $PBS_O_WORKDIR/$PBS_JOBNAME.o$JOB_NUM\nfi')      
        
    def write_surfaces(self, f, pebble, pebble_num):
        """
        Write the pebble surfaces file
        """
        f.write(f'particle {pebble_num}\n')
        for surf, radius in pebble._kernel_data.items():
            f.write(f'{surf}_{pebble._universe} {radius}\n')
        f.write(f'matrix_{pebble._universe}\n')
        f.write(f'pbed triso_{pebble._universe} matrix_u{pebble._universe} "triso/triso_dist_u{pebble_num}.triso"\n\n')
        self.write_triso_file(pebble_num)

    def write_triso_file(self, pebble_num):
        """
        For each unique particle type, we need a TRISO particle file, we copy a tempmlate file
        and place this in a unique directory for reference
        """
        triso_path = os.path.join(self.output_dir, 'triso')
        if not os.path.isdir(triso_path):
            os.mkdir(triso_path)
        data_triso = os.path.join(self._path_to_data_files, self.triso_dist_name)
        run_triso = os.path.join(self.output_dir, 'triso', self.triso_dist_name)

        shutil.copy(data_triso, run_triso)
        with open(run_triso) as f:
            txt = f.read().replace('triso', str(pebble_num))

        run_triso_pebble_num = os.path.join(self.output_dir, 'triso', f'triso_dist_u{pebble_num}.triso')        
        with open(run_triso_pebble_num, 'w') as f:
            f.write(txt)
