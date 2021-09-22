#!/bin/bash

docker build --tag parflow/python_dev_environment:latest .
conda install -c conda-forge ffmpeg
