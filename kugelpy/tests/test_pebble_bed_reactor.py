'''
@author: balep, stewryan, ethan-fowler

Copyright 2024, Battelle Energy Alliance, LLC, ALL RIGHTS RESERVED
'''

import kugelpy.kugelpy.kugelpy.pebble_bed_reactor as pbr
from os import remove, path
from kugelpy.kugelpy.mutineer.testutils import gen_tmp_folder

#===============================================================================
# Shared objects
#===============================================================================
# Paths.
main_dir = path.dirname(path.realpath(__file__))
ifiles_dir = path.join(main_dir, 'testfiles')
distfile_path = path.join(ifiles_dir, 'dist.txt')
main_tests_dir = path.join(main_dir, '_tmp/')
gen_tmp_folder(main_tests_dir)

def test_init(regtest):
    pbr_instance = pbr.PebbleBedReactor(cavity_height=100)
    print(vars(pbr_instance))
    print(vars(pbr_instance), file=regtest)

def test_build_block(regtest):
    pbr_instance = pbr.PebbleBedReactor()
    pbr_instance.build_block(1, 0.0)
    print(pbr_instance._block_dict, file=regtest)

def test_build_all_blocks(regtest):
    pbr_instance = pbr.PebbleBedReactor()
    pbr_instance.build_all_blocks()
    print(pbr_instance._block_dict, file=regtest)

def test_build_pbr_core(regtest):
    pbr_instance = pbr.PebbleBedReactor()
    pbr_instance.build_pbr_core()
    print(pbr_instance._block_dict, file=regtest)
    print(pbr_instance._reactor_dict, file=regtest)

def test_build_cylinder_surface(regtest):
    pbr_instance = pbr.PebbleBedReactor()
    cylv = pbr_instance.build_cylinder_surface('surf_1', 'cylv', 40, u=1, v=1, w=1)
    print(cylv, file=regtest)
    cylz = pbr_instance.build_cylinder_surface('surf_1', 'cylz', 40, lower_height=10, upper_height=2)
    print(cylz, file=regtest)
    cyly = pbr_instance.build_cylinder_surface('surf_1', 'cyly', 40, x_offset=10, y_offset=2, z_offset=5)
    print(cyly, file=regtest)
    cylx = pbr_instance.build_cylinder_surface('surf_1', 'cylx', 40, x_offset=10, y_offset=2, z_offset=5)
    print(cylx, file=regtest)

def test_build_conus(regtest):
    pbr_instance = pbr.PebbleBedReactor()
    pbr_instance.build_conus()
    print(pbr_instance._reactor_dict, file=regtest)

def test_build_outlet_plenum(regtest):
    pbr_instance = pbr.PebbleBedReactor()
    pbr_instance.build_outlet_plenum()
    print(pbr_instance._reactor_dict, file=regtest)

def test_build_outlet_channel(regtest):
    pbr_instance = pbr.PebbleBedReactor()
    pbr_instance.build_outlet_channel()
    print(pbr_instance._reactor_dict, file=regtest)

def test_build_pebble_shoot(regtest):
    pbr_instance = pbr.PebbleBedReactor()
    pbr_instance.build_pebble_shoot()
    print(pbr_instance._reactor_dict, file=regtest)

def test_build_bottom_reflector(regtest):
    pbr_instance = pbr.PebbleBedReactor()
    pbr_instance.build_bottom_reflector()
    print(pbr_instance._reactor_dict, file=regtest)

def test_build_pebble_bed(regtest):
    pbr_instance = pbr.PebbleBedReactor()
    pbr_instance.build_pebble_bed()
    print(pbr_instance._reactor_dict, file=regtest)

def test_build_pebble(regtest):
    pbr_instance = pbr.PebbleBedReactor()
    pbr_instance.build_pebble()
    print(pbr_instance._reactor_dict, file=regtest)

def test_build_outside(regtest):
    pbr_instance = pbr.PebbleBedReactor()
    pbr_instance.build_outside()
    print(pbr_instance._reactor_dict, file=regtest)

def test_build_cavity(regtest):
    pbr_instance = pbr.PebbleBedReactor()
    pbr_instance.build_cavity()
    print(pbr_instance._reactor_dict, file=regtest)

def test_build_top_reflector(regtest):
    pbr_instance = pbr.PebbleBedReactor()
    pbr_instance.build_top_reflector()
    print(pbr_instance._reactor_dict, file=regtest)

def test_build_cell(regtest):
    pbr_instance = pbr.PebbleBedReactor()
    cyl = pbr_instance.build_cell('cell1', 'univ1', 'material', ['surf_0', 'surf_2'], outside_surfaces=['surf_5', 'surf_6'], outside_cells=['cell_0', 'cell_2'] )
    print(cyl, file=regtest)

def test_build_filled_cell(regtest):
    pbr_instance = pbr.PebbleBedReactor()
    cyl = pbr_instance.build_filled_cell('cell1', 'univ1', 'material', ['surf_0', 'surf_2'], outside_surfaces=['surf_5', 'surf_6'], outside_cells=['cell_0', 'cell_2'] )
    print(cyl, file=regtest)

def test_build_universe(regtest):
    pbr_instance = pbr.PebbleBedReactor()
    cyl = pbr_instance.build_universe('cellu1',  inside_surfaces=['surf_0', 'surf_2'], outside_surfaces=['surf_5', 'surf_6'], outside_cells=['cell_0', 'cell_2'] )
    print(cyl, file=regtest)

def test_convert_theta_to_uv(regtest):
    pbr_instance = pbr.PebbleBedReactor()
    theta = pbr_instance.convert_theta_to_uv(0.0, r=50)
    print(theta, file=regtest)

def test_build_block_surfaces(regtest):
    pbr_instance = pbr.PebbleBedReactor()
    surf = pbr_instance.build_block_surface(1, 2, 4, 0, 30, x_offset=1.0, y_offset=12.0)
    print(surf, file=regtest)

def test_build_dimple_surfaces(regtest):
    pbr_instance = pbr.PebbleBedReactor()
    dimple = pbr_instance.build_dimple_surfaces(1, 3, 0, 15, x_offset= 1.0, y_offset=-10.0)
    print(dimple, file=regtest)

def test_build_rod_surfaces(regtest):
    pbr_instance = pbr.PebbleBedReactor()
    rod = pbr_instance.build_rod_surfaces(10, 10, 3, 10, 'cr', 0.0, 100.0)
    print(rod, file=regtest)

def test_build_block_cell(regtest):
    pbr_instance = pbr.PebbleBedReactor()
    cell = pbr_instance.build_block_cell(1, surfaces_to_skip=['surf1', 'surf2'], cells_to_skip=['cell1', 'cell2'])
    print(cell, file=regtest)

def test_build_dimple_cells(regtest):
    pbr_instance = pbr.PebbleBedReactor()
    dimple = pbr_instance.build_dimple_cells('test', 1)
    print(dimple, file=regtest)

def test_build_rod_cells(regtest):
    pbr_instance = pbr.PebbleBedReactor()
    rod_cells =  pbr_instance.build_rod_cells('test', 'cr', 'control', surfaces_to_skip=['sruf1', 'surf2'], cells_to_skip=['cell1', 'cell2'])
    print(rod_cells, file=regtest)

def test_block_universe(regtest):
    pbr_instance = pbr.PebbleBedReactor()
    rod_cells =  pbr_instance.build_block_universe('test', surfaces_to_skip=['sruf1', 'surf2'], cells_to_skip=['cell1', 'cell2'])
    print(rod_cells, file=regtest)

def test_build_dimple_universes(regtest):
    pbr_instance = pbr.PebbleBedReactor()
    dimple_cells =  pbr_instance.build_dimple_universes('test', 1)
    print(dimple_cells, file=regtest)

def test_build_rod_universe(regtest):
    pbr_instance = pbr.PebbleBedReactor()
    rod_univ =  pbr_instance.build_rod_universe('test', 'cr', surfaces_to_skip=['sruf1', 'surf2'], cells_to_skip=['cell1', 'cell2'])
    print(rod_univ, file=regtest)

def test_build_pbr_core(regtest):
    pbr_instance = pbr.PebbleBedReactor(output_dir=main_tests_dir)
    pbr_instance.build_pbr_core()
    pbr_instance.write_pbr_core()
    file_ = open(path.join(main_tests_dir, 'pbr_structure.inp'), 'r')
    print([x for x in file_], file=regtest)

def test_build_pbr_core_no_dimples(regtest):
    pbr_instance = pbr.PebbleBedReactor(output_dir=main_tests_dir, create_dimples=False)
    pbr_instance.build_pbr_core()
    pbr_instance.write_pbr_core()
    file_ = open(path.join(main_tests_dir, 'pbr_structure.inp'), 'r')
    print([x for x in file_], file=regtest)

def test_build_pbr_core_simple(regtest):
    pbr_instance = pbr.PebbleBedReactor(output_dir=main_tests_dir, simple_core=True)
    pbr_instance.build_pbr_core()
    pbr_instance.write_pbr_core()
    file_ = open(path.join(main_tests_dir, 'pbr_structure.inp'), 'r')
    print([x for x in file_], file=regtest)    
