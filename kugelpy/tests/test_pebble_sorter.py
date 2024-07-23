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
    peb_nums = [(pebble._pebble_number, pebble._num_passes, pebble._material, pebble._universe, pebble._previous_universe)
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

    pebble_order = [copy.deepcopy(pebble._pebble_type) for pebble in ps._pebble_array[0][0]]
    ps._burnup_materials = {0:{}, 1: {'f0_c1v0': {'92234':  1, 'volume': 1},
                                     'f0_c1v1': {'92234':  2, 'volume': 1},
                                     'f0_c0v2': {'92234':  3, 'volume': 1},
                                     'f0_c0v0': {'92234':  4, 'volume': 1},
                                     'f0_c0v1': {'92234':  5, 'volume': 1},}}
    ps.read_volume_powers()
    ps._pebble_array[0][1][-1].homogenization_group = 1
    ps.shift_pebbles()
    print(pebble_order == [pebble._pebble_type for pebble in ps._pebble_array[0][1]], file=regtest)    
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
    print([x._pebble_type for x in ps._pebble_array[0][0]], file=regtest)
    print([x._pebble_type for x in ps._pebble_array[1][0]], file=regtest) 
    print([x._material['fuel'] for x in ps._pebble_array[0][0] if x._pebble_type == 'fuel'], file=regtest) 
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
    print([x._pebble_type for x in ps._pebble_array[0][0]], file=regtest)
    print([x._pebble_type for x in ps._pebble_array[0][0]], file=regtest) 
    print([x._material['fuel'] for x in ps._pebble_array[0][0] if x._pebble_type == 'fuel' ], file=regtest)
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
    peb_nums = [(pebble._pebble_number, pebble._num_passes, pebble._material, pebble._universe, pebble._previous_universe)
                for channel in ps._pebble_array
                for volume in channel
                for pebble in volume]

    pebble = ps._pebble_array[1][0][0]
    fuel=pebble._material['fuel'] if pebble._pebble_type == 'fuel' else 'graphite'
    power = round(pebble._power_days,5) if pebble._pebble_type == 'fuel' else 0.0
    print('*****************************************************************************************************************************************************************************')   
    print(f'Pebble Num: {pebble._pebble_number}, Pass Num: {pebble._num_passes}, BU Num: {round(pebble._burnup,5)}, Power Days: {power} Universe: {pebble._universe}, \nMaterial: {fuel}')
    ps.homogenization_group=1
    ps.graphite_fraction = 0.0
    ps.shift_pebbles()
    ps.refuel_pebbles()
    peb_nums = [(pebble._pebble_number, pebble._num_passes, pebble._material, pebble._universe, pebble._previous_universe)
                for channel in ps._pebble_array
                for volume in channel
                for pebble in volume]
    print(peb_nums, file=regtest)
    
    pebble = ps._pebble_array[1][1][0]
    fuel=pebble._material['fuel'] if pebble._pebble_type == 'fuel' else 'graphite'
    power = round(pebble._power_days,5) if pebble._pebble_type == 'fuel' else 0.0
    print('*****************************************************************************************************************************************************************************')   
    print(f'Pebble Num: {pebble._pebble_number}, Pass Num: {pebble._num_passes}, BU Num: {round(pebble._burnup,5)}, Power Days: {power} Universe: {pebble._universe}, \nMaterial: {fuel}')
    print('*****************************************************************************************************************************************************************************')   
    pebble = ps._pebble_array[1][0][0]
    fuel=pebble._material['fuel'] if pebble._pebble_type == 'fuel' else 'graphite'
    power = round(pebble._power_days,5) if pebble._pebble_type == 'fuel' else 0.0
    print('*****************************************************************************************************************************************************************************')   
    print(f'Pebble Num: {pebble._pebble_number}, Pass Num: {pebble._num_passes}, BU Num: {round(pebble._burnup,5)}, Power Days: {power} Universe: {pebble._universe}, \nMaterial: {fuel}')
    print('*****************************************************************************************************************************************************************************')
    ps.shift_pebbles()
    ps.refuel_pebbles()
    peb_nums = [(pebble._pebble_number, pebble._num_passes, pebble._material, pebble._universe, pebble._previous_universe)
                for channel in ps._pebble_array
                for volume in channel
                for pebble in volume]
    print(peb_nums, file=regtest)    
 
    pebble = ps._pebble_array[0][0][232]
    fuel=pebble._material['fuel'] if pebble._pebble_type == 'fuel' else 'graphite'
    power = round(pebble._power_days,5) if pebble._pebble_type == 'fuel' else 0.0
    print('*****************************************************************************************************************************************************************************')   
    print(f'Pebble Num: {pebble._pebble_number}, Pass Num: {pebble._num_passes}, BU Num: {round(pebble._burnup,5)}, Power Days: {power} Universe: {pebble._universe}, \nMaterial: {fuel}')
    print('*****************************************************************************************************************************************************************************')
    pebble = ps._pebble_array[1][1][0]
    fuel=pebble._material['fuel'] if pebble._pebble_type == 'fuel' else 'graphite'
    power = round(pebble._power_days,5) if pebble._pebble_type == 'fuel' else 0.0
    print('*****************************************************************************************************************************************************************************')   
    print(f'Pebble Num: {pebble._pebble_number}, Pass Num: {pebble._num_passes}, BU Num: {round(pebble._burnup,5)}, Power Days: {power} Universe: {pebble._universe}, \nMaterial: {fuel}')
    print('*****************************************************************************************************************************************************************************')


    ps.shift_pebbles()
    ps.refuel_pebbles()
    peb_nums = [(pebble._pebble_number, pebble._num_passes, pebble._material, pebble._universe, pebble._previous_universe)
                for channel in ps._pebble_array
                for volume in channel
                for pebble in volume]
    print(peb_nums, file=regtest)
    
    pebble = ps._pebble_array[0][1][232]
    fuel=pebble._material['fuel'] if pebble._pebble_type == 'fuel' else 'graphite'
    power = round(pebble._power_days,5) if pebble._pebble_type == 'fuel' else 0.0
    print('*****************************************************************************************************************************************************************************')
    print(f'Pebble Num: {pebble._pebble_number}, Pass Num: {pebble._num_passes}, BU Num: {round(pebble._burnup,5)}, Power Days: {power} Universe: {pebble._universe}, \nMaterial: {fuel}')
    print('*****************************************************************************************************************************************************************************')
    
    pebble = ps._pebble_array[1][0][1390]
    fuel=pebble._material['fuel'] if pebble._pebble_type == 'fuel' else 'graphite'
    power = round(pebble._power_days,5) if pebble._pebble_type == 'fuel' else 0.0
    print('*****************************************************************************************************************************************************************************')   
    print(f'Pebble Num: {pebble._pebble_number}, Pass Num: {pebble._num_passes}, BU Num: {round(pebble._burnup,5)}, Power Days: {power} Universe: {pebble._universe}, \nMaterial: {fuel}')
    print('*****************************************************************************************************************************************************************************')
    ps.create_temperature_profile(500,900,'fuel',axial_zones=5)

    ps.shift_pebbles()
    ps.refuel_pebbles()
    peb_nums = [(pebble._pebble_number, pebble._num_passes, pebble._material, pebble._universe, pebble._previous_universe, pebble._temperature)
                for channel in ps._pebble_array
                for volume in channel
                for pebble in volume]
    print(peb_nums, file=regtest)
    pebble = ps._pebble_array[1][1][1390]
    fuel=pebble._material['fuel'] if pebble._pebble_type == 'fuel' else 'graphite'
    power = round(pebble._power_days,5) if pebble._pebble_type == 'fuel' else 0.0
    print('*****************************************************************************************************************************************************************************')   
    print(f'Pebble Num: {pebble._pebble_number}, Pass Num: {pebble._num_passes}, BU Num: {round(pebble._burnup,5)}, Power Days: {power} Universe: {pebble._universe}, \nMaterial: {fuel}')
    print('*****************************************************************************************************************************************************************************')
