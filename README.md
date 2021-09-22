# parflow-python-example
This repo is an example of how to run the parflow python sdk (pftools) in a docker container. It contains a script for building the container, and a script for starting the container mounted to your hard drive so you can directly edit and run files on your computer.

# Building the repo
You will need to have docker installed and running. If you do not, follow these docs: https://docs.docker.com/

To do visualizations you will also need to have conda installed (we use it to grab some filewriter packages) https://www.anaconda.com/products/individual#Downloads

Once you have docker installed building the repo should be rather simple. If on unix, navigate to the top level folder here (parflow-python example) and run the command:
```
./bin/build_dev_container.sh
```
If you are on a windows machine you will want to run:
```
.\bin\build_dev_container.bat
```
If this was successful you should be able to open docker desktop and see an image with the name parflow/python_dev_environment

# Starting the dev container
Once you have built the image there is a script that will start a dev container configured to allow you to run python scripts with pftools. By default, this container will be mounted to wherever you run the script from. Once in, you will be brought to the /data folder where you will be able to see and edit all of the files that were in your local path when you ran the command. Note that the /data folder is not like a dream, IF YOU DELETE FILES HERE THEY GET DELETED IN REAL LIFE.

If you are unfamilar with docker you can think of this as logging you in to another computer with parflow already installed, except that that computer can also read and write to the folder you were in when you ran it.

The script is run via:
```
./bin/start_dev_container.sh
```

Once in the dev container you can try running the parflow example via 
```
python3 main/tilted_v/PF_TiltedV_train.py
```
Afterwards you should see your output in main/tilted_v/TV-Ensemble-Training-InRange. Note you do not have to be in the container to do so, and can edit the python scripts without restarting the container. Also, this directory is in the gitignore, so you shouldn't have to worry about accidentally committing data. If you add more output locations I would recommend doing the same with them.

This script also accepts configuration of mount location, created container name, and image used:
```
./bin/start_dev_container.sh -i {IMAGE_NAME} -m {/PATH/TO/MOUNT} -c {CONTAINER_NAME}
```

This repo does not currently have a script to start a dev container for windows, but if you want to write one the important components are the volume mounted with the -v tag, and setting the container to use a utf-8 encoding so python can play nice and actually do file i/o (-e LANG=en_US.utf8).

# Adding python packages to the dev container
If you need to install new python packages in the dev container you can do so by simply adding the package name in the requirements.txt file. Note that whenever you add a new package you will need to rebuild the dev container (./bin/build_dev_container.sh) and restart it.

You can also install packages inside an already running container but if you do so they will not be there the next time you start it.

# Using the visualization scripts
The visualization sceipts for now should be run on your computer and not in the container. If you want to use the ones that make movies you will need to have ffmpeg installed. My recommendation for mac would be to install homebew if you do not have it already (https://brew.sh/) and run:
```
brew install ffmpeg
```

You could also try installing it from their site https://www.ffmpeg.org/ but there is no guarentee it will be placed into a part of your path python knows about


