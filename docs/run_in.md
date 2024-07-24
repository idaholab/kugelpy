Copyright 2024, Battelle Energy Alliance, LLC, ALL RIGHTS RESERVED
# `kugelpy`

`kugelpy` is a python module that performs time-dependent high-temperature gas-cooled pebble bed reactor (PBR) analysis. 
This process can simulate the run-in procedure for a PBR along with equilibrium analysis. 
The following notebook will describe how to create a `kugelpy` input and how to load previous `kugelpy` simulations to restart or examine the state of the reactor.

## Basic python input for run-in scenario

`kugelpy` is run using a pbs script, see [here](./pbr_runin.pbs). 
Typically the script should be run on a high performance computing cluster (HPC), as the simulations are computationally expensive (reasonable results have been shown between 30-40 nodes with 48 processors each).
The python script has been annotated to provide clarity for the input script.

```python
import pyrates.kugelpy.pebble_sorter as psp
from os import path

# set paths for where the data files are in addition to there output directory should
module_path = path.dirname(path.realpath(psp.__file__))
main_dir = path.dirname(path.realpath(__file__))
output_dir = path.join(main_dir, 'examples', 'ri_test')
pebble_dist_path = path.join(module_path, 'data', 'rawdist.inp')

# chcurves creates the streamlines which are used to separate pebbles into radial and axial regions (denoted as axial zones)
# this inputs consists of 5 streamlines, and thus requires 6 inputs for chcurves
# each entry consists of a 2xN matrix, where the first array contains the fuel heights and the second array contains the radial positions
# the first matrix is radially positioned at the center of the core, and the last matrix is radially positioned at the core/reflector interface
# we note that there is both an upper and lower conus in this simulation
chcurvs = [[[1126.49, 1099.74, 1072.99, 1046.23, 1019.48, 992.73, 965.98, 939.22, 912.47, 885.72, 858.96, 832.21, 805.46, 778.71, 751.95, 725.2, 698.45, 671.69, 644.94, 618.19, 591.44, 564.68, 537.93, 511.18, 484.42, 457.67, 430.92, 404.17, 377.41, 350.66, 340.31, 329.97, 319.62, 309.27, 298.92, 288.57, 278.23, 267.88, 257.53, 247.19, 236.84, 226.49, 216.14, 205.79, 195.45, 185.1],
      [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],
[[1126.49, 1099.74, 1072.99, 1046.23, 1019.48, 992.73, 965.98, 939.22, 912.47, 885.72, 858.96, 832.21, 805.46, 778.71, 751.95, 725.2, 698.45, 671.69, 644.94, 618.19, 591.44, 564.68, 537.93, 511.18, 484.42, 457.67, 430.92, 404.17, 377.41, 350.66, 340.31, 329.97, 319.62, 309.27, 298.92, 288.57, 278.23, 267.88, 257.53, 247.19, 236.84, 226.49, 216.14, 205.79, 195.45, 185.1],
      [44.211, 44.211, 44.211, 44.211, 44.211, 44.20345, 44.18431, 44.15973, 44.12076, 44.05477, 43.96634, 43.86105, 43.74685, 43.62336, 43.49642, 43.37785, 43.26327, 43.14269, 43.02477, 42.89514, 42.77098, 42.64801, 42.53059, 42.41545, 42.31044, 42.21782, 42.14349, 42.05958, 41.92575, 41.63257, 41.42335, 41.12016, 40.68085, 40.05544, 39.098, 37.47593, 34.54502, 30.21314, 25.3088, 20.6561, 16.72857, 13.54777, 10.99466, 9.14798, 8.12596, 8.19874]],
[[1126.49, 1099.74, 1072.99, 1046.23, 1019.48, 992.73, 965.98, 939.22, 912.47, 885.72, 858.96, 832.21, 805.46, 778.71, 751.95, 725.2, 698.45, 671.69, 644.94, 618.19, 591.44, 564.68, 537.93, 511.18, 484.42, 457.67, 430.92, 404.17, 377.41, 350.66, 340.31, 329.97, 319.62, 309.27, 298.92, 288.57, 278.23, 267.88, 257.53, 247.19, 236.84, 226.49, 216.14, 205.79, 195.45, 185.1],
      [82.105, 82.105, 82.105, 82.105, 82.105, 82.087, 82.02266, 81.9622, 81.89196, 81.77948, 81.66513, 81.53734, 81.40771, 81.26746, 81.10857, 80.96155, 80.81659, 80.67267, 80.53068, 80.38331, 80.23166, 80.08721, 79.94035, 79.79063, 79.63851, 79.48877, 79.35236, 79.20133, 79.01734, 78.70429, 78.51402, 78.25401, 77.89377, 77.39389, 76.66375, 75.52775, 73.41357, 69.3007, 61.96307, 52.28305, 42.07782, 33.06554, 25.70736, 20.15169, 16.61293, 16.09318]],
[[1126.49, 1099.74, 1072.99, 1046.23, 1019.48, 992.73, 965.98, 939.22, 912.47, 885.72, 858.96, 832.21, 805.46, 778.71, 751.95, 725.2, 698.45, 671.69, 644.94, 618.19, 591.44, 564.68, 537.93, 511.18, 484.42, 457.67, 430.92, 404.17, 377.41, 350.66, 340.31, 329.97, 319.62, 309.27, 298.92, 288.57, 278.23, 267.88, 257.53, 247.19, 236.84, 226.49, 216.14, 205.79, 195.45, 185.1],
      [94.737, 94.737, 94.737, 94.737, 94.737, 94.71306, 94.62775, 94.59489, 94.557, 94.44693, 94.3595, 94.30034, 94.2407, 94.13986, 94.03026, 93.9561, 93.87629, 93.78233, 93.68947, 93.60143, 93.53932, 93.43703, 93.33228, 93.23621, 93.14022, 93.0316, 92.93193, 92.82167, 92.71202, 92.47871, 92.32607, 92.1331, 91.8812, 91.51028, 90.98523, 90.22885, 89.00353, 86.55365, 81.18153, 71.71382, 59.76636, 47.45436, 36.29467, 27.19942, 20.96119, 19.2266]],
[[1126.49, 1099.74, 1072.99, 1046.23, 1019.48, 992.73, 965.98, 939.22, 912.47, 885.72, 858.96, 832.21, 805.46, 778.71, 751.95, 725.2, 698.45, 671.69, 644.94, 618.19, 591.44, 564.68, 537.93, 511.18, 484.42, 457.67, 430.92, 404.17, 377.41, 350.66, 340.31, 329.97, 319.62, 309.27, 298.92, 288.57, 278.23, 267.88, 257.53, 247.19, 236.84, 226.49, 216.14, 205.79, 195.45, 185.1],
      [107.37, 107.37, 107.37, 107.37, 107.37, 107.33419, 107.34077, 107.49045, 107.47701, 107.29504, 107.22586, 107.36764, 107.36501, 107.19078, 107.09066, 107.22299, 107.23292, 107.10503, 106.95589, 107.00479, 107.12655, 107.02795, 106.86841, 106.87822, 106.94322, 106.86412, 106.69916, 106.63512, 106.7939, 106.66, 106.5303, 106.29289, 106.27, 106.137, 105.71554, 105.34689, 104.9322, 104.011, 102.05009, 96.23443, 83.67145, 69.222, 54.54269, 40.42161, 28.33431, 22.96025]],
[[1126.49, 1099.74, 1072.99, 1046.23, 1019.48, 992.73, 965.98, 939.22, 912.47, 885.72, 858.96, 832.21, 805.46, 778.71, 751.95, 725.2, 698.45, 671.69, 644.94, 618.19, 591.44, 564.68, 537.93, 511.18, 484.42, 457.67, 430.92, 404.17, 377.41, 350.66, 340.31, 329.97, 319.62, 309.27, 298.92, 288.57, 278.23, 267.88, 257.53, 247.19, 236.84, 226.49, 216.14, 205.79, 195.45, 185.1],
      [120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 112.69338, 95.3547, 78.01603, 60.67735, 43.33868, 26.0]],]

# chcurves defines the radial streamlines, where trgtchnv defines how many axial zones are requested for each channel
# for this this simulation channels 1,2,3 contains 14 axial zones, channel 4 contains 15 axial zones, and channel 5 contains 18 axial zones
# the number of axial zones per channel should be used to determine the speed at which pebbles move in each region
# in this case pebbles in channel 5 move about 20% slower than pebbles in channel 1
# these results are based off of "Discrete Element Simulation of Pebble Bed Reactors on Graphics Processing Units" by David Reger et al.
trgtchnv = [14, 14, 14, 15, 18]

# pebble materials are described by a dictionary where the key is the ZAID number and the value is the atom density
# here we define the startup fuel with 5 w/o U-235 in UCO, equilibrium fuel is 15.6 w/o U-235 in UCO
run_in_fuel={'92235': 1.19404E-03, '92238': 2.24002E-02,  '8016': 3.36925E-02,  '6000': 9.14997E-03 + 9.89636E-05,  '5010': 1.86866E-08,  '5011': 7.56902E-08}
equilibrium_fuel_material = {'92235': 3.701063E-3, '92238': 1.992191E-2, '8016': 3.37336E-2, '6000': 9.260240E-3, '5010': 1.87091E-8, '5011': 7.57813E-8}

# to facilitate a smooth approach to equilibrium (assuming a 6 pass core) we need to remove approximately 1/6 of startup fuel each time it reaches the discharge chute
# to do this, we artificially assign startup fuel with a pass number between 0 and 5
# this ensures that startup fuel is continually removed to make way for equilibrium fuel
eq_mats = {}
for channel_num, volumes in enumerate(trgtchnv):
    for volume_num in range(volumes):
        eq_mats[f'c{channel_num}v{volume_num}'] = [(run_in_fuel, n) for n in range(0,6)]

# the PebbleSorter class houses the functionality to perform a run-in analysis
# the keyword args listed below show some of the functionality to manipulate the process
ps = psp.PebbleSorter(graphite_height=450.0, # run-in simulation: the initial height of the graphite fuel (measured from the bottom)
                      graphite_fraction=0.42, # run-in simulation: the initial fraction of graphite pebbles mixed with fuel pebbles
                      power_level=1E+6, # the power level of the reactor (W)
                      output_dir=output_dir, # directory where outputs should be placed
                      fuel_material=run_in_fuel, # dictionary of the fuel isotopics for the fuel which will be initially used
                      steps=200, # desired number of time steps steps to take 
                      day_limit = 3000, # desired number of days to run to simulation to
                      pass_limit=6, # number of passes required before pebbles are discharged
                      burnup_limit = 1000.0, # burnup limit allowed before pebbles are discharged
                      depletion_steps = [5,5], # list of ints/floats denoting how many days each serpent run will deplete (this depletes a total of 10 days, in two 5 day increments resulting in 3 serpent calculations)
                      keep_files = True, # flag to keep all associated input/output files
                      num_particles=20000, # number of particles in Serpent calculation
                      num_generations=200, # number of generations in Serpent calculation
                      num_skipped_generations=40, # number of skipped generations in Serpent calculation
                      core_inlet_temperature=500.0, # temperature of core inlet, can be used to create temperature profile
                      core_outlet_temperature=500.0, # temperature of the core outlet, can be used to create temperature profile
                      fuel_temperature=500.0, # temperature of the fuel kernels
                      pebble_temperature=500.0, # temperature of the graphite matrix for the fuel pebbles
                      final_pass_limit=6, # pass limit for equilibrium fuel
                      final_homogenization_group=1, # denotion of fuel type for equilibrium fuel, start up fuel is denoted as 0
                      equilibrium_core = True, # this is used to create a core with pebbles that can be assigned to each axial zone, allowing for jump-in to equilibrium calculation or for startup fuel to artificially be given a pass number
                      equilibrium_materials = eq_mats, # materials to be assigned to each axial zone as required if equilibrium_core=True
                      automatic_fuel_transition = True, # automitically transitions from startup fuel to equilibrium fuel once the fraction of graphite pebbles is less than 3% of the entire core
                      equilibrium_fuel_material = equilibrium_fuel_material, # dictionary of the equilibrium fuel
                      cr_insertion_depth = 100, # rough depth from the top of the upper conus to insert the control rods into the core
                      allowable_keff=1.004, # allowable keff to determine when to stop the simulation
                     ) 

# create_energy_grid method creates an energy grid which can be applied to a detector and store it in a dictionary
# the following energy grid will include 20 bins of equal energy spanning from 0.0eV to 1.36eV. This grid will be named 'thermal_energy_grid' which will then be passed to a detector
ps.create_energy_grid(name = 'thermal_energy_grid', # user-given name of energy grid
                      type = 2, # Serpent energy grid type
                      boundaries = [20, 0.0, 1.36E-6], # grid parameters/boundaries depend on the type of grid
                      )

# create_user_detector method creates a detector defined by the user and stores it in a dictionary
# the following detector will count and bin thermal neutrons by energy and radial position. Note, the resulting flux measurements will not be volume-normalized
ps.create_user_detector(name='thermal_neutron_flux', # name of detector, used in output file
                        particle_type='n', # particle type, by default it is 'n'=neutrons
                        energy_bins='thermal_energy_grid', # name of energy grid previously defined
                        cylindrical_variation={'r':[0, 120, 10], 'theta':[0, 360, 1], 'z':[-240.538, 1024.8, 1]}, # cylindrical mesh. Single regions in the azimuthal and axial directions, 10 divisions in the radial direction
                        )

# assign_pebble_dist_variables method creates the geometry necessary for the PBR
# pbcyll is the height of the core (excluding the lower conus) - note that the height of the core is measured from the bottom of the core (top of the conus)
# pblwcon is the height of the lower conus
# pbupconl is the height of the upper conus, the upper conus can also be created by increasing pbcyll if the pebble distribution already includes the upper conus
# pbr is the radius of the pebble bed, typically this is set to larger than the actual radius to prevent cutting pebbles, but can be used to shrink the radius if necessary
# dcr is the radius of the lower conus
# axial_offset is used to shift pebbles in the distribution file
# idistrfile is the file path for the pebble locations in the core, this can be obtained via DEM calculations or serpent's built in method
# odistrfile is the output distribution file path
# chcurves describes how the streamlines curve through the core
# trgtchnv is the number of axial zones for each streamlines
ps.assign_pebble_dist_variables(pbcyll=893, pblwconl=55.438, pbupconl=54.0, pbr=120.0,
                       dcr=26.0, axial_offset=-235.538, idistrfile=pebble_dist_path,
                       odistrfile='findist.txt', chcurvs=chcurvs,
                       log=None, trgtchnv=trgtchnv)
# we can set the random number in an attempt to minimize differences in runs
ps.set_random_seed(1)

# perform the run in (or equilibrium) calculation
ps.perform_run_in()
```

Once the input file has been generated, it is advised to create a PBR script to submit the job to the HPC. 
Depending on the number of steps, fidelity of the simulation, etc. a reload may be required to finish the simulation. 
The following script shows how to restart a simulation based on the pickled save point.

```python
import pyrates.kugelpy.pebble_sorter as psp

# utilize the loader function to read the pickle file placed in the 
# provide the path to the pickle file and the step (this ensure we grab the correct file)
ps = psp.PebbleSorter.loader('./examples/ri_base_final/step_130/',130)

# provide the step from which to restart the calculation
# note we save the file before we perform any shuffling, so we rerun the calculation at this time step
# during this time any additional variables can be set if we want to branch off from the original calculation
# i.e. we can move control rods, change fuel characteristics, etc.
ps.load_step=130
# Perform the run-in
ps.perform_run_in()
```

### Analysis

Following a successful PBR simulation(s) the resulting output files can be analyzed, along with a csv file containing a majority of important information. 
This csv file can be found in the base directory for the simulation.

## Basic python input for run-in scenario

`kugelpy` is run using a pbs script, see [here](./pbr_runin.pbs). 
Typically the script should be run on a high performance computing cluster (HPC), as the simulations are computationally expensive (reasonable results have been shown between 30-40 nodes with 48 processors each).
The python script has been annotated to provide clarity for the input script.

```python
import pyrates.kugelpy.pebble_sorter as psp
from os import path

# set paths for where the data files are in addition to there output directory should
module_path = path.dirname(path.realpath(psp.__file__))
main_dir = path.dirname(path.realpath(__file__))
output_dir = path.join(main_dir, 'examples', 'ri_test')
pebble_dist_path = path.join(module_path, 'data', 'rawdist.inp')
# step_creator is a function which allows you to determine the time-dependent changes in the PBR
# this examples allows us update the fuel temperature, pebble temperature, inlet temperature, outlet temperature
# along with the power, graphite fraction and the time spacing for each time step
# this will create a run-in scenario which takes roughly 1 year to compelete
# note that steps takes the form of a nested dictionary the first key is the day in which to implement the dictionary stored as the value
# the value is a dictionary containing attributes of the pebble_sorter class that should be updated at each time step
def step_creator(min_fuel_temp = 500, max_fuel_temp = 1025, 
                min_pebble_temp = 500, max_pebble_temp = 1025, 
                min_outlet_temp = 500, max_outlet_temp = 1100, 
                min_power = 1, max_power = 200, 
                max_graphite_fraction = 0.42, total_steps_1 = 67, 
                day_step = 5, total_graphite_steps = 7, graphite_day_step = 10):
    graphite_step = 1

    steps = {0: {'power_level': 1}}
    days = 0
    for step in range(0,total_steps_1+1):
        days = day_step * step + 30 if steps[days]['power_level'] > 100E+6 else day_step * step # Around a power level of 125 MW, provide a 30 day period to stabalize power before increasing again 
        steps[days] = {'power_level': round(((max_power - min_power) * step / total_steps_1 + min_power) * 1E+6),
                       'fuel_temperature': round((max_fuel_temp - min_fuel_temp) * step / total_steps_1 + min_fuel_temp),
                       'pebble_temperature': round((max_pebble_temp - min_pebble_temp) * step / total_steps_1 + min_pebble_temp),
                       'core_inlet_temperature': round((max_fuel_temp - min_fuel_temp) * step / total_steps_1 + min_fuel_temp), # reflector temperature follows the fuel temperature
                       'core_outlet_temperature': round((max_outlet_temp - min_outlet_temp) * step / total_steps_1 + min_outlet_temp),}
        if  days % graphite_day_step  == 0 and graphite_step < total_graphite_steps+1:
            steps[days].update({'graphite_fraction':  round(max_graphite_fraction - max_graphite_fraction * graphite_step / total_graphite_steps,2),
                                'depletion_steps': [5,5,5]})              
            graphite_step += 1 
            if graphite_step == total_graphite_steps+1:
                  steps[days].update({'depletion_steps': [5,5,2.5,2.5,2.5,2.5]})    
    steps[360].update({'depletion_steps': [10,2.5,2.5,2.5,2.5]})
    return steps

steps = step_creator()

# chcurves creates the streamlines which are used to separate pebbles into radial and axial regions (denoted as axial zones)
# this inputs consists of 5 streamlines, and thus requires 6 inputs for chcurves
# each entry consists of a 2xN matrix, where the first array contains the fuel heights and the second array contains the radial positions
# the first matrix is radially positioned at the center of the core, and the last matrix is radially positioned at the core/reflector interface
# we note that there is both an upper and lower conus in this simulation
chcurvs = [[[1126.49, 1099.74, 1072.99, 1046.23, 1019.48, 992.73, 965.98, 939.22, 912.47, 885.72, 858.96, 832.21, 805.46, 778.71, 751.95, 725.2, 698.45, 671.69, 644.94, 618.19, 591.44, 564.68, 537.93, 511.18, 484.42, 457.67, 430.92, 404.17, 377.41, 350.66, 340.31, 329.97, 319.62, 309.27, 298.92, 288.57, 278.23, 267.88, 257.53, 247.19, 236.84, 226.49, 216.14, 205.79, 195.45, 185.1],
      [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],
[[1126.49, 1099.74, 1072.99, 1046.23, 1019.48, 992.73, 965.98, 939.22, 912.47, 885.72, 858.96, 832.21, 805.46, 778.71, 751.95, 725.2, 698.45, 671.69, 644.94, 618.19, 591.44, 564.68, 537.93, 511.18, 484.42, 457.67, 430.92, 404.17, 377.41, 350.66, 340.31, 329.97, 319.62, 309.27, 298.92, 288.57, 278.23, 267.88, 257.53, 247.19, 236.84, 226.49, 216.14, 205.79, 195.45, 185.1],
      [44.211, 44.211, 44.211, 44.211, 44.211, 44.20345, 44.18431, 44.15973, 44.12076, 44.05477, 43.96634, 43.86105, 43.74685, 43.62336, 43.49642, 43.37785, 43.26327, 43.14269, 43.02477, 42.89514, 42.77098, 42.64801, 42.53059, 42.41545, 42.31044, 42.21782, 42.14349, 42.05958, 41.92575, 41.63257, 41.42335, 41.12016, 40.68085, 40.05544, 39.098, 37.47593, 34.54502, 30.21314, 25.3088, 20.6561, 16.72857, 13.54777, 10.99466, 9.14798, 8.12596, 8.19874]],
[[1126.49, 1099.74, 1072.99, 1046.23, 1019.48, 992.73, 965.98, 939.22, 912.47, 885.72, 858.96, 832.21, 805.46, 778.71, 751.95, 725.2, 698.45, 671.69, 644.94, 618.19, 591.44, 564.68, 537.93, 511.18, 484.42, 457.67, 430.92, 404.17, 377.41, 350.66, 340.31, 329.97, 319.62, 309.27, 298.92, 288.57, 278.23, 267.88, 257.53, 247.19, 236.84, 226.49, 216.14, 205.79, 195.45, 185.1],
      [82.105, 82.105, 82.105, 82.105, 82.105, 82.087, 82.02266, 81.9622, 81.89196, 81.77948, 81.66513, 81.53734, 81.40771, 81.26746, 81.10857, 80.96155, 80.81659, 80.67267, 80.53068, 80.38331, 80.23166, 80.08721, 79.94035, 79.79063, 79.63851, 79.48877, 79.35236, 79.20133, 79.01734, 78.70429, 78.51402, 78.25401, 77.89377, 77.39389, 76.66375, 75.52775, 73.41357, 69.3007, 61.96307, 52.28305, 42.07782, 33.06554, 25.70736, 20.15169, 16.61293, 16.09318]],
[[1126.49, 1099.74, 1072.99, 1046.23, 1019.48, 992.73, 965.98, 939.22, 912.47, 885.72, 858.96, 832.21, 805.46, 778.71, 751.95, 725.2, 698.45, 671.69, 644.94, 618.19, 591.44, 564.68, 537.93, 511.18, 484.42, 457.67, 430.92, 404.17, 377.41, 350.66, 340.31, 329.97, 319.62, 309.27, 298.92, 288.57, 278.23, 267.88, 257.53, 247.19, 236.84, 226.49, 216.14, 205.79, 195.45, 185.1],
      [94.737, 94.737, 94.737, 94.737, 94.737, 94.71306, 94.62775, 94.59489, 94.557, 94.44693, 94.3595, 94.30034, 94.2407, 94.13986, 94.03026, 93.9561, 93.87629, 93.78233, 93.68947, 93.60143, 93.53932, 93.43703, 93.33228, 93.23621, 93.14022, 93.0316, 92.93193, 92.82167, 92.71202, 92.47871, 92.32607, 92.1331, 91.8812, 91.51028, 90.98523, 90.22885, 89.00353, 86.55365, 81.18153, 71.71382, 59.76636, 47.45436, 36.29467, 27.19942, 20.96119, 19.2266]],
[[1126.49, 1099.74, 1072.99, 1046.23, 1019.48, 992.73, 965.98, 939.22, 912.47, 885.72, 858.96, 832.21, 805.46, 778.71, 751.95, 725.2, 698.45, 671.69, 644.94, 618.19, 591.44, 564.68, 537.93, 511.18, 484.42, 457.67, 430.92, 404.17, 377.41, 350.66, 340.31, 329.97, 319.62, 309.27, 298.92, 288.57, 278.23, 267.88, 257.53, 247.19, 236.84, 226.49, 216.14, 205.79, 195.45, 185.1],
      [107.37, 107.37, 107.37, 107.37, 107.37, 107.33419, 107.34077, 107.49045, 107.47701, 107.29504, 107.22586, 107.36764, 107.36501, 107.19078, 107.09066, 107.22299, 107.23292, 107.10503, 106.95589, 107.00479, 107.12655, 107.02795, 106.86841, 106.87822, 106.94322, 106.86412, 106.69916, 106.63512, 106.7939, 106.66, 106.5303, 106.29289, 106.27, 106.137, 105.71554, 105.34689, 104.9322, 104.011, 102.05009, 96.23443, 83.67145, 69.222, 54.54269, 40.42161, 28.33431, 22.96025]],
[[1126.49, 1099.74, 1072.99, 1046.23, 1019.48, 992.73, 965.98, 939.22, 912.47, 885.72, 858.96, 832.21, 805.46, 778.71, 751.95, 725.2, 698.45, 671.69, 644.94, 618.19, 591.44, 564.68, 537.93, 511.18, 484.42, 457.67, 430.92, 404.17, 377.41, 350.66, 340.31, 329.97, 319.62, 309.27, 298.92, 288.57, 278.23, 267.88, 257.53, 247.19, 236.84, 226.49, 216.14, 205.79, 195.45, 185.1],
      [120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 112.69338, 95.3547, 78.01603, 60.67735, 43.33868, 26.0]],]

# chcurves defines the radial streamlines, where trgtchnv defines how many axial zones are requested for each channel
# for this this simulation channels 1,2,3 contains 14 axial zones, channel 4 contains 15 axial zones, and channel 5 contains 18 axial zones
# the number of axial zones per channel should be used to determine the speed at which pebbles move in each region
# in this case pebbles in channel 5 move about 20% slower than pebbles in channel 1
# these results are based off of "Discrete Element Simulation of Pebble Bed Reactors on Graphics Processing Units" by David Reger et al.
trgtchnv = [14, 14, 14, 15, 18]

# pebble materials are described by a dictionary where the key is the ZAID number and the value is the atom density
# here we define the startup fuel with 5 w/o U-235 in UCO, equilibrium fuel is 15.6 w/o U-235 in UCO
run_in_fuel={'92235': 1.19404E-03, '92238': 2.24002E-02,  '8016': 3.36925E-02,  '6000': 9.14997E-03 + 9.89636E-05,  '5010': 1.86866E-08,  '5011': 7.56902E-08}
equilibrium_fuel_material = {'92235': 3.701063E-3, '92238': 1.992191E-2, '8016': 3.37336E-2, '6000': 9.260240E-3, '5010': 1.87091E-8, '5011': 7.57813E-8}

# to facilitate a smooth approach to equilibrium (assuming a 6 pass core) we need to remove approximately 1/6 of startup fuel each time it reaches the discharge chute
# to do this, we artificially assign startup fuel with a pass number between 0 and 5
# this ensures that startup fuel is continually removed to make way for equilibrium fuel
eq_mats = {}
for channel_num, volumes in enumerate(trgtchnv):
    for volume_num in range(volumes):
        eq_mats[f'c{channel_num}v{volume_num}'] = [(run_in_fuel, n) for n in range(0,6)]

# the PebbleSorter class houses the functionality to perform a run-in analysis
# the keyword args listed below show some of the functionality to manipulate the process
ps = psp.PebbleSorter(power_level=200E+6, # the power level of the reactor (W)
                      output_dir=output_dir, # directory where outputs should be placed
                      fuel_material=run_in_fuel, # dictionary of the fuel isotopics for the fuel which will be initially used
                      run_in_steps=steps, # dictionary of the steps desired for manipulating the time-dependent PBR problem
                      steps=200, # desired number of time steps steps to take 
                      day_limit = 3000, # desired number of days to run to simulation to
                      pass_limit=6, # number of passes required before pebbles are discharged
                      burnup_limit = 1000.0, # burnup limit allowed before pebbles are discharged
                      depletion_steps = [5,5], # list of ints/floats denoting how many days each serpent run will deplete (this depletes a total of 10 days, in two 5 day increments resulting in 3 serpent calculations)
                      keep_files = True, # flag to keep all associated input/output files
                      num_particles=20000, # number of particles in Serpent calculation
                      num_generations=200, # number of generations in Serpent calculation
                      num_skipped_generations=40, # number of skipped generations in Serpent calculation
                      core_inlet_temperature=500.0, # temperature of core inlet, can be used to create temperature profile
                      core_outlet_temperature=500.0, # temperature of the core outlet, can be used to create temperature profile
                      fuel_temperature=500.0, # temperature of the fuel kernels
                      pebble_temperature=500.0, # temperature of the graphite matrix for the fuel pebbles
                      final_pass_limit=6, # pass limit for equilibrium fuel
                      final_homogenization_group=1, # denotion of fuel type for equilibrium fuel, start up fuel is denoted as 0
                      equilibrium_core = True, # this is used to create a core with pebbles that can be assigned to each axial zone, allowing for jump-in to equilibrium calculation or for startup fuel to artificially be given a pass number
                      equilibrium_materials = eq_mats, # materials to be assigned to each axial zone as required if equilibrium_core=True
                      automatic_fuel_transition = True, # automitically transitions from startup fuel to equilibrium fuel once the fraction of graphite pebbles is less than 3% of the entire core
                      equilibrium_fuel_material = equilibrium_fuel_material, # dictionary of the equilibrium fuel
                      cr_insertion_depth = 100, # rough depth from the top of the upper conus to insert the control rods into the core
                      allowable_keff=1.004, # allowable keff to determine when to stop the simulation
                     ) 

# assign_pebble_dist_variables method creates the geometry necessary for the PBR
# pbcyll is the height of the core (excluding the lower conus) - note that the height of the core is measured from the bottom of the core (top of the conus)
# pblwcon is the height of the lower conus
# pbupconl is the height of the upper conus, the upper conus can also be created by increasing pbcyll if the pebble distribution already includes the upper conus
# pbr is the radius of the pebble bed, typically this is set to larger than the actual radius to prevent cutting pebbles, but can be used to shrink the radius if necessary
# dcr is the radius of the lower conus
# axial_offset is used to shift pebbles in the distribution file
# idistrfile is the file path for the pebble locations in the core, this can be obtained via DEM calculations or serpent's built in method
# odistrfile is the output distribution file path
# chcurves describes how the streamlines curve through the core
# trgtchnv is the number of axial zones for each streamlines
ps.assign_pebble_dist_variables(pbcyll=893, pblwconl=55.438, pbupconl=54.0, pbr=120.0,
                       dcr=26.0, axial_offset=-235.538, idistrfile=pebble_dist_path,
                       odistrfile='findist.txt', chcurvs=chcurvs,
                       log=None, trgtchnv=trgtchnv)
# we can set the random number in an attempt to minimize differences in runs
ps.set_random_seed(1)

# perform the run in (or equilibrium) calculation
ps.perform_run_in()
```
