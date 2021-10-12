
@echo off

docker run --rm -it --env=DISPLAY --name=parflow_dev -e LANG=en_US.utf8 -v %CD%:/data/  westb2/parflow:latest