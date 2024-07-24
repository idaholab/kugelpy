'''
@authors: balep, stewryan, ethan-fowler

Copyright 2024, Battelle Energy Alliance, LLC, ALL RIGHTS RESERVED
'''

import math
from kugelpy.kugelpy.sea_serpent.reactor import SerpentReactor
import os

class PebbleBedReactor(SerpentReactor):
    
    def __init__(self, **kwargs):
        
        super().__init__()

        self.pebble_bed_name = 'pf61_Step1.pbed'
        self.core_file_name = 'pbr_structure.inp'
        self.output_dir = ''
        
        self._block_material = 'reflector'
        self._pebble_shoot_material = 'pebble_shoot'
        self._outlet_plenum_material = 'outlet_plenum'
        self._outlet_channel_material = 'outlet_channel'
        self._safety_rod_material = 'safety_rod'
        self._control_rod_material = 'control_rod'
        self._cavity_material = 'helium'
        self.riser_material = 'helium'
        self._control_rod_cavity_material = 'helium'
        self.create_dimples = True
        self.simple_core = False

        # lower conus details, note that the conus height is 
        self.conus_height = 70.772 # this is the height of the cone to create a conus of 55.438 cm
        self.conus_z_offset = 0
        self.conus_channel_height = 85.438 # Note, the conus channel is the total height of the conus plus 30 cm of height
        
        # pebble chute details
        self.pebble_shoot_radius = 26.0
        self.pebble_chute_height = 185.1

        # Heights for the lower reflector and outlet plenum
        self.bottom_reflector_height = 58.4
        self.outlet_plenum_height = 96.7

       # control rod insertion depth and radius information
        self.cr_insertion_depth = 0.0
        self.sr_insertion_depth = -25.0
        self.radius_to_cr_center = 133
        self.control_rod_radius = 6.25
        self.control_rod_cavity_radius = 6.5

        # riser radius information
        self.radius_to_riser_center = 178.5
        self.riser_radius = 8.5

        # cavity and top reflector height information
        self.cavity_height = 45.8
        self.top_reflector_height = 86.0
        
        # Basic pebble information 
        self.pebble_inner_radius = 2.5
        self.pebble_outer_radius = 3.0

        # core and dimple information
        self.pebble_bed_height = 893.0        
        self.dimple_axial_offset = 20.5
        self.dimple_radius = 17.5
        self.dimple_depth = 3.0
        self.num_dimples = 12      
        self.block_inner_radius = 120.0
        self.block_outer_radius = 206.6
        self.pebble_bed_dimple_radius = self.block_inner_radius + self.dimple_radius
        
        self.number_of_blocks = 18
        self._block_dict = {}
        self._reactor_dict = {}
        self._block_angle = 360 / self.number_of_blocks
        # We added the 90 degree rotation to align with the pebble model generated from ProjectChrono
        self._block_angles = [self._block_angle * block_num + 90 for block_num in range(self.number_of_blocks)]    
        for k,v in kwargs.items():
            setattr(self, k, v)

        if self.simple_core:
            self.conus_height = 0.0
            self.conus_channel_height = 0.0
            self.outlet_plenum_height = 0.0
            self.cavity_height = 0.0

        self.__init__heights()
        
    def __init__heights(self):
        self.lower_model_height = -(self.bottom_reflector_height + self.conus_channel_height + self.outlet_plenum_height)

        self.bottom_reflector_lower_height = self.lower_model_height
        self.bottom_reflector_upper_height = self.bottom_reflector_lower_height + self.bottom_reflector_height
        
        self.outlet_plenum_lower_height = self.bottom_reflector_upper_height
        self.outlet_plenum_upper_height = self.outlet_plenum_lower_height + self.outlet_plenum_height    
        
        self.outlet_channel_lower_height = self.outlet_plenum_upper_height
        self.outlet_channel_upper_height = self.outlet_channel_lower_height + self.conus_channel_height
        
        self.pebble_shoot_lower_height = self.lower_model_height
        self.pebble_shoot_upper_height = self.pebble_shoot_lower_height + self.pebble_chute_height     
        
        self.pebble_bed_lower_height = self.outlet_channel_upper_height
        self.pebble_bed_upper_height = self.pebble_bed_lower_height + self.pebble_bed_height
        
        self.cavity_lower_height = self.pebble_bed_upper_height
        self.cavity_upper_height = self.cavity_lower_height + self.cavity_height
        
        self.top_reflector_lower_height = self.cavity_upper_height
        self.top_reflector_upper_height = self.top_reflector_lower_height + self.top_reflector_height    
        
        self.model_upper_height = self.top_reflector_upper_height
        
        self.control_rod_lower_height = self.pebble_bed_lower_height
        self.control_rod_upper_height = self.model_upper_height

        self.riser_lower_height = self.pebble_bed_lower_height
        self.riser_upper_height = self.cavity_upper_height
    
    def build_block(self, block_id, angle):
        """
        Collection of function required to build a reflector block.
        """
        self._block_dict[block_id] = {'surfaces': {'block': '', 'dimples': '', 'control_rods': '', 'risers': ''},
                                     'cells': {'block': '', 'dimples': '', 'control_rods': '', 'risers': ''},
                                     'universes': {'block': '', 'dimples': '', 'control_rods': '', 'risers': ''},}
        
        surfaces_to_skip = []
        cells_to_skip = []
        self._block_dict[block_id]['surfaces']['block'] = self.build_block_surface(block_id, self.block_inner_radius, self.block_outer_radius, angle, angle+self._block_angle)
        
        if self.create_dimples:
            dimple_surface_names, dimple_surfaces = self.build_dimple_surfaces(block_id, self.dimple_radius, angle, self.num_dimples)
            self._block_dict[block_id]['surfaces']['dimples'] = dimple_surfaces
            dimple_cell_names, dimple_cells = self.build_dimple_cells(block_id,self.num_dimples)
            self._block_dict[block_id]['cells']['dimples'] = dimple_cells
            self._block_dict[block_id]['universes']['dimples'] = self.build_dimple_universes(block_id,self.num_dimples)
            cells_to_skip += dimple_cell_names
        
        if not self.simple_core:
            # Grab all of the surfaces, cells, and universes for the safety and control rods
            rod_type = 'cr' if block_id % 2 == 0 else 'sr'
            cr_insertion_depth = self.cr_insertion_depth if rod_type == 'cr' else self.sr_insertion_depth
            rod_material = self._control_rod_material if rod_type == 'cr' else self._safety_rod_material
            control_rod_surface_names, control_rod_surfaces = self.build_rod_surfaces(block_id, self.radius_to_cr_center, self.control_rod_radius, angle, rod_type, self.pebble_bed_upper_height - cr_insertion_depth, self.control_rod_upper_height)
            self._block_dict[block_id]['surfaces']['control_rod'] = control_rod_surfaces
            control_rod_cell_names, control_rod_cells = self.build_rod_cells(block_id, rod_type, rod_material)
            self._block_dict[block_id]['cells']['control_rod'] = control_rod_cells
            self._block_dict[block_id]['universes']['control'] = self.build_rod_universe(block_id, rod_type)
            cells_to_skip += control_rod_cell_names        

            control_rod_cavity_surface_names, control_rod_cavity_surfaces = self.build_rod_surfaces(block_id, self.radius_to_cr_center, self.control_rod_cavity_radius, angle, 'cr_cavity', self.control_rod_lower_height, self.control_rod_upper_height)
            self._block_dict[block_id]['surfaces']['control_rod_cavity'] = control_rod_cavity_surfaces
            control_rod_cavity_cell_names, control_rod_cavity_cells = self.build_rod_cells(block_id, 'cr_cavity', self._cavity_material, cells_to_skip=control_rod_cell_names)
            self._block_dict[block_id]['cells']['control_rod_cavity'] = control_rod_cavity_cells
            self._block_dict[block_id]['universes']['control_rod_cavity'] = self.build_rod_universe(block_id, 'cr_cavity',cells_to_skip=control_rod_cell_names)
            cells_to_skip += control_rod_cavity_cell_names        

            # Grab all of the surfaces, cells, and universes for the risers
            rod_type = 'riser'
            risers_surface_names, risers_surfaces = self.build_rod_surfaces(block_id, self.radius_to_riser_center, self.riser_radius, angle, rod_type, self.riser_lower_height, self.riser_upper_height)
            self._block_dict[block_id]['surfaces']['risers'] = risers_surfaces
            risers_cell_names, risers_cells = self.build_rod_cells(block_id, rod_type, self.riser_material)
            self._block_dict[block_id]['cells']['risers'] = risers_cells
            self._block_dict[block_id]['universes']['risers'] = self.build_rod_universe(block_id, rod_type)
            cells_to_skip += risers_cell_names  
        
        self._block_dict[block_id]['cells']['block'] = self.build_block_cell(block_id,surfaces_to_skip=surfaces_to_skip,
                                                                           cells_to_skip=cells_to_skip)
        self._block_dict[block_id]['universes']['block'] = self.build_block_universe(block_id,surfaces_to_skip=surfaces_to_skip,
                                                                                       cells_to_skip=cells_to_skip)

    def build_all_blocks(self):
        # Grab all of the surfaces, cells, and universes for the dimples
        if self.create_dimples:
            self._reactor_dict['dimples'] = {'surface': self.build_cylinder_surface('inner_dimple', 'cylz', self.block_inner_radius, lower_height=self.pebble_bed_lower_height, upper_height=self.pebble_bed_upper_height)}
            self._reactor_dict['dimples']['surface'] += self.build_cylinder_surface('outer_dimple', 'cylz', self.block_inner_radius + self.dimple_depth, lower_height=self.pebble_bed_lower_height, upper_height=self.pebble_bed_upper_height) 

        for block_id, angle in enumerate(self._block_angles):
            self.build_block(block_id, angle)
    
    def build_pbr_core(self):
        if self.simple_core:
           self.build_bottom_reflector()
           self.build_all_blocks()
           self.build_pebble_bed()
           self.build_pebble()
           self.build_top_reflector()
           self.build_outside()         
        else:
            self.build_pebble_shoot()  
            self.build_conus(z_offset=self.conus_z_offset, radius=self.block_inner_radius, height=self.conus_height)
            self.build_outlet_plenum()
            self.build_outlet_channel()
            self.build_bottom_reflector()
            self.build_all_blocks()
            self.build_pebble_bed()
            self.build_pebble()
            self.build_cavity()
            self.build_top_reflector()
            self.build_outside()
    
    def build_conus(self, surface_name='conus_s', x_offset=0.0, y_offset=0.0, z_offset=0.0, radius=0.0, height=0.0):
        surf = f'surf {surface_name} cone {x_offset} {y_offset} {z_offset} {radius} -{height}\n'
        surf += f'trans s conus_s rot 0.0 0.0  {z_offset}      0. 0. 1. 180.\n'
        surf += f'surf upper_cone pz {self.pebble_bed_lower_height}'
        self._reactor_dict['conus'] = {'surface': surf}
        self._reactor_dict['conus']['cells'] = self.build_filled_cell('cone_c', 'cone_u', 'pebble_bed', ['conus_s'])
        self._reactor_dict['conus']['universes'] = self.build_universe('cone_u', ['conus_s', 'upper_cone'], outside_surfaces=['pebble_shoot_s'])

    def build_outlet_plenum(self):
        surf = self.build_cylinder_surface('outlet_plenum_s', 'cylz', self.block_inner_radius, lower_height=self.outlet_plenum_lower_height, upper_height=self.outlet_plenum_upper_height)
        self._reactor_dict['outlet_plenum'] = {'surface': surf}
        self._reactor_dict['outlet_plenum']['cells'] = self.build_cell('outlet_plenum_c', 'outlet_plenum_u', self._outlet_plenum_material, ['outlet_plenum_s'], outside_surfaces=['pebble_shoot_s'])
        self._reactor_dict['outlet_plenum']['universes'] = self.build_universe('outlet_plenum_u', ['outlet_plenum_s'], outside_surfaces=['pebble_shoot_s'])
        
    def build_outlet_channel(self):
        surf = self.build_cylinder_surface('outlet_channel_s', 'cylz', self.block_inner_radius, lower_height=self.outlet_channel_lower_height, upper_height=self.outlet_channel_upper_height)
        self._reactor_dict['outlet_channel'] = {'surface': surf}
        self._reactor_dict['outlet_channel']['cells'] = self.build_cell('outlet_channel_c', 'outlet_channel_u', self._outlet_channel_material, ['outlet_channel_s'], outside_surfaces=['pebble_shoot_s', 'conus_s'])
        self._reactor_dict['outlet_channel']['universes'] = self.build_universe('outlet_channel_u', ['outlet_channel_s'], outside_surfaces=['pebble_shoot_s', 'conus_s'])

    def build_pebble_shoot(self):
        surf = self.build_cylinder_surface('pebble_shoot_s', 'cylz', self.pebble_shoot_radius , lower_height=self.pebble_shoot_lower_height, upper_height=self.pebble_shoot_upper_height)
        self._reactor_dict['pebble_shoot'] = {'surface': surf}
        #self._reactor_dict['pebble_shoot']['cells'] = self.build_filled_cell('pebble_shoot_c', 'pebble_shoot_u', 'pebble_bed', ['pebble_shoot_s'])
        self._reactor_dict['pebble_shoot']['cells'] = self.build_cell('pebble_shoot_c', 'pebble_shoot_u', self._pebble_shoot_material, ['pebble_shoot_s'])
        self._reactor_dict['pebble_shoot']['universes'] = self.build_universe('pebble_shoot_u', ['pebble_shoot_s'])

    def build_bottom_reflector(self):
        pebble_shoot_surface = '' if self.simple_core else 'pebble_shoot_s'
        surf = self.build_cylinder_surface('bottom_reflector_s', 'cylz', self.block_inner_radius, lower_height=self.bottom_reflector_lower_height, upper_height=self.bottom_reflector_upper_height)
        self._reactor_dict['bottom_reflector'] = {'surface': surf}
        self._reactor_dict['bottom_reflector']['cells'] = self.build_cell('bottom_reflector_c', 'bottom_reflector_u', self._block_material, ['bottom_reflector_s'], outside_surfaces=[pebble_shoot_surface])
        self._reactor_dict['bottom_reflector']['universes'] = self.build_universe('bottom_reflector_u', ['bottom_reflector_s'], outside_surfaces=[pebble_shoot_surface])
        
    def build_pebble_bed(self):
        surf  = 'surf inf_surf inf\n'
        surf += f'pbed pebble_bed helium_u "{self.pebble_bed_name}" pow\n' 
        surf += self.build_cylinder_surface('pebbles_s', 'cylz', self.block_inner_radius, lower_height=self.pebble_bed_lower_height, upper_height=self.pebble_bed_upper_height)
        self._reactor_dict['pebble_bed'] = {'surface': surf}
        self._reactor_dict['pebble_bed']['cells'] = 'cell c_he helium_u helium  -inf_surf\n'
        self._reactor_dict['pebble_bed']['cells'] += self.build_filled_cell('pebbles_c', 'pebbles_u', 'pebble_bed', ['pebbles_s'])
        self._reactor_dict['pebble_bed']['universes'] = self.build_universe('pebbles_u', ['pebbles_s'])
        
    def build_pebble(self):
        surf = f'surf pebble_inner sph 0. 0. 0. {self.pebble_inner_radius}\n'
        surf += f'surf pebble_outer sph 0. 0. 0. {self.pebble_outer_radius}\n'
        self._reactor_dict['pebble'] = {'surface': surf}
        
    def build_outside(self):
        self._reactor_dict['outside'] = {'surface': self.build_cylinder_surface('outside_s', 'cylz', self.block_outer_radius, self.bottom_reflector_lower_height, self.model_upper_height)}
        self._reactor_dict['outside']['universe'] = 'cell out        0 outside            outside_s'
        
    def build_cavity(self):
        self._reactor_dict['cavity'] = {'surface':self.build_cylinder_surface('cavity_s', 'cylz', self.block_inner_radius, self.cavity_lower_height, self.cavity_upper_height)} 
        self._reactor_dict['cavity']['cells'] = self.build_cell('cavity_c', 'cavity_u', self._cavity_material, ['cavity_s'])
        self._reactor_dict['cavity']['universes'] = self.build_universe('cavity_u', ['cavity_s'])
        
    def build_top_reflector(self):
        self._reactor_dict['top_reflector'] = {'surface':self.build_cylinder_surface('top_reflector_s', 'cylz', self.block_inner_radius, self.top_reflector_lower_height, self.top_reflector_upper_height)} 
        self._reactor_dict['top_reflector']['cells'] = self.build_cell('top_reflector_c', 'top_reflector_u', self._block_material, ['top_reflector_s'])
        self._reactor_dict['top_reflector']['universes'] = self.build_universe('top_reflector_u', ['top_reflector_s'])
            
    def build_block_surface(sefl, id_, ir_, or_, ang1, ang2, x_offset=0.0, y_offset=0.0):
        return f'surf block_{id_}_s  pad {x_offset} {y_offset} {ir_} {or_} {ang1} {ang2}\n'
        
    def build_dimple_surfaces(self, id_, dr_, ang, num_dimples, x_offset=0.0, y_offset=0.0):
        # 7.0 is the dimple off set
        base_height = self.dimple_axial_offset + self.pebble_bed_lower_height + self.dimple_radius if id_ % 2 == 0 else self.pebble_bed_lower_height + self.dimple_radius * 4
        u, v = self.convert_theta_to_uv(math.radians(ang+100))
        dimple = f'surf block_{id_}_plane plane {u} {v}\n'
        dimple_surfaces = []
        for num in range(num_dimples):
            z_offset=base_height + num * dr_ * 4
            dimple += self.build_cylinder_surface(f'block_{id_}_d{num}_s', 'cylv', dr_, x_offset=x_offset, y_offset=y_offset, z_offset=z_offset, u=u, v=v, w=0.0)
            dimple_surfaces.append(f'block_{id_}_d{num}_s')
        return dimple_surfaces, dimple
        
    def build_rod_surfaces(self, id_, r2c, or_, ang, rod_type, lh, uh):
        u, v = self.convert_theta_to_uv(math.radians(ang+100), r=r2c)    
        return f'block_{id_}_{rod_type}_s', self.build_cylinder_surface(f'block_{id_}_{rod_type}_s', 'cylz', or_, x_offset=u, y_offset=v,  lower_height=lh, upper_height=uh)
        
    def build_block_cell(self, id_, surfaces_to_skip=[], cells_to_skip=[]):
        surfaces_to_skip_str = ' '.join(surf for surf in surfaces_to_skip)
        cells_to_skip_str = '#' + ' #'.join(surf for surf in cells_to_skip) if len(cells_to_skip)>0 else ''
    
        return f'cell block_{id_}_c block_{id_}_u {self._block_material} -block_{id_}_s {surfaces_to_skip_str} {cells_to_skip_str}'
    
    def build_dimple_cells(self, block_id, num):
        cell = ''
        dimple_cells = []
        for num in range(num):
            cell += f'cell block_{block_id}_d{num}_c pebbles_u fill pebble_bed -block_{block_id}_d{num}_s -outer_dimple inner_dimple block_{block_id}_plane\n'   
            dimple_cells.append(f'block_{block_id}_d{num}_c')
        return dimple_cells, cell
    
    def build_rod_cells(self, block_id, rod_type, material, surfaces_to_skip=[], cells_to_skip=[]):
        surfaces_to_skip_str = ' '.join(surf for surf in surfaces_to_skip)
        cells_to_skip_str = '' if cells_to_skip == [] else '#' + ' #'.join(surf for surf in cells_to_skip)
        cell_str = f'cell block_{block_id}_{rod_type}_c block_{block_id}_{rod_type}_u {material} -block_{block_id}_{rod_type}_s {surfaces_to_skip_str}  {cells_to_skip_str}'
        cell = [f'block_{block_id}_{rod_type}_c']
        return cell, cell_str
        
    def build_block_universe(self, id_, surfaces_to_skip=[], cells_to_skip=[]):
        surfaces_to_skip_str = ' '.join(surf for surf in surfaces_to_skip)
        cells_to_skip_str = '#' + ' #'.join(surf for surf in cells_to_skip) if len(cells_to_skip)>0 else ''
        return f'cell block_{id_}_u 0 fill block_{id_}_u -block_{id_}_s {surfaces_to_skip_str} {cells_to_skip_str}'
    
    def build_dimple_universes(self, block_id, num):
        cell = ''
        for num in range(num):
            cell += f'cell block_{block_id}_d{num}_u 0 fill pebbles_u -block_{block_id}_d{num}_s -outer_dimple inner_dimple block_{block_id}_plane\n'   
        return cell
    
    def build_rod_universe(self, block_id, rod_type, surfaces_to_skip=[], cells_to_skip=[]):
        surfaces_to_skip_str = ' '.join(surf for surf in surfaces_to_skip)
        cells_to_skip_str = '' if cells_to_skip == [] else '#' + ' #'.join(surf for surf in cells_to_skip)
        cell = f'cell block_{block_id}_{rod_type}_u 0 fill block_{block_id}_{rod_type}_u -block_{block_id}_{rod_type}_s {surfaces_to_skip_str}  {cells_to_skip_str}'
        return cell
    
    def write_pbr_core(self):
        core_input = os.path.join(self.output_dir,self.core_file_name)

        f = open(core_input, 'w')
        for block_id, block in self._block_dict.items():
            for print_type, region in block.items():
                f.write(f'\n\n%%%%%%%%%%%%%%%%%%%%% Block {block_id} {print_type} %%%%%%%%%%%%%%%%%%%%%\n\n')
                for region_name, region_print in region.items():
                    f.write(f'\n\n%%%%%%%%%%%%%%%%%%%%% Block {block_id} {print_type} {region_name} %%%%%%%%%%%%%%%%%%%%%\n\n')
                    f.write(region_print)

        for region_name, region in self._reactor_dict.items():
            for print_type, region in region.items():
                f.write(f'\n\n%%%%%%%%%%%%%%%%%%%%% {region_name} {print_type} %%%%%%%%%%%%%%%%%%%%%\n\n')
                f.write(region)