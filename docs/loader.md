Copyright 2024, Battelle Energy Alliance, LLC, ALL RIGHTS RESERVED
## Loading a `kugely` Simulation

Often times we will will run a simulation to a specified point and then want to perform som perturbation after this point.
It would be convenient if we didn't have to rerun the entire first portion of the simulation since these calculations are computationally expensive.
`kugelpy` offers the ability to load simulations from a previously generated save point (note that the variable `keep_files` must be set to `True`; it is by default).
Below offers an exmaple of how to load a simulation from a specified statepoint.
Like the other examples, this is best run using the pbs script.

```python
import pyrates.kugelpy.pebble_sorter as psp
import numpy as np
import os.path as path

# we specify the path to the step we want to reload
# by default kugelpy will create a state point every 10 steps
path_ = path.join('run_in_simulation', 'step_10')

# we call the `loader` class function and tell it the path and step we want to load
ps = psp.PebbleSorter.loader(path_,10)

# it is best to set the `load_step` and `start_step` equal to the step we are loading
ps.load_step = 10
ps.start_step = 10

#after this we can set any other attribute associated with the pebble_sorter class
#for example, here we are setting the temperature of the fuel
ps.fuel_temperature = 1000

# Perform the run-in
ps.perform_run_in()
```