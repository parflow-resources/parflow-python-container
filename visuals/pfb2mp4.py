from parflow.tools.io import read_array_pfb
import matplotlib.pyplot as plot
import matplotlib.cm as cm
import os
import matplotlib.animation as manimation
import argparse, sys


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


def make_movie(frames, output_file):
    # Define the meta data for the movie
    FFMpegWriter = manimation.writers["ffmpeg"]
    metadata = dict(title="Movie Test", artist="Matplotlib",
                    comment="Your parflow output")
    writer = FFMpegWriter(fps=15, metadata=metadata)
    # Initialize the movie
    figure = plot.figure()
    # Update the frames for the movie
    with writer.saving(figure, f"./visuals/movies/{output_file}", 100):
        for frame in frames:
            plot.imshow(frame[0], interpolation="nearest", cmap=cm.Greys_r)
            plot.colorbar()
            writer.grab_frame()
            plot.clf()


def get_command_line_arguments():
    parser=argparse.ArgumentParser()

    parser.add_argument('--directory', help='The directory the run was output to')
    parser.add_argument('--run_name', help='The run name')
    parser.add_argument('--variable', help='The variable you want to plot e.g. press')
    parser.add_argument('--output_file', help='The name of the output file')

    return parser.parse_args()

args = get_command_line_arguments()

RUN_DIRECTORY = args.directory # "./main/tilted_v/TV-Ensemble-Training-InRange/00/"
RUN_NAME = args.run_name # "overland_tiltedV"
VARIABLE = args.variable # "press"
OUTPUT_FILE = args.output_file # "tilted_v.mp4"


files = get_files(RUN_DIRECTORY, RUN_NAME, VARIABLE)
frames = [read_array_pfb(f"{RUN_DIRECTORY}{file}") for file in files]
make_movie(frames, OUTPUT_FILE)

