# parflow-python-example
This repo is an example of how to run the parflow python sdk (pftools) in a docker container. It contains a script for building the container, and a script for starting the container mounted to your hard drive so you can directly edit and run files on your computer.

# Building the repo
You will need to have docker installed and running. If you do not, follow these docs: https://docs.docker.com/

Once you have docker installed building the repo should be rather simple. If on unix, navigate to the top level folder here (parflow-python example) and run the command:
```
./bin/build_repo.sh
```
If you are on a windows machine you will want to run:
```
.\bin\build_repo.bat
```
If this was successful you should be able to open docker desktop and see an image with the name parflow/python_dev_environment

# Starting the dev container
Once you have built the image there is a script that will start a dev container configured to allow you to run python scripts with pftools. By default, this container will be mounted to wherever you run the script from. Once in, you will brought to the /data folder where you will be able to see and edit all of your local files. Note that the /data folder is not like a dream, IF YOU DELETE FILES HERE THEY GET DELETED IN REAL LIFE. The script is run via:
```
./bin/start_dev_container.sh
```
If you are unfamilar with docker you can think of the above as having logged you in to another computer with parflow already installed, except that that computer can also read and write to the folder you were in when you ran it.

Once in the dev container you can try running the parflow example via 
```
python3 main/PF_TiltedV_train.py
```
Afterwards you can see your output in main/TV-Ensemble-Training-InRange. Note you do not have to be in the container to do so, and can edit the python scripts without restarting the container. Also, this directory is in the gitignore, so you shouldn't have to worry about accidentally committing data. If you add more output locations I would recommend doing the same with them.

This script also accepts configuration of mount location, created container name, and image used:
```
./bin/start_dev_container.sh -i {IMAGE_NAME} -m {/PATH/TO/MOUNT} -c {CONTAINER_NAME}
```

This repo does not currently have a script to start a dev container for windows, but if you want to write one the important components are the volume mounted with the -v tag, and setting the container to use a utf-8 encoding so python can play nice and actually do file i/o (-e LANG=en_US.utf8).

