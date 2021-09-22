from parflow.tools.io import read_array_pfb
import matplotlib.pyplot as plot
import matplotlib.cm as cm
import os
import matplotlib.animation as manimation

RUN_DIRECTORY = "./main/TV-Ensemble-Training-InRange/00/"
RUN_NAME = "overland_tiltedV"
VARIABLE = "press"
OUTPUT_FILE = "tilted_v.mp4"

def get_files(directory, run_name, variable):
    PFB_FILE_EXTENSION = ".pfb"
    substring = f"{RUN_NAME}.out.{VARIABLE}"
    files = os.listdir(RUN_DIRECTORY)
    # filter out files of other variables
    files = [file for file in files if substring in file]
    # filter out non-pfb files
    files = [file for file in files if file.endswith(PFB_FILE_EXTENSION)]
    files.sort()
    return files


def make_movie(frames):
    # Define the meta data for the movie
    FFMpegWriter = manimation.writers["ffmpeg"]
    metadata = dict(title="Movie Test", artist="Matplotlib",
                    comment="Your parflow output")
    writer = FFMpegWriter(fps=15, metadata=metadata)
    # Initialize the movie
    figure = plot.figure()
    axis = figure.add_subplot()
    # Update the frames for the movie
    with writer.saving(figure, "writer_test.mp4", 100):
        for frame in frames:
            axis.imshow(frame[0], interpolation="nearest", cmap=cm.Greys_r)
            writer.grab_frame()


files = get_files(RUN_DIRECTORY, RUN_NAME, VARIABLE)
frames = [read_array_pfb(f"{RUN_DIRECTORY}{file}") for file in files]
make_movie(frames)

