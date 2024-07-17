'''
@author: balep, stewryan, ethan-fowler

Copyright 2024, Battelle Energy Alliance, LLC, ALL RIGHTS RESERVED
'''

import os
from os import path
import shutil
import kugelpy.kugelpy.kugelpy.pebble_sorter as psp
import copy
from kugelpy.kugelpy.mutineer.testutils import gen_tmp_folder, find_pbed_input, compare_pbeds

#===============================================================================
# Shared objects
#===============================================================================
# Paths.
main_dir = path.dirname(path.realpath(__file__))
ifiles_dir = path.join(main_dir, 'testfiles')
distfile_path = path.join(ifiles_dir, 'dist.txt')
main_tests_dir = path.join(main_dir, '_tmp/')
gen_tmp_folder(main_tests_dir)

chcurvs = [
            [[37.00, 0.00],
            [0.00, 0.00]],

            [[37.00, 12.0, 0.00],
            [60.00, 60.0, 12.00]],

            [[37.00, 12.00, 0.00],
            [120.00, 120.00, 24.00]]]
trgtchnv = [3, 2]

def test_pebble_sorter_init(regtest):
    ps = psp.PebbleSorter()
    # Check init
    print(ps._kernel_data      , file=regtest)
    print(ps.graphite_fraction, file=regtest)
    print(ps.graphite_height  , file=regtest)

def test_setup_kernel(regtest):

    ps = psp.PebbleSorter()
    ps.setup_kernel()
    print(ps._kernel_data, file=regtest)
        
def test_homogenize_materials(regtest):
    
    ps = psp.PebbleSorter()
    ps._pebble_array = [[
                        [0,0],[0,0]  ],[
                        [0,0],[0,0]  ]]
    
    ps.critical_timestep = 0
    ps._burnup_materials[0] = {'f0_c0v1' :      {'92234': 1, 'volume': 5},
                              'f0_c0v0_c0v1' : {'92234': 2, 'volume': 10},
                              'f0_c1v1' :      {'92234': 3, 'volume': 15},
                              'f0_c0v0_c1v1' : {'92234': 4, 'volume': 20},}
    ps.homogenize_materials()
    print(ps._homogenized_materials_dict[1][0]['mats'], file=regtest) 
    print(ps._homogenized_materials_dict[1][0]['vol'] , file=regtest) 
    print(ps._homogenized_materials_dict[2][0]['mats'], file=regtest) 
    print(ps._homogenized_materials_dict[2][0]['vol'] , file=regtest) 
    
    print(ps._homogenized_materials_dict[1][0]['mats']) 
    print(ps._homogenized_materials_dict[1][0]['vol'] ) 
    print(ps._homogenized_materials_dict[2][0]['mats']) 
    print(ps._homogenized_materials_dict[2][0]['vol'] )   

def test_homogenize_materials_two_pebbles(regtest):
    
    ps = psp.PebbleSorter()
    ps._pebble_array = [[
                        [0,0],[0,0]  ],[
                        [0,0],[0,0]  ]]
    
    ps.critical_timestep = 0
    ps._homogenization_group = 1
    ps._burnup_materials = {0: {'f0_c0v1' :      {'92234': 1, 'volume': 5},
                               'f0_c1v1' :      {'92234': 3, 'volume': 15},
                               'f0_c0v0_c0v1' : {'92234': 2, 'volume': 10},
                               'f0_c0v0_c1v1' : {'92234': 4, 'volume': 20},
                               'f1_c0v0_c0v1' : {'92234': 6, 'volume': 15},
                               'f1_c0v0_c1v1' : {'92234': 5, 'volume': 25},}}
    ps.homogenize_materials()
    print(ps._homogenized_materials_dict)
    print(ps._homogenized_materials_dict[1][0]['mats'], file=regtest) 
    print(ps._homogenized_materials_dict[1][0]['vol'] , file=regtest) 
    print(ps._homogenized_materials_dict[2][0]['mats'], file=regtest) 
    print(ps._homogenized_materials_dict[2][0]['vol'] , file=regtest)   
    print(ps._homogenized_materials_dict[2][1]['vol'] , file=regtest)
    print(ps._homogenized_materials_dict[2][1]['mats'] , file=regtest)
    
def test_write_pebble_location_file():
    temp_path = path.join(main_tests_dir, 'test_write_pebble_location_file')
    gen_tmp_folder(temp_path)
    ps = psp.PebbleSorter(graphite_height=12.5,
                          output_dir=temp_path,
                          pebble_distribution_file='small_pbr')

    
    ps.assign_pebble_dist_variables(pbcyll=25.0, pblwconl=12.0, pbupconl=0.0, pbr=120.0,
                           dcr=24.0, idistrfile=distfile_path,
                           odistrfile='small_pbr.pbed', chcurvs=chcurvs,
                           log='', trgtchnv=trgtchnv)
    ps.read_in_pebble_dist()
    ps.write_pebble_location_file()
    # with open(os.path.join(temp_path, 'small_pbr_Step1.pbed')) as fc:
    #     print(fc.read(), file=regtest) 
    solution_path = path.join(main_dir, '_regtest_outputs')

    # output path
    test_path = path.join(main_tests_dir, 'test_write_pebble_location_file')

    solution_file ='test_pebble_sorter.test_write_pebble_location_file.out'
    test_file = 'small_pbr_Step1.pbed'

    solution_start_line, solution_end_line, format = find_pbed_input(solution_file, solution_path)
    assert compare_pbeds(solution_file, solution_path, test_file, test_path, solution_start_line, solution_end_line, format) == True

def test_write_pebble_data_refuel(regtest):
    temp_path = path.join(main_tests_dir, 'test_write_pebble_data_refuel')
    gen_tmp_folder(temp_path)
    shutil.copy(path.join(ifiles_dir, 'serpent.inp_det0.m'), path.join(temp_path, 'serpent.inp_det0.m'))
    shutil.copy(path.join(ifiles_dir, 'serpent.inp_det0.m'), path.join(temp_path, 'serpent.inp_det1.m'))
    shutil.copy(path.join(ifiles_dir, 'serpent.inp.bumat0'), path.join(temp_path, 'serpent.inp.bumat0'))
    shutil.copy(path.join(ifiles_dir, 'serpent.inp.bumat1'), path.join(temp_path, 'serpent.inp.bumat1'))
    shutil.copy(path.join(ifiles_dir, 'serpent.inp_res.m'),  path.join(temp_path, 'serpent.inp_res.m' ))    
    ps = psp.PebbleSorter(graphite_fraction=0.5,
                          output_dir=temp_path,
                          homogenize_passes = True)

    
    ps.assign_pebble_dist_variables(pbcyll=25.0, pblwconl=12.0, pbupconl=0.0, pbr=120.0,
                           dcr=24.0, idistrfile=distfile_path,
                           odistrfile='small_pbr.pbed', chcurvs=chcurvs,
                           log='', trgtchnv=trgtchnv)
    ps._burnup_materials = {0:{}, 1: {'f0_c1v0': {'92234':  1, 'volume': 1},
                                     'f0_c1v1': {'92234':  2, 'volume': 1},
                                     'f0_c0v2': {'92234':  3, 'volume': 1},
                                     'f0_c0v0': {'92234':  4, 'volume': 1},
                                     'f0_c0v1': {'92234':  5, 'volume': 1},
                                     'f0_c0v0_c0v0': {'92234':  6, 'volume': 1},
                                     'f0_c0v0_c1v0': {'92234':  7, 'volume': 1},}}
    ps.set_random_seed(2)
    ps.read_in_pebble_dist()
    ps.read_volume_powers()
    ps.shift_pebbles()
    ps.refuel_pebbles()     
    ps.write_pebble_data()
    files = ['pebble_materials.inp', 'pebble_cells.inp', 'pebble_surfaces.inp']
    for file in files:
        with open(os.path.join(temp_path, file)) as fc:
            print(fc.read(), file=regtest) 
    
def test_write_pebble_data(regtest):
    temp_path = path.join(main_tests_dir, 'test_write_pebble_data')
    gen_tmp_folder(temp_path)
    ps = psp.PebbleSorter(graphite_height=12.5,
                          output_dir=temp_path)
    
    ps.assign_pebble_dist_variables(pbcyll=25.0, pblwconl=12.0, pbupconl=0.0, pbr=120.0,
                           dcr=24.0, idistrfile=distfile_path,
                           odistrfile='small_pbr.pbed', chcurvs=chcurvs,
                           log='', trgtchnv=trgtchnv)
    
    ps.read_in_pebble_dist()
    ps.write_pebble_data()
    files = ['pebble_materials.inp', 'pebble_cells.inp', 'pebble_surfaces.inp']
    for file in files:
        with open(os.path.join(temp_path, file)) as fc:
            print(fc.read(), file=regtest)    

def test_write_serpent_input(regtest):
    temp_path = path.join(main_tests_dir, 'test_write_serpent_input')
    gen_tmp_folder(temp_path)
    ps = psp.PebbleSorter(graphite_height=12.5,
                          output_dir=temp_path,
                          )
    
    ps.assign_pebble_dist_variables(pbcyll=25.0, pblwconl=12.0, pbupconl=0.0, pbr=120.0,
                           dcr=24.0, idistrfile=distfile_path,
                           odistrfile='small_pbr.pbed', chcurvs=chcurvs,
                           log='', trgtchnv=trgtchnv)
    
    ps.read_in_pebble_dist()
    ps.build_pbr_core()
    ps.write_serpent_input()
    with open(os.path.join(temp_path, 'serpent.inp')) as fc:
        print(fc.read(), file=regtest)   

def test_write_serpent_input_no_dimples(regtest):
    temp_path = path.join(main_tests_dir, 'test_write_serpent_input_no_dimples')
    gen_tmp_folder(temp_path)
    ps = psp.PebbleSorter(graphite_height=12.5,
                          output_dir=temp_path,
                          create_dimples=False)
    
    ps.assign_pebble_dist_variables(pbcyll=25.0, pblwconl=12.0, pbupconl=0.0, pbr=120.0,
                           dcr=24.0, idistrfile=distfile_path,
                           odistrfile='small_pbr.pbed', chcurvs=chcurvs,
                           log='', trgtchnv=trgtchnv)
    
    ps.read_in_pebble_dist()
    ps.build_pbr_core()
    ps.write_serpent_input()
    with open(os.path.join(temp_path, 'serpent.inp')) as fc:
        print(fc.read(), file=regtest)   

def test_write_serpent_input_simple_core(regtest):
    temp_path = path.join(main_tests_dir, 'test_write_serpent_input_simple_core')
    gen_tmp_folder(temp_path)
    ps = psp.PebbleSorter(graphite_height=12.5,
                          output_dir=temp_path,
                          create_dimples=False,
                          simple_core = True)
    
    ps.assign_pebble_dist_variables(pbcyll=25.0, pblwconl=0.0, pbupconl=0.0, pbr=120.0,
                           dcr=0.0, idistrfile=distfile_path,
                           odistrfile='small_pbr.pbed', chcurvs=chcurvs,
                           log='', trgtchnv=trgtchnv)

    ps.read_in_pebble_dist()
    ps.build_pbr_core()
    ps.write_serpent_input()
    with open(os.path.join(temp_path, 'serpent.inp')) as fc:
        print(fc.read(), file=regtest)   

def test_create_temperature_profile(regtest):
    temp_path = path.join(main_tests_dir, 'test_create_temperature_profile')
    gen_tmp_folder(temp_path)   
    ps = psp.PebbleSorter(graphite_height=12.5,
                          output_dir=temp_path,
                          )

    trgtchnv = [10, 11, 12, 15, 19]
    ps.assign_pebble_dist_variables(pbcyll=893.0, pblwconl=54.0, pbupconl=0.0, pbr=120.0,
                       dcr=24.0, axial_offset=170.0, idistrfile='./tests/testfiles/rawdist.txt',
                       odistrfile='findist.txt', chcurvs=chcurvs,
                       log='', trgtchnv=trgtchnv)
    ps.core_inlet_temperature = 500
    ps.core_outlet_temperature = 900
    fuel_dict = ps.create_temperature_profile(500,900,'fuel',axial_zones=5)
    print(fuel_dict, file=regtest)
    ps.core_outlet_temperature = 1000
    fuel_dict = ps.create_temperature_profile(500,1000,'fuel',axial_heights=[0,300,400,500,600])
    print(fuel_dict, file=regtest)
    ps.core_outlet_temperature = 900
    pebble_dict = ps.create_temperature_profile(500,900,'pebble',axial_zones=3)
    print(pebble_dict, file=regtest)  
        
def test_setup_core(regtest):
    temp_path = path.join(main_tests_dir, 'test_setup_core')
    gen_tmp_folder(temp_path) 
    ps = psp.PebbleSorter(graphite_height=12.5,
                          output_dir=temp_path,
                          )
    
    ps.assign_pebble_dist_variables(pbcyll=25.0, pblwconl=12.0, pbupconl=0.0, pbr=120.0,
                           dcr=24.0, idistrfile=distfile_path,
                           odistrfile='small_pbr.pbed', chcurvs=chcurvs,
                           log='', trgtchnv=trgtchnv)
    
    ps.read_in_pebble_dist()
    ps.setup_core()
    files = ['pebble_materials.inp', 'pebble_cells.inp', 'pebble_surfaces.inp']
    for file in files:
        with open(os.path.join(temp_path, file)) as fc:
            print(fc.read(), file=regtest)

def test_update_run_in_step(regtest):
    temp_path = path.join(main_tests_dir, 'test_update_run_in_step')
    gen_tmp_folder(temp_path) 
    steps = {30: {'fuel_material': {'92235': 1.0},
                    'power_level': 100E+9,
                    'graphite_fraction': 0.5},
             120: {'fuel_material': {'92238': 1.0},
                    'power_level': 100E+7,
                    'graphite_fraction': 0.25}}

    ps = psp.PebbleSorter(graphite_height=450,
                          output_dir=temp_path,
                          run_in_steps=steps
                          )
    ps.update_run_in_step()
    ps.efpd_tracker = 30
    print(ps.power_level      , file=regtest)
    print(ps.fuel_material    , file=regtest)
    print(ps.graphite_fraction, file=regtest)

    ps.update_run_in_step()
    ps.efpd_tracker = 119
    print(ps.power_level       ,  file=regtest)
    print(ps.fuel_material     ,  file=regtest)
    print(ps.graphite_fraction ,  file=regtest)

    ps.update_run_in_step()
    ps.efpd_tracker = 120
    print(ps.power_level       ,  file=regtest)
    print(ps.fuel_material     ,  file=regtest)
    print(ps.graphite_fraction ,  file=regtest)

    ps.update_run_in_step()
    ps.efpd_tracker = 121
    print(ps.fuel_material     , file=regtest)
    print(ps.power_level       , file=regtest)
    print(ps.graphite_fraction , file=regtest)
    print(len(ps.run_in_steps) , file=regtest)

def test_read_burn_material(regtest):
    temp_path = path.join(main_tests_dir, 'test_kugel_read_burn_material')
    gen_tmp_folder(temp_path) 
    shutil.copy(path.join(ifiles_dir, 'serpent.inp.bumat0'), path.join(temp_path, 'serpent.inp.bumat0'))
    shutil.copy(path.join(ifiles_dir, 'serpent.inp.bumat1'), path.join(temp_path, 'serpent.inp.bumat1'))    
    ps = psp.PebbleSorter(graphite_height=45.0,
                          output_dir=temp_path)

    ps.read_burn_material()
    print(ps._burnup_materials, file=regtest)

def test_read_in_pebble_dist(regtest):

    ps = psp.PebbleSorter(graphite_height=12.50,
                          output_dir=main_tests_dir,)

    ps.assign_pebble_dist_variables(pbcyll=25.0, pblwconl=12.0, pbupconl=0.0, pbr=120.0,
                           dcr=24.0, idistrfile=distfile_path,
                           odistrfile='small_pbr.pbed', chcurvs=chcurvs,
                           log='', trgtchnv=trgtchnv)
    
    ps.read_in_pebble_dist()
    peb_nums = [(pebble.pebble_number, pebble.num_passes, pebble.material, pebble.universe, pebble.previous_universe)
                for channel in ps._pebble_array
                for volume in channel
                for pebble in volume]
    print(peb_nums, file=regtest)
    
def test_shift_pebbles(regtest):
    temp_path = path.join(main_tests_dir, 'test_shift_pebbles')
    gen_tmp_folder(temp_path) 
    shutil.copy(path.join(ifiles_dir, 'serpent.inp_det0.m'), path.join(temp_path, 'serpent.inp_det0.m'))
    shutil.copy(path.join(ifiles_dir, 'serpent.inp_det0.m'), path.join(temp_path, 'serpent.inp_det1.m'))
    shutil.copy(path.join(ifiles_dir, 'serpent.inp.bumat0'), path.join(temp_path, 'serpent.inp.bumat0'))
    shutil.copy(path.join(ifiles_dir, 'serpent.inp.bumat1'), path.join(temp_path, 'serpent.inp.bumat1'))
    shutil.copy(path.join(ifiles_dir, 'serpent.inp_res.m'),  path.join(temp_path, 'serpent.inp_res.m' ))     
    ps = psp.PebbleSorter(graphite_height=0.0,
                          graphite_fraction = 0.25,
                           initial_pebble_distribution_file='pf59_full_core',
                           output_dir=temp_path,
                           path_to_template_files='./pebshuf/templates/')
    
    ps.assign_pebble_dist_variables(pbcyll=25.0, pblwconl=12.0, pbupconl=0.0, pbr=120.0,
                           dcr=24.0, idistrfile=distfile_path,
                           odistrfile='findist.txt', chcurvs=chcurvs,
                           log='', trgtchnv=trgtchnv)
    ps.read_in_pebble_dist()

    pebble_order = [copy.deepcopy(pebble.pebble_type) for pebble in ps._pebble_array[0][0]]
    ps._burnup_materials = {0:{}, 1: {'f0_c1v0': {'92234':  1, 'volume': 1},
                                     'f0_c1v1': {'92234':  2, 'volume': 1},
                                     'f0_c0v2': {'92234':  3, 'volume': 1},
                                     'f0_c0v0': {'92234':  4, 'volume': 1},
                                     'f0_c0v1': {'92234':  5, 'volume': 1},}}
    ps.read_volume_powers()
    ps._pebble_array[0][1][-1].homogenization_group = 1
    ps.shift_pebbles()
    print(pebble_order == [pebble.pebble_type for pebble in ps._pebble_array[0][1]], file=regtest)    
    print(len(ps._unloaded_pebbles) , file=regtest)

def test_refuel_pebbles_homogenize(regtest):
    temp_path = path.join(main_tests_dir, 'test_refuel_pebbles_homogenize')
    gen_tmp_folder(temp_path) 
    shutil.copy(path.join(ifiles_dir, 'serpent.inp_det0.m'), path.join(temp_path, 'serpent.inp_det0.m'))
    shutil.copy(path.join(ifiles_dir, 'serpent.inp_det0.m'), path.join(temp_path, 'serpent.inp_det1.m'))
    shutil.copy(path.join(ifiles_dir, 'serpent.inp.bumat0'), path.join(temp_path, 'serpent.inp.bumat0'))
    shutil.copy(path.join(ifiles_dir, 'serpent.inp.bumat1'), path.join(temp_path, 'serpent.inp.bumat1'))
    shutil.copy(path.join(ifiles_dir, 'serpent.inp_res.m'),  path.join(temp_path, 'serpent.inp_res.m' ))     
    ps = psp.PebbleSorter(graphite_fraction=0.25,
                           initial_pebble_distribution_file='pf59_full_core',
                           output_dir=temp_path,
                           path_to_template_files='./pebshuf/templates/',
                           homogenize_passes = True)

    
    ps.assign_pebble_dist_variables(pbcyll=25.0, pblwconl=12.0, pbupconl=0.0, pbr=120.0,
                           dcr=24.0, idistrfile=distfile_path,
                           odistrfile='findist.txt', chcurvs=chcurvs,
                           log='', trgtchnv=trgtchnv)
    ps.set_random_seed(2)
    ps.read_in_pebble_dist()
    ps._burnup_materials = {0:{}, 1: {'f0_c1v0': {'92234':  1, 'volume': 1},
                                     'f0_c1v1': {'92234':  2, 'volume': 1},
                                     'f0_c0v2': {'92234':  3, 'volume': 1},
                                     'f0_c0v0': {'92234':  4, 'volume': 1},
                                     'f0_c0v1': {'92234':  5, 'volume': 1},}}
    ps.read_volume_powers()
    ps.shift_pebbles()
    print(ps._pebble_array[0][0], file=regtest)
    print(ps._pebble_array[1][0], file=regtest) 
    print(len(ps._unloaded_fuel_pebbles), file=regtest)
    print(len(ps._unloaded_pebbles), file=regtest)
    ps.refuel_pebbles()
    print([x.pebble_type for x in ps._pebble_array[0][0]], file=regtest)
    print([x.pebble_type for x in ps._pebble_array[1][0]], file=regtest) 
    print([x.material['fuel'] for x in ps._pebble_array[0][0] if x.pebble_type == 'fuel'], file=regtest) 
    print(len(ps._unloaded_fuel_pebbles), file=regtest)
    print(len(ps._unloaded_pebbles), file=regtest)

    
def test_refuel_pebbles(regtest):
    temp_path = path.join(main_tests_dir, 'test_refuel_pebbles')
    gen_tmp_folder(temp_path) 
    shutil.copy(path.join(ifiles_dir, 'serpent.inp_det0.m'), path.join(temp_path, 'serpent.inp_det0.m'))
    shutil.copy(path.join(ifiles_dir, 'serpent.inp_det0.m'), path.join(temp_path, 'serpent.inp_det1.m'))
    ps = psp.PebbleSorter(graphite_height=0.0,
                           initial_pebble_distribution_file='pf59_full_core',
                           output_dir=temp_path,
                           path_to_template_files='./pebshuf/templates/',
                           homogenize_passes = False)
    trgtchnv = [3, 2]
    
    ps.assign_pebble_dist_variables(pbcyll=25.0, pblwconl=12.0, pbupconl=0.0, pbr=120.0,
                           dcr=24.0, idistrfile=distfile_path,
                           odistrfile='findist.txt', chcurvs=chcurvs,
                           log='', trgtchnv=trgtchnv)
    ps.set_random_seed(2)    
    ps.read_in_pebble_dist()
    ps._burnup_materials = {0:{}, 1: {'f0_c1v0': {'92234':  1, 'volume': 1},
                                     'f0_c1v1': {'92234':  2, 'volume': 1},
                                     'f0_c0v2': {'92234':  3, 'volume': 1},
                                     'f0_c0v0': {'92234':  4, 'volume': 1},
                                     'f0_c0v1': {'92234':  5, 'volume': 1},}}
    ps.read_volume_powers()
    ps.shift_pebbles()
    print(ps._pebble_array[0][0], file=regtest)
    print(ps._pebble_array[1][0], file=regtest) 
    print(len(ps._unloaded_fuel_pebbles), file=regtest)
    print(len(ps._unloaded_pebbles), file=regtest)
    ps.refuel_pebbles()
    print([x.pebble_type for x in ps._pebble_array[0][0]], file=regtest)
    print([x.pebble_type for x in ps._pebble_array[0][0]], file=regtest) 
    print([x.material['fuel'] for x in ps._pebble_array[0][0] if x.pebble_type == 'fuel' ], file=regtest)
    print(len(ps._unloaded_fuel_pebbles), file=regtest)
    print(len(ps._unloaded_pebbles), file=regtest)
    
def test_read_volume_powers(regtest):
    temp_path = path.join(main_tests_dir, 'test_read_volume_powers')
    gen_tmp_folder(temp_path) 
    shutil.copy(path.join(ifiles_dir, 'serpent.inp_det0.m'), path.join(temp_path, 'serpent.inp_det0.m'))
    shutil.copy(path.join(ifiles_dir, 'serpent.inp_det0.m'), path.join(temp_path, 'serpent.inp_det1.m'))    
    ps = psp.PebbleSorter(graphite_height=0.0,
                           output_dir=temp_path,
                           path_to_template_files='./pebshuf/templates/')
    ps.read_volume_powers()
    print(ps.volume_powers, file=regtest)
    
# Test currently fails due to a change in the pebble class
#def test_calculate_pebble_features(regtest):
#
#    ps = psp.PebbleSorter.loader('./tests/testfiles/step_100/',100)
#    ps.step_pebble_distribution_file = ps.pebble_distribution_file
#    ps.burnstep = 100
#    ps.load_step = 99
#    bu = ps.calculate_average_pebble_feature('burnup')
#    print(bu, file=regtest)
#    power = ps.calculate_average_pebble_feature('power_density')
#    print(power, file=regtest)
#    bu2 = ps.calculate_discharge_bu()
#    print(bu2, file=regtest)
#    ps.output_dir = './tests/testfiles/'
#    ps.step_pebble_distribution_file = 'pf61_Step100.pbed'
#    max_power = ps.calculate_maximum_pebble_power()
#    print(max_power, file=regtest)
#    ps.keep_files = False
#    ps.save_state_point = False
#    ps.create_solutions_file()
#    ps.update_solution_file()
#    csv_file = open('./tests/testfiles/reactor_status.csv', 'r')
#    print([x for x in csv_file], file=regtest)
#    csv_file.close()
#    os.remove('./tests/testfiles/reactor_status.csv')

def test_refuel_pebbles_homogenize3(regtest):
    temp_path = path.join(main_tests_dir, 'test_refuel_pebbles_homogenize3')
    gen_tmp_folder(temp_path)   
    ps = psp.PebbleSorter(graphite_fraction=0.5,
                          initial_pebble_distribution_file='pf59_full_core',
                          output_dir=main_tests_dir,
                          path_to_template_files='./pebshuf/templates/',
                          pass_limit = 3,
                          homogenize_passes = True)
    
    ps.assign_pebble_dist_variables(pbcyll=25.0, pblwconl=12.0, pbupconl=0.0, pbr=120.0,
                           dcr=24.0, idistrfile=distfile_path,
                           odistrfile='findist.txt', chcurvs=chcurvs,
                           log='', trgtchnv=trgtchnv)
    ps.set_random_seed(2)
    ps.read_in_pebble_dist()
    ps._burnup_materials = {0:{}, 1: {'f0_c1v0': {'92234':  1, 'volume': 1},
                                     'f0_c1v1': {'92234':  2, 'volume': 1},
                                     'f0_c0v2': {'92234':  3, 'volume': 1},
                                     'f0_c0v0': {'92234':  4, 'volume': 1},
                                     'f0_c0v1': {'92234':  5, 'volume': 1},
                                     'f0_c0v0_c0v0': {'92235': 1, 'volume': 1},
                                     'f0_c0v0_c1v0': {'92235': 2, 'volume': 1},
                                     'f0_c0v0_c0v1': {'92235': 3, 'volume': 1},
                                     'f0_c0v0_c1v1': {'92235': 4, 'volume': 1},
                                     'f0_c0v0_c0v2': {'92235': 5, 'volume': 1},
                                     'f0_c0v0_c0v0_c0v0': {'92236': 1, 'volume': 1},
                                     'f0_c0v0_c0v0_c1v0': {'92236': 2, 'volume': 1},
                                     'f0_c0v0_c0v0_c0v1': {'92236': 3, 'volume': 1},
                                     'f0_c0v0_c0v0_c1v1': {'92236': 4, 'volume': 1},
                                     'f0_c0v0_c0v0_c0v2': {'92236': 5, 'volume': 1},
                                     'f1_c1v0': {'92237':  1, 'volume': 1},
                                     'f1_c1v1': {'92237':  2, 'volume': 1},
                                     'f1_c0v2': {'92237':  3, 'volume': 1},
                                     'f1_c0v0': {'92237':  4, 'volume': 1},
                                     'f1_c0v1': {'92237':  5, 'volume': 1},
                                     'f1_c0v0_c0v0': {'92238': 1, 'volume': 1},
                                     'f1_c0v0_c1v0': {'92238': 2, 'volume': 1},
                                     'f1_c0v0_c0v1': {'92238': 3, 'volume': 1},
                                     'f1_c0v0_c1v1': {'92238': 4, 'volume': 1},
                                     'f1_c0v0_c0v2': {'92238': 5, 'volume': 1},
                                     'f1_c0v0_c0v0_c0v0': {'92239': 1, 'volume': 1},
                                     'f1_c0v0_c0v0_c1v0': {'92239': 2, 'volume': 1},
                                     'f1_c0v0_c0v0_c0v1': {'92239': 3, 'volume': 1},
                                     'f1_c0v0_c0v0_c1v1': {'92239': 4, 'volume': 1},
                                     'f1_c0v0_c0v0_c0v2': {'92239': 5, 'volume': 1},
                                    }
                          }
    ps.volume_powers = {'f0_c1v0': (1E6,0),
                                  'f0_c1v1': (1E6,0),
                                  'f0_c0v2': (1E6,0),
                                  'f0_c0v0': (1E6,0),
                                  'f0_c0v1': (1E6,0),
                                  'f0_c0v0_c0v0': (1E6,0),
                                  'f0_c0v0_c1v0': (1E6,0),
                                  'f0_c0v0_c0v1': (1E6,0),
                                  'f0_c0v0_c1v1': (1E6,0),
                                  'f0_c0v0_c0v2': (1E6,0),
                                  'f0_c0v0_c0v0_c0v0': (1E6,0),
                                  'f0_c0v0_c0v0_c1v0': (1E6,0),
                                  'f0_c0v0_c0v0_c0v1': (1E6,0),
                                  'f0_c0v0_c0v0_c1v1': (1E6,0),
                                  'f0_c0v0_c0v0_c0v2': (1E6,0),                                     
                                  'f1_c1v0': (1E6,0),
                                  'f1_c1v1': (1E6,0),
                                  'f1_c0v2': (1E6,0),
                                  'f1_c0v0': (1E6,0),
                                  'f1_c0v1': (1E6,0),
                                  'f1_c0v0_c0v0': (1E6,0),
                                  'f1_c0v0_c1v0': (1E6,0),
                                  'f1_c0v0_c0v1': (1E6,0),
                                  'f1_c0v0_c1v1': (1E6,0),
                                  'f1_c0v0_c0v2': (1E6,0),
                                  'f1_c0v0_c0v0_c0v0': (1E6,0),
                                  'f1_c0v0_c0v0_c1v0': (1E6,0),
                                  'f1_c0v0_c0v0_c0v1': (1E6,0),
                                  'f1_c0v0_c0v0_c1v1': (1E6,0),
                                  'f1_c0v0_c0v0_c0v2': (1E6,0), 
                          }
    peb_nums = [(pebble.pebble_number, pebble.num_passes, pebble.material, pebble.universe, pebble.previous_universe)
                for channel in ps._pebble_array
                for volume in channel
                for pebble in volume]

    pebble = ps._pebble_array[1][0][0]
    fuel=pebble.material['fuel'] if pebble.pebble_type == 'fuel' else 'graphite'
    power = round(pebble.power_days,5) if pebble.pebble_type == 'fuel' else 0.0
    print('*****************************************************************************************************************************************************************************')   
    print(f'Pebble Num: {pebble.pebble_number}, Pass Num: {pebble.num_passes}, BU Num: {round(pebble.burnup,5)}, Power Days: {power} Universe: {pebble.universe}, \nMaterial: {fuel}')
    ps.homogenization_group=1
    ps.graphite_fraction = 0.0
    ps.shift_pebbles()
    ps.refuel_pebbles()
    peb_nums = [(pebble.pebble_number, pebble.num_passes, pebble.material, pebble.universe, pebble.previous_universe)
                for channel in ps._pebble_array
                for volume in channel
                for pebble in volume]
    print(peb_nums, file=regtest)
    
    pebble = ps._pebble_array[1][1][0]
    fuel=pebble.material['fuel'] if pebble.pebble_type == 'fuel' else 'graphite'
    power = round(pebble.power_days,5) if pebble.pebble_type == 'fuel' else 0.0
    print('*****************************************************************************************************************************************************************************')   
    print(f'Pebble Num: {pebble.pebble_number}, Pass Num: {pebble.num_passes}, BU Num: {round(pebble.burnup,5)}, Power Days: {power} Universe: {pebble.universe}, \nMaterial: {fuel}')
    print('*****************************************************************************************************************************************************************************')   
    pebble = ps._pebble_array[1][0][0]
    fuel=pebble.material['fuel'] if pebble.pebble_type == 'fuel' else 'graphite'
    power = round(pebble.power_days,5) if pebble.pebble_type == 'fuel' else 0.0
    print('*****************************************************************************************************************************************************************************')   
    print(f'Pebble Num: {pebble.pebble_number}, Pass Num: {pebble.num_passes}, BU Num: {round(pebble.burnup,5)}, Power Days: {power} Universe: {pebble.universe}, \nMaterial: {fuel}')
    print('*****************************************************************************************************************************************************************************')
    ps.shift_pebbles()
    ps.refuel_pebbles()
    peb_nums = [(pebble.pebble_number, pebble.num_passes, pebble.material, pebble.universe, pebble.previous_universe)
                for channel in ps._pebble_array
                for volume in channel
                for pebble in volume]
    print(peb_nums, file=regtest)    
 
    pebble = ps._pebble_array[0][0][232]
    fuel=pebble.material['fuel'] if pebble.pebble_type == 'fuel' else 'graphite'
    power = round(pebble.power_days,5) if pebble.pebble_type == 'fuel' else 0.0
    print('*****************************************************************************************************************************************************************************')   
    print(f'Pebble Num: {pebble.pebble_number}, Pass Num: {pebble.num_passes}, BU Num: {round(pebble.burnup,5)}, Power Days: {power} Universe: {pebble.universe}, \nMaterial: {fuel}')
    print('*****************************************************************************************************************************************************************************')
    pebble = ps._pebble_array[1][1][0]
    fuel=pebble.material['fuel'] if pebble.pebble_type == 'fuel' else 'graphite'
    power = round(pebble.power_days,5) if pebble.pebble_type == 'fuel' else 0.0
    print('*****************************************************************************************************************************************************************************')   
    print(f'Pebble Num: {pebble.pebble_number}, Pass Num: {pebble.num_passes}, BU Num: {round(pebble.burnup,5)}, Power Days: {power} Universe: {pebble.universe}, \nMaterial: {fuel}')
    print('*****************************************************************************************************************************************************************************')


    ps.shift_pebbles()
    ps.refuel_pebbles()
    peb_nums = [(pebble.pebble_number, pebble.num_passes, pebble.material, pebble.universe, pebble.previous_universe)
                for channel in ps._pebble_array
                for volume in channel
                for pebble in volume]
    print(peb_nums, file=regtest)
    
    pebble = ps._pebble_array[0][1][232]
    fuel=pebble.material['fuel'] if pebble.pebble_type == 'fuel' else 'graphite'
    power = round(pebble.power_days,5) if pebble.pebble_type == 'fuel' else 0.0
    print('*****************************************************************************************************************************************************************************')
    print(f'Pebble Num: {pebble.pebble_number}, Pass Num: {pebble.num_passes}, BU Num: {round(pebble.burnup,5)}, Power Days: {power} Universe: {pebble.universe}, \nMaterial: {fuel}')
    print('*****************************************************************************************************************************************************************************')
    
    pebble = ps._pebble_array[1][0][1390]
    fuel=pebble.material['fuel'] if pebble.pebble_type == 'fuel' else 'graphite'
    power = round(pebble.power_days,5) if pebble.pebble_type == 'fuel' else 0.0
    print('*****************************************************************************************************************************************************************************')   
    print(f'Pebble Num: {pebble.pebble_number}, Pass Num: {pebble.num_passes}, BU Num: {round(pebble.burnup,5)}, Power Days: {power} Universe: {pebble.universe}, \nMaterial: {fuel}')
    print('*****************************************************************************************************************************************************************************')
    ps.create_temperature_profile(500,900,'fuel',axial_zones=5)

    ps.shift_pebbles()
    ps.refuel_pebbles()
    peb_nums = [(pebble.pebble_number, pebble.num_passes, pebble.material, pebble.universe, pebble.previous_universe, pebble.temperature)
                for channel in ps._pebble_array
                for volume in channel
                for pebble in volume]
    print(peb_nums, file=regtest)
    pebble = ps._pebble_array[1][1][1390]
    fuel=pebble.material['fuel'] if pebble.pebble_type == 'fuel' else 'graphite'
    power = round(pebble.power_days,5) if pebble.pebble_type == 'fuel' else 0.0
    print('*****************************************************************************************************************************************************************************')   
    print(f'Pebble Num: {pebble.pebble_number}, Pass Num: {pebble.num_passes}, BU Num: {round(pebble.burnup,5)}, Power Days: {power} Universe: {pebble.universe}, \nMaterial: {fuel}')
    print('*****************************************************************************************************************************************************************************')

# def test_create_griffin_file(regtest):
#     main_dir = os.path.dirname(os.path.realpath(psp.__file__))
#     data_dir = os.path.join(main_dir, 'data')

#     temp_path = path.join(main_tests_dir, 'test_create_griffin_file')
#     gen_tmp_folder(temp_path)

#     chcurvs = [[[1126.49, 1099.74, 1072.99, 1046.23, 1019.48, 992.73, 965.98, 939.22, 912.47, 885.72, 858.96, 832.21, 805.46, 778.71, 751.95, 725.2, 698.45, 671.69, 644.94, 618.19, 591.44, 564.68, 537.93, 511.18, 484.42, 457.67, 430.92, 404.17, 377.41, 350.66, 340.31, 329.97, 319.62, 309.27, 298.92, 288.57, 278.23, 267.88, 257.53, 247.19, 236.84, 226.49, 216.14, 205.79, 195.45, 185.1],
#         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],
#     [[1126.49, 1099.74, 1072.99, 1046.23, 1019.48, 992.73, 965.98, 939.22, 912.47, 885.72, 858.96, 832.21, 805.46, 778.71, 751.95, 725.2, 698.45, 671.69, 644.94, 618.19, 591.44, 564.68, 537.93, 511.18, 484.42, 457.67, 430.92, 404.17, 377.41, 350.66, 340.31, 329.97, 319.62, 309.27, 298.92, 288.57, 278.23, 267.88, 257.53, 247.19, 236.84, 226.49, 216.14, 205.79, 195.45, 185.1],
#         [44.211, 44.211, 44.211, 44.211, 44.211, 44.20345, 44.18431, 44.15973, 44.12076, 44.05477, 43.96634, 43.86105, 43.74685, 43.62336, 43.49642, 43.37785, 43.26327, 43.14269, 43.02477, 42.89514, 42.77098, 42.64801, 42.53059, 42.41545, 42.31044, 42.21782, 42.14349, 42.05958, 41.92575, 41.63257, 41.42335, 41.12016, 40.68085, 40.05544, 39.098, 37.47593, 34.54502, 30.21314, 25.3088, 20.6561, 16.72857, 13.54777, 10.99466, 9.14798, 8.12596, 8.19874]],
#     [[1126.49, 1099.74, 1072.99, 1046.23, 1019.48, 992.73, 965.98, 939.22, 912.47, 885.72, 858.96, 832.21, 805.46, 778.71, 751.95, 725.2, 698.45, 671.69, 644.94, 618.19, 591.44, 564.68, 537.93, 511.18, 484.42, 457.67, 430.92, 404.17, 377.41, 350.66, 340.31, 329.97, 319.62, 309.27, 298.92, 288.57, 278.23, 267.88, 257.53, 247.19, 236.84, 226.49, 216.14, 205.79, 195.45, 185.1],
#         [82.105, 82.105, 82.105, 82.105, 82.105, 82.087, 82.02266, 81.9622, 81.89196, 81.77948, 81.66513, 81.53734, 81.40771, 81.26746, 81.10857, 80.96155, 80.81659, 80.67267, 80.53068, 80.38331, 80.23166, 80.08721, 79.94035, 79.79063, 79.63851, 79.48877, 79.35236, 79.20133, 79.01734, 78.70429, 78.51402, 78.25401, 77.89377, 77.39389, 76.66375, 75.52775, 73.41357, 69.3007, 61.96307, 52.28305, 42.07782, 33.06554, 25.70736, 20.15169, 16.61293, 16.09318]],
#     [[1126.49, 1099.74, 1072.99, 1046.23, 1019.48, 992.73, 965.98, 939.22, 912.47, 885.72, 858.96, 832.21, 805.46, 778.71, 751.95, 725.2, 698.45, 671.69, 644.94, 618.19, 591.44, 564.68, 537.93, 511.18, 484.42, 457.67, 430.92, 404.17, 377.41, 350.66, 340.31, 329.97, 319.62, 309.27, 298.92, 288.57, 278.23, 267.88, 257.53, 247.19, 236.84, 226.49, 216.14, 205.79, 195.45, 185.1],
#         [94.737, 94.737, 94.737, 94.737, 94.737, 94.71306, 94.62775, 94.59489, 94.557, 94.44693, 94.3595, 94.30034, 94.2407, 94.13986, 94.03026, 93.9561, 93.87629, 93.78233, 93.68947, 93.60143, 93.53932, 93.43703, 93.33228, 93.23621, 93.14022, 93.0316, 92.93193, 92.82167, 92.71202, 92.47871, 92.32607, 92.1331, 91.8812, 91.51028, 90.98523, 90.22885, 89.00353, 86.55365, 81.18153, 71.71382, 59.76636, 47.45436, 36.29467, 27.19942, 20.96119, 19.2266]],
#     [[1126.49, 1099.74, 1072.99, 1046.23, 1019.48, 992.73, 965.98, 939.22, 912.47, 885.72, 858.96, 832.21, 805.46, 778.71, 751.95, 725.2, 698.45, 671.69, 644.94, 618.19, 591.44, 564.68, 537.93, 511.18, 484.42, 457.67, 430.92, 404.17, 377.41, 350.66, 340.31, 329.97, 319.62, 309.27, 298.92, 288.57, 278.23, 267.88, 257.53, 247.19, 236.84, 226.49, 216.14, 205.79, 195.45, 185.1],
#         [107.37, 107.37, 107.37, 107.37, 107.37, 107.33419, 107.34077, 107.49045, 107.47701, 107.29504, 107.22586, 107.36764, 107.36501, 107.19078, 107.09066, 107.22299, 107.23292, 107.10503, 106.95589, 107.00479, 107.12655, 107.02795, 106.86841, 106.87822, 106.94322, 106.86412, 106.69916, 106.63512, 106.7939, 106.66, 106.5303, 106.29289, 106.27, 106.137, 105.71554, 105.34689, 104.9322, 104.011, 102.05009, 96.23443, 83.67145, 69.222, 54.54269, 40.42161, 28.33431, 22.96025]],
#     [[1126.49, 1099.74, 1072.99, 1046.23, 1019.48, 992.73, 965.98, 939.22, 912.47, 885.72, 858.96, 832.21, 805.46, 778.71, 751.95, 725.2, 698.45, 671.69, 644.94, 618.19, 591.44, 564.68, 537.93, 511.18, 484.42, 457.67, 430.92, 404.17, 377.41, 350.66, 340.31, 329.97, 319.62, 309.27, 298.92, 288.57, 278.23, 267.88, 257.53, 247.19, 236.84, 226.49, 216.14, 205.79, 195.45, 185.1],
#         [120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 120.0, 112.69338, 95.3547, 78.01603, 60.67735, 43.33868, 26.0]],]

#     trgtchnv = [14, 14, 14, 15, 18]

#     eq_mats = {}
#     run_in_fuel={'92235': 1.18113E-03, '92238': 2.24415E-02, '8016': 3.37336E-2, '6000': 9.260240E-3, '5010': 1.87091E-8, '5011': 7.57813E-8}

#     fuel_material= {'92235': 9.55244E-04, 
#                         '92238': 2.26363E-02, 
#                         '8016': 3.36887E-02, 
#                         '6000': 9.14892E-03 + 9.89522E-05, 
#                         '5010': 1.86845E-08, 
#                         '5011': 7.56816E-08}


#     step_name = f'test_create_griffin_file'
#     for channel_num, volumes in enumerate(trgtchnv):
#         for volume_num in range(volumes):
#             eq_mats[f'c{channel_num}v{volume_num}'] = [(fuel_material, n) for n in range(0,6)]

#     ps = psp.PebbleSorter(graphite_fraction=0.42,
#                         graphite_height=505.15,
#                         output_dir=temp_path,
#                         path_to_template_files=data_dir,
#                         fuel_material=run_in_fuel,
#                         steps=100,
#                         day_limit = 600,
#                         pass_limit=6,
#                         burnup_limit = 1000.0,
#                         depletion_steps = [5,5,5,5],
#                         core_inlet_temperature=500.0,
#                         core_outlet_temperature=500.0,
#                         fuel_temperature=500.0,
#                         pebble_temperature=500.0,
#                         final_pass_limit=6,
#                         final_homogenization_group=1,
#                         equilibrium_core = True,
#                         equilibrium_materials = eq_mats,
#                         equilibrium_fuel_material = {'92235': 3.701063E-3, '92238': 1.992191E-2, '8016': 3.37336E-2, '6000': 9.260240E-3, '5010': 1.87091E-8, '5011': 7.57813E-8},
#                         target_keff = 1.0065,
#                         num_particles = 10000,
#                         num_generations = 100,
#                         critical_keff_tolerance = 1E-3,
#                         path_to_micro_xs = path.join(ifiles_dir, 'os200mw_gcpbr_7ge15_microxs.xml'),
#                         path_to_moose_mesh = path.join(ifiles_dir, 'os200mw_gcpbr_mesh_gfnk.e'),
#     ) 
    
#     ps.assign_pebble_dist_variables(pbcyll=893, pblwconl=55.438, pbupconl=54.0, pbr=120.0,
#                     dcr=26.0, axial_offset=-235.538, idistrfile=os.path.join(data_dir,'rawdist.inp'),
#                     odistrfile='findist.txt', chcurvs=chcurvs,
#                     log=None, trgtchnv=trgtchnv)
#     ps.read_in_pebble_dist()
#     ps.multiphysics_run = True
#     ps.build_pbr_core()
#     ps.setup_core()
#     ps.create_griffin_file()
#     files = ['gpbr200_ri_griffin_step0.i', 'gpbr200_ri_pronghorn_step0.i', 'gpbr200_ri_triso_step0.i',
#             'fuel_blocks_isotope_densities.csv', 'fuel_blocks_burnup.csv']
#     for file in files:
#         file_path = path.join(main_tests_dir, 'test_create_griffin_file', file)
#         with open(file_path) as fc:
#             print(fc.read(), file=regtest) 