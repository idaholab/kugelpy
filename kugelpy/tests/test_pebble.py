'''
@author: balep, stewryan

Copyright 2024, Battelle Energy Alliance, LLC, ALL RIGHTS RESERVED
'''

import kugelpy.kugelpy.kugelpy.pebble as pebble
from kugelpy.kugelpy.mutineer.testutils import gen_tmp_folder
from os import path

main_dir = path.dirname(path.realpath(__file__))
ifiles_dir = path.join(main_dir, 'testfiles')
main_tests_dir = path.join(main_dir,  '_tmp/')
gen_tmp_folder(main_tests_dir)

def test_init(regtest):
    peb = pebble.Pebble(111,111,111,111,111,4,5,temperature=600,pass_limit=5,pebble_number=12345)
    print(vars(peb), file=regtest)

def test_update_position(regtest):
    peb = pebble.Pebble(1,1,1,1,1,1,2,temperature=600,pass_limit=5,pebble_number=12345)
    peb.update_position(111,111,111,111,4,5,shuffled=True)
    print(vars(peb), file=regtest)

def test_increase_pass(regtest):
    peb = pebble.Pebble(1,1,1,1,1,1,2,temperature=600,pass_limit=5,pebble_number=12345)
    peb.increase_pass()
    print(vars(peb), file=regtest)

def test_update_pebble_temperature(regtest):
    peb = pebble.Pebble(1,1,1,1,1,1,2,temperature=600,pass_limit=5,pebble_number=12345)
    peb.update_pebble_temperature(547,fuel_temp=900)
    print(vars(peb), file=regtest)

def test_FuelPebble_init(regtest):
    peb = pebble.FuelPebble(111,111,111,111,111,4,5,temperature=600,fuel_temperature=576, pass_limit=5,pebble_number=12345)
    print(vars(peb), file=regtest)

def test_update_fuel_material(regtest):
    peb = pebble.FuelPebble(111,111,111,111,111,4,5,temperature=600,fuel_temperature=576, pass_limit=5,pebble_number=12345)
    peb.update_fuel_material({'fractions': {'1001': 1.0}})
    print(vars(peb), file=regtest)

def test_update_burnup(regtest):
    peb = pebble.FuelPebble(111,111,111,111,111,4,5,temperature=600,fuel_temperature=576, pass_limit=5,pebble_number=12345)
    peb.update_burnup(20, 5)
    print(vars(peb), file=regtest)

def test_update_pebble_temperature(regtest):
    peb = pebble.FuelPebble(111,111,111,111,111,4,5,temperature=600,fuel_temperature=576, pass_limit=5,pebble_number=12345)
    peb.update_pebble_temperature(547,fuel_temp=900)
    print(vars(peb), file=regtest)

def test_calculate_volumes(regtest):
    peb = pebble.Pebble(111,111,111,111,3,4,5)
    peb.calculate_volumes()
    print(peb.geometry, file=regtest)
    
    fpeb = pebble.FuelPebble(111,111,111,111,3,4,5)
    fpeb.calculate_volumes()
    print(fpeb.geometry, file=regtest)    
