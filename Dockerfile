#-----------------------------------------------------------------------------
# start by building the basic container
#-----------------------------------------------------------------------------
FROM parflow/parflow:latest
MAINTAINER Ben West <benjaminwest@email.arizona.edu>

#-----------------------------------------------------------------------------
# Set environment vars
#-----------------------------------------------------------------------------

ENV CMAKE_DIR /home/parflow/cmake-3.14.5-Linux-x86_64
ENV PARFLOW_DIR /usr/local
ENV SILO_DIR /home/parflow/silo-4.10.2
ENV HYPRE_DIR /home/parflow/hypre
ENV PATH $PATH:/usr/lib64/openmpi/bin:$CMAKE_DIR/bin:$PARFLOW_DIR/bin
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/usr/lib64/openmpi/lib
ENV PARFLOW_MPIEXEC_EXTRA_FLAGS "--mca mpi_yield_when_idle 1 --oversubscribe --allow-run-as-root"

WORKDIR /data

#-----------------------------------------------------------------------------
# Setup for running interacting with Parflow via python inside the docker
#-----------------------------------------------------------------------------

RUN apt-get -y update && apt-get -y install python3 && apt-get -y install zsh
COPY container_requirements.txt /opt/app/container_requirements.txt
WORKDIR /opt/app
RUN python3 -m pip install --upgrade pip && python3 -m pip install -r container_requirements.txt
COPY . /opt/app
WORKDIR /data


ENTRYPOINT ["zsh"]
