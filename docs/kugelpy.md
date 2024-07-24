Copyright 2024, Battelle Energy Alliance, LLC, ALL RIGHTS RESERVED
# `kugelpy`

`kugelpy` is a python module that performs time-dependent high-temperature gas-cooled pebble bed reactor (PBR) analysis. 
This process can simulate the run-in procedure for a PBR along with equilibrium analysis. 
The following notebook will describe how to create a `kugelpy` input and how to load previous `kugelpy` simulations to restart or examine the state of the reactor.

The examples are run using a pbs script, see an example [here](./kugelpy/kugelpy.pbs), feel free to use this script and update it for your work. 
Typically the script should be run on a high performance computing cluster (HPC), as the simulations are computationally expensive (reasonable results have been shown between 30-40 nodes with 48 processors each).
The python script has been annotated to provide clarity for the input script.

## Examples

[Multi-Pass Jump-In Simulation](./jump_in.md)

[Multi-Pass Run-In Simulation](./run_in.md)

[OTTO Jump-In Simulation](./otto.md)

[Multiphysics Run-In Simulation](./mp_run_in.md)

[Loading a Previous Simulation](./loader.md)

### Variables

#### Questions

If you have questions or need help with the `kugelpy` module, please direct questions to Ryan Stewart (ryan.stewart@inl.gov).