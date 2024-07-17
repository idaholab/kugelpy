

from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='kugelpy',
   version='0.1.0',
   description='Module use to model PBR run-in using Serpent monte carlo neutron transport',
   license="BSD-3",
   long_description=long_description,
   author='Ryan Stewart, Paulo Balestra',
   #author_email='foomail@foo.example',
   url="https://github.com/idaholab/kugelpy",
   packages=['kugelpy', 
             'kugelpy.mutineer', 
             'kugelpy.kugelpy',
             'kugelpy.sea_serpent'],  #same as name
   install_requires=['numpy', 'pandas', 'py', 'pytest', 'pytest-regtest', 'pytest-xdist', 'pyglet', 'matplotlib', 'scipy'], #external packages as dependencies
#    scripts=[
#             'kugelpy/first_mate/',
#             'kugelpy/kugelpy/',
#             'kugelpy/sea_serpent/',
#             #'kugelpy/tests',
#            ]
)