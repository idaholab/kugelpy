Copyright 2024, Battelle Energy Alliance, LLC, ALL RIGHTS RESERVED
### Inheritance
- PebbleSorter inherits from SerpentReactor
- PebbleBedReactor inherits from SerpentReactor
- DiverterPebble inherits from Pebble
- FuelPebble inherits from Pebble

### The following variables are hard-coded to match materials found in `PebbleSorter.core_materials`. Changing material names here could break your model if the name is not also included in `PebbleSorter.core_materials`. ###
**PebbleBedReactor._block_material** : str, default: 'reflector' \
    Name of material, which can be found in `PebbleSorter.core_materials`, composing the reflector blocks. \
\
**PebbleBedReactor._pebble_shoot_material** : str, default: 'pebble_shoot' \
    Name of the homogenized material, which can be found in `PebbleSorter.core_materials`, composing the pebble chute region where burned fuel is removed from the core. \
\
**PebbleBedReactor._outlet_plenum_material** : str, default 'outlet_plenum' \
    Name of material, which can be found in `PebbleSorter.core_materials`, composing the outlet plenum where hot helium exits the core. \
\
**PebbleBedReactor._outlet_channel_material** : str, default: 'outlet_channel' \
    Name of material composing the outlet channel (see figure). \
\
**PebbleBedReactor._safety_rod_material** : str, default: 'safety_rod' \
    Name of material composing the safety rods/shutdown rods \
\
**PebbleBedReactor._control_rod_material** : str, default: 'control_rod' \
    Name of material composing the control rods \
\
**PebbleBedReactor._cavity_material** : str, default: 'helium' \
    Name of material filling reactor cavities (background universe for pebble bed geometry) \
\
**PebbleBedReactor._riser_material** : str, default: 'riser' \
    Name of material filling the helium riser region \
\
**PebbleBedReactor._control_rod_cavity_material** : str, default: 'helium' \
    Name of material filling the empty region(s) of the control rods 

### The following dictionaries are populated by the code using other parameters which can be set by the user. Attempting to edit these directories directly could have adverse effects. (Let's set these as private later)
**PebbleBedReactor._block_dict** : dict, default: {} \
    Contains information about the blocks used to define the radial reflector region. This parameter is generally changed using `build_block().` \
\
**PebbleBedReactor._reactor_dict** : f the build functions.  \
\
**SerpentReactor._detector_dict** : dict, default: {} \
    Internal variable which stores detector data and how to print the detectors in a Serpent input.

### Changing this value could result in gaps in the reflector or non-physical overlaps of blocks (set this as private)
**PebbleBedReactor._block_angle** : floatdict, default: {} \
    Contains information for most surfaces/cells that make up the reactor model. This parameter is changed using any o, default: 360 / number_of_blocks \
    Angle in degrees that a single block spans around the 'proper core' region.

### The following variables are automatically updated in the code and can be affected by changing other variables. Attempting to edit these variables directly could have adverse effects.
**PebbleSorter._pebble_array** : list, default: [] \
    3-D ordered array containing pebble information. Organized by channel (in to out), then volume (top to bottom), then individual pebble (top to bottom). This array is populated by `read_in_pebble_dist()`. \
\
**PebbleSorter._kernel_data** : dict, default: {} \
    Dictionary which holds geometry information for the fuel kernels in centimeters (cm). `setup_kernel()` sets up the fuel kernel data either using default values or by taking user inputs, `{'fuel': fuel_radius, 'buffer': buffer_radius, 'inner_pyc': inner_pyc_radius, 'sic': sic_radius, 'outer_pyc':  outer_pyc_radius, 'kernels_per_pebble': kernels_per_pebble}`. \
\
**PebbleSorter._unloaded_pebbles** : list, default: [] \
    Used to store pebbles (see kugelpy.kugelpy.pebble.Pebble) which will be unloaded during refueling/pebble shifting. \
\
**PebbleSorter._unloaded_fuel_pebbles** : list, default: [] \
    Used to store fueled pebbles (see kugelpy.kugelpy.pebble.Pebble) which will be unloaded during refueling/pebble shifting (takes from unloaded_pebbles). \
\
**PebbleSorter._burnup_materials** : dict, default: {} \
    Dictionary of burnup material for pebbles in their previous location. \
\
**PebbleSorter._efpd_tracker** : float, default: 0.0 \
    Keeps track of the number of 'effective full power days' of operation for the reactor \
\
**PebbleSorter._burnstep** : int, default: 0 \
    Tracks the step of the simulation/how many models have been run \
\
**PebbleSorter._power_days** : foat, default: 0.0 \
    Used to keep track of full power days (sum of current_efpd*power_level) 

### Variables required for Griffin/Pronghorn coupling
Note, by default Griffin/Pronghorn coupling is not allowed in kugelpy. Please contact the developers at INL for access to the appropriate modules for Griffin/Pronghorn coupling with kugelpy. \
**multiphysics_run** = False \
**path_to_micro_xs** = '' \
**path_to_moose_mesh** = '' \
**minimum_temperature_difference** = 50 \

### Limit imposed by Serpent
**PebbleSorter._atom_density_limit** : float, default: 1E-20 \
    Minimum atomic density in atoms/barns-cm allowed for materials to be included in burnup material. \
\

**PebbleSorter._path_to_data_files** : str, default: data_path \
    Path pointing to directory containing TRISO particle distribution and original pebble distribution (contained within kugelpyu/data). \
\

**PebbleSorter._homogenized_materials_dict** : dict, default: {} \
    Contains material definitions after they have been homogenized. This results in new materials which will be placed back in the core.  \
\

**(DiverterPebble or FuelPebble or PebbleSorter)._homogenization_group** : int, default: 0 \
    Index used to group pebbles together for burnup and homogenization. Handled in-code without user input. \
\
**PebbleSorter._pebble_number** : int, default: 0 \
    Used to track number of core passes a pebble has undergone. Handled in-code without user input. \
\
**PebbleSorter._step_pebble_distribution_file** : str, deafult: '' \
    Name of file where pebble information is stored after a completed run. Automatically updated during run-in simulation. \
\
**Pebble._pebble_type** : str, default: 'graphite' \
    Designation if this is a graphite or fuel pebble. \
\
**Pebble._inner_radius** : float, default: 2.5 \
    Inner radius of the pebble surrounding the graphite matrix [cm]. \
\
**Pebble._radius** : float, default: radius \
    Dictionary of the material in the pebble. Takes the form: {'material_name': {'ZAID1': float, 'ZAID2': float, ...}}. \
\
**Pebble._material** : dict, default: \
{'matrix':   {'6000': 9.22570E-2, '5010': 2.28336E-9, '5011': 9.24876E-9},\
'pebshell': {'6000': 6.61814E-2, '5010': 2.23273E-8,  '5011': 9.04368E-7}} \
    Dictionary of the geometry in the pebble. 
        Each entry describes a part of the geometry, where a given radius and number of instances are used to calculate the volume. Takes the form: {'geometry_name': {'radius': float, 'number_of_instances': int, 'volume': float}}. \
\
**Pebble._x** : float, default: x \
    Current x position in the pebble bed. \
\
**Pebble._y** : float, default: y \
    Current y position in the pebble bed. \
\
**Pebble._z** : float, default: z \
    Current z position in the pebble bed. \
\
**Pebble._r** : float, default: r \
    Current radial position in the pebble bed. \
\
**Pebble._volume_num** : int, default: volume \
    Integer representation the volume region the pebble is in. \
\
**Pebble._channel_num** : int, default: channel \
    Integer representation the channel the pebble is in. \
\
**Pebble._mesh_location** = f'c{channel}v{volume}' \
    Combination of channel, and volume for where the pebble is. \
\
**Pebble._temperature** = temperature \
    Temperature of the pebble [K]. \
\
**Pebble._shuffled** : bool, default: False \
    Indicator if this is the first pass or Nth pass through the core. \
\
**Pebble._previous_universe** : str, default: '' \
    Concatinated string containing the previous universes the pebble was exposed to. If the pebble is homogenized after each pass, we default the previous universes to c0v0. \
\
**Pebble._burnup** : float, default: 0. \
    Burnup accrued during pebble movement [MWd/kg]. \
\
**Pebble._burnup_j_cm3** : float, default: 0. \
    Burnup accrued during pebble movement [J/cm3]. \
\
**Pebble._num_passes** : int, default: 0 \
    Number of passes a pebble has gone through the core. \
\
**Pebble._pass_limit** : int, default: pass_limit \
    Maximum number of times a pebble can go through the core before being discarded. \
\
**Pebble._pebble_number** : int, default: pebble_number
    Integer related to the pebble number in the core. \
\
**Pebble._xs_dict** : dict, default \
{1500: {'graphite': 'grph1500', 'xs_set': '15c'}, \
1200: {'graphite': 'grph1200', 'xs_set': '12c'}, \
900: {'graphite':  'grph900', 'xs_set': '09c'}, \
600: {'graphite':  'grph600', 'xs_set': '06c'}, \
300: {'graphite':  'grph300', 'xs_set': '03c'},} \
    \
\
**Pebble._previous_universe** : str, default: 'g0_' + self.mesh_location \
    Tracks previous universe of pebble. \
\
**Pebble._xs_library** : dict, default: self.set_xs_set(self.temperature)[1] \
    Cross-section set and scattering library based on the temperature. \
\
**Pebble._scattering_library** : dict, default: self.set_xs_set(self.temperature)[1] \
    Cross-section set and scattering library based on the temperature. \
\

**Pebble._geometry** = 
{'matrix':    {'radius': self.inner_radius,    'number_of_instance': 1, 'volume': 0.0}, \
'pebshell':  {'radius': radius, 'number_of_instance': 1, 'volume': 0.0}}\
    m\
\
**FuelPebble._pebble_type** : str, default: 'fuel' \
    Designation if this is a graphite or fuel pebble. \
\
**FuelPebble._previous_universe** : str, default: f'f{self.homogenization_group}_' + self.mesh_location \
    Concatinated string containing the previous universes the pebble was exposed to. If the pebble is homogenized after each pass, we default the previous universes to c0v0. \
\
**FuelPebble._triso_volume** : float, default: 18687 * 0.0000402 \
    Volume of the fuel kernels in the pebble (required for correct burnup). \
\
**FuelPebble._power_days** : float, default: 0. \
    Number of megawatt days the pebbles has been in the core (days * power) [MWd]. \
\
**FuelPebble._power_density** : float, default: 0. \
    Current power density for the pebble (this is the power density for all pebbles of the same fuel type, same pass number, and in the same core location) [MW] \
\
**FuelPebble._xs_fuel_library** : dict, default: self.set_xs_set(self.lial2_temperature)[0] \
    Dictinary storing cross sections for the fuel at the current temperature. \
\
**FuelPebble._fuel_scattering_library** : dict, default: self.set_xs_set(self.lial2_temperature)[1] \
    Dictinary storing neutron scattering cross sections for the fuel at the current temperature. \
\
**FuelPebble._kernel_data** : dict, default:
kernel_data if kernel_data else {'fuel':0.02125, 'buffer':0.03125, 'inner_pyc':0.03525, 'sic':0.03875, 'outer_pyc':0.04275, 'kernels_per_pebble': 18687} \
    Geometry of TRISO particle in fuel pebble, contained in dictionary where layer name is paired with the outer radius of the layer. 'fuel' is at the center followed by 'buffer', 'inner_pyc', 'sic', and 'outer_pyc' in that order. Can be changed from default at instantiation. \
\
**FuelPebble._kernels_per_pebble** : int, default: self.kernel_data.pop('kernels_per_pebble') \
    Number of TRISO kernels per fuel pebble.\
\
**FuelPebble._material** : dict, default: \
{'fuel':      {'92235': 3.70100E-3, '92238': 1.99216E-2,  '8016': 3.37331E-1, '6000': 9.26006E-3, '5010': 1.87091E-8, '5011': 7.57813E-8},\
'buffer':    { '6000': 5.26466E-2,  '5010': 1.35512E-8,  '5011': 5.48894E-8},\
'inner_pyc': { '6000': 9.52653E-2,  '5010': 2.45213E-8,  '5011': 9.93236E-8},\
'sic':       {'14028': 4.43271E-2, '14029': 2.25082E-3, '14030': 1.48376E-3, '6000': 4.80616E-2,  '5010': 1.23711E-8,  '5011': 5.0109E-8}, \
'outer_pyc': { '6000': 9.52653E-2,  '5010': 2.45213E-8,  '5011': 9.93236E-8}, \
'matrix':    { '6000': 8.67416E-2,  '5010': 2.23273E-8,  '5011': 9.04368E-8}, \
'pebshell':  { '6000': 8.67416E-2,  '5010': 2.23273E-8,  '5011': 9.04368E-8}} \
    Material compositions for fuel pebble stored in a nested dictionary of the form {'material_name':{'ZAID':atomic_density, ...}, ...}.\
\         
**FuelPebble._fuel_temperature** : float, default: fuel_temperature \
    Averaged fuel kernel temperature. \
\
**FuelPebble._days_in_core** : int, default: 0
    Tracks how long the pebble has been in the core. \
\
**FuelPebble._geometry** : dict,  default: \
 {'fuel':      {'radius': self.kernel_data['fuel'],      'number_of_instance': self.kernels_per_pebble, 'volume': 0}, \
'buffer':    {'radius': self.kernel_data['buffer'],    'number_of_instance': self.kernels_per_pebble, 'volume': 0}, \
'inner_pyc': {'radius': self.kernel_data['inner_pyc'], 'number_of_instance': self.kernels_per_pebble, 'volume': 0}, \
'sic':       {'radius': self.kernel_data['sic'],       'number_of_instance': self.kernels_per_pebble, 'volume': 0}, \
'outer_pyc': {'radius': self.kernel_data['outer_pyc'], 'number_of_instance': self.kernels_per_pebble, 'volume': 0}, \
'matrix':    {'radius': self.inner_radius, 'number_of_instance': 1}, \
'pebshell':  {'radius': radius, 'number_of_instance': 1}} \
    Stores geometric information about the pebble as well as volumes of components of fueled pebbles used during homogenization. \
\