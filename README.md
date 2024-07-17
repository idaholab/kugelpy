# Kugelpy (OpenSource)

The `kugelpy` modules are used to model and analyze run-in, jump-in, and operations of a pebble bed reactor (PBR).

### Current Submodules:

If new submodules are added please follow PEP8 naming conventions described below:

- **kugelpy**: module containing the function needed to perform monte carlo based run in calculations, approach to equilibrium, and time-dependent analysis  for pebble (kugel) bed reactors.
- **first_mate**: support module containing shared utilities required by the other modules.
- **sea_serpent**: module for helping generate `Serpent2` reactor input files

### Main Folder Files

- **docs**: markdown documentation.
- **examples**: main scripts and examples.
- **kugelpy**: code used to generate PBR models and tests to verify correct installation

### Naming Conventions:

The following conventions are used for comments and naming modules/packages:

- [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/#naming-conventionshttps://www.python.org/dev/peps/pep-0008/#naming-conventions)
- [numpydoc Style guide](https://numpydoc.readthedocs.io/en/latest/format.html)

#### Names to Avoid

Never use the characters ‘l’ (lowercase letter el), ‘O’ (uppercase letter oh), or ‘I’ (uppercase letter eye) as single character variable names.

In some fonts, these characters are indistinguishable from the numerals one and zero. When tempted to use ‘l’, use ‘L’ instead.

#### ASCII Compatibility
Identifiers used in the standard library must be ASCII compatible as described in the policy section of PEP 3131.

#### Package and Module Names
Modules should have short, all-lowercase names. Underscores can be used in the module name if it improves readability. Python packages should also have short, all-lowercase names, although the use of underscores is discouraged.

When an extension module written in C or C++ has an accompanying Python module that provides a higher level (e.g. more object oriented) interface, the C/C++ module has a leading underscore (e.g. _socket).

#### Class Names
Class names should normally use the CapWords convention.

The naming convention for functions may be used instead in cases where the interface is documented and used primarily as a callable.

Note that there is a separate convention for builtin names: most builtin names are single words (or two words run together), with the CapWords convention used only for exception names and builtin constants.

### Pip Installation

kugelpy is setup to enable pip installation. Ensure that pip is installed, then navigate to the base directory ```~/kugelpy/``` and run the following command in terminal

```
pip install .
```

You can then check to verify the installation by running

```
pip list 
```

and locating ```kugelpy```.

### Conda Installation

Use conda to install the packages used by the module:

```shell
conda config --add channels conda-forge
conda create --name kugelpy numpy pandas py pytest pytest-regtest pytest-xdist pyglet matplotlib scipy
conda activate kugelpy
```

Note: If you plan to use the `cartographer` module, you will also need to add the following:

```shell
conda config --add channels https://conda.software.inl.gov/public
conda install moose-pyhit
```

Then download this module in the `pymodules` directory:

```shell
mkdir $HOME/pymodules
cd $HOME/pymodules
git clone https://github.com/idaholab/kugelpy.git
cd kugelpy
```

To use the `kugelpy` module, you must add it's path to your .bash file using the following.

```shell
export PYTHONPATH="${PYTHONPATH}:$HOME/pymodules:$HOME/pymodules/kugelpy"
```

#### Docker
A Docker installation is available which eases environment setup and allows Windows users to run/develop kugelpy (certain kugelpy dependencies are only available for Mac and Linux). To run kugelpy from within a Linux Docker container:

 1. Make sure Docker is installed on your machine
 2. Navigate to the docker directory and run `docker-compose build` (builds the image, only needs to be ran once), `docker-compose up -d` (starts the container in detached mode), and `docker-compose exec kugelpy-dev /bin/bash` (executes an interactive Bash shell session inside the running container "kugelpy-dev")
 3. From within the newly created Bash shell, run `conda activate kugelpy` to activate the kugelpy conda environment, defined previously in the Dockerfile.

You now have a Dockerized python environment with all the packages required to run kugelpy - and this Docker container has access to your local kugelpy project clone (specified in the docker-compose.yml `volumes` declaration).

### Testing

To test the modules available in this repository run the following (note depending on the python version you may need to use `python -m pytest -vv` rather than `py.test -vv` for the following commands).

```shell
py.test -vv kugelpy/tests
```

To run specific tests (e.g. `test_file.py`) run the following command instead:

```shell
py.test -vv kugelpy/tests/test_file.py
```

To regenerate the `gold` files, the following command can be used:

```shell
py.test -vv --regtest-reset kugelpy/tests/test_file.py
```

To print the time needed by each test, the following command can be used:

```shell
py.test --durations=0 kugelpy/tests/test_file.py
```

#### Test markers
You can add markers to tests so that they only run when certain flags are used in the py.test run command. This has been implemented for some long running cartographer tests. For example, you can create a marker like this `longrun = pytest.mark.skipif("not config.getoption('--longrun')", reason="Only run when --longrun is given",)` and then place the marker on a specific test by adding `@longrun` to the line before the test definition. These tests marked `longrun` will be skipped by default; to run the test pass in the flag `--longrun`.

### General overview

sea_serpent.SerpentReactor:
    Handles basic Serpent input file parameters, detectors, geometry, and saving/running models.
kugelpy.Pebble:
    Class for holding information for an individual pebble including position, geometry, designation/type, pass number/burnup, etc.
kugelpy.Maelstream:
    Class to generate and or divide a pebble distribution in channels and
    volumes.
kugelpy.PebbleBedReactor:
    Creates pebble bed reactor geometry and writes geometry input files.
kugelpy.PebbleSorter:
    Generally used to perform run-in and jump-in. A large portion of this module is dedicated to tracking, sorting, and redistributing pebbles within a pebble bed reactor core but it also handles the creation of input files. PebbleSorter inherits from SerpentReactor and makes use of PebbleBedReactor and Maelstream, so developing the reactor model, reading in pebble and TRISO geometry, and performing run in can be done using only the PebbleSorter module.
mutineer.serpentutils:
    Provides methods for extracting data from Serpent output files.
mutineer.testutils:
    Variety of tools used for running test cases to ensure the code has been installed properly.
mutineer.logutils:

Kugelpy provides default values taken from the GPBR, but nearly all reactor parameters can be changed by passing variables through the PebbleSorter function call, as seen in docs/pbr_runin.md or docs/otto.md. Additionally, TRISO and pebble geometry can be changed so long as new input files are provided. 

PebbleSorter uses various power detectors to monitor pebbles as they pass through the core. These detectors are reset prior to each time step, so additional detectors must be stored in user_detector_dict by using PebbleSorter.create_user_detector(). These can be added to the reactor after the PebbleSorter object has been created. If an energy grid is desirable, one can be created using PebbleSorter.create_energy_grid() and passing the name of the energy grid to a user-made detector.

### Specific guides

* Utilizing [kugeply](docs/pbr_runin.md) for examining a run-in simulation.
* List of **kwargs [kugelpy](PATH TO TUTORIAL) for use in creating new reactor
