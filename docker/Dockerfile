# Copyright 2024, Battelle Energy Alliance, LLC, ALL RIGHTS RESERVED

FROM continuumio/miniconda3:latest

WORKDIR /kugelpy

RUN conda config --add channels conda-forge
RUN conda config --add channels https://conda.software.inl.gov/public
RUN conda create --name kugelpy numpy pandas py pytest pytest-regtest pytest-xdist pyglet matplotlib qt lxml scipy shapely 

SHELL ["/bin/bash", "-c"]

# Set additional directories to be added to PYTHONPATH
ENV PYTHONPATH="${PYTHONPATH}:/kugelpy"

ENV PATH /opt/conda/envs/kugelpy/bin:$PATH

CMD ["conda", "run", "-n", "kugelpy", "/bin/bash"]
