# parflow-python-container
This repo is an example of how to run the parflow python sdk (pftools) in a docker container. It contains a script for building the container, and a script for starting the container mounted to your hard drive so you can directly edit and run files on your computer.

# Building the repo
You will need to have docker installed and running. If you do not, follow these docs: https://docs.docker.com/

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
Once you have built the image there is a script that will start a dev container configured to allow you to run python scripts with pftools. By default, this container will be mounted to wherever you run the script from. Once in, you will be brought to a folder where you will be able to see and edit all of the files that were in your local path when you ran the command. Note that this folder is not like a dream, IF YOU DELETE FILES HERE THEY GET DELETED IN REAL LIFE.

In order to more easily start the dev container anywhere you can alias the script to do so. Open your ~/.bashrc file or equivelent and add the line:
```
alias start_parflow_container="{PATH}/{TO}/parflow-python-container/bin/start_dev_container.sh"
```
Afterwards you will want to either restart your terminal or enter
```
source ~/.bashrc
```
Now you should be able to start the dev container anywhere by entering ```start_parflow_container```

If you are unfamilar with docker you can think of this as logging you in to another computer with parflow already installed, except that that computer can also read and write to the folder you were in when you ran it.

# Using/Testing the dev container
If you'd like to validate the dev container is working I recommend cloning the main repository: https://github.com/parflow/parflow

Once you've done that use open a terminal window and navigate to parflow/examples. Then enter 
```
start_parflow_container
```

Next make a folder for your output and navigate into it:
```
mkdir test_output && cd test_output
```
Now pick an example to run from the directory above e.g. ```tclsh ../default_richards.tcl 1 1 1```

Once the example has run exit the dev container by pressing ctrl+d and note the outputs are still available

This is the same workflow you would follow for your own development. In summary:
1) Navigate to the folder you want the dev container for
2) Start the dev container using ```start_parflow_container```
3) Run any parflow commands inside the container, but feel free to continue working on files in other editors.

The workflow for python scripts is the same you just run them with python instead of tclsh e.g.
```
python3 my_script.py
```
instead of 
```
tclsh ../default_richards.tcl 1 1 1
```

Lastly, if needed this script also accepts configuration of mount location, created container name, and image used:
```
start_parflow_container -i {IMAGE_NAME} -m {/PATH/TO/MOUNT} -c {CONTAINER_NAME}
```

This repo does not currently have a script to start a dev container for windows, but if you want to write one the important components are the volume mounted with the -v tag, and setting the container to use a utf-8 encoding so python can play nice and actually do file i/o (-e LANG=en_US.utf8).


# Adding python packages to the dev container
If you need to install new python packages in the dev container you can do so by simply adding the package name in the container_requirements.txt file. Note that whenever you add a new package you will need to rebuild the dev container (./bin/build_dev_container.sh) and restart it.

You can also install packages inside an already running container but if you do so they will not be there the next time you start it.

# Updating to the latest parflow version
By default when you rebuild the container it will not grab the latest parflow version (for performance reasons) but if you would like to update at any point simply run ```./force_update_dev_container.sh```

# What if I'm on windows?
I've included .bat files that should work, though only build_dev_container.bat has been tested. You should be able to follow the instructions subbing these in, though I'm not sure of how aliasing works on windows.

# Some TODOS
I (Ben West) have some of these on my radar. If one of these workflows would help you out let me know and I might be able to bump it up in terms of priority.
- Visualizing output from docker container. Would need to figure out how to connect the container to the computer display. Not a must because you can run scripts to visualize just fine outside of the container, and the section of pftools that does parflow specific file io doesn't require parflow to actually be working.
- Allowing jupyter notebook development inside of the container. This is also possible in theory, but requires some configuration.
- Easily allowing containers to be built for different environments such that you can manage dependencies individually across different projects



