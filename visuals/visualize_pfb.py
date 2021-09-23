from parflow.tools.io import read_array_pfb
import matplotlib.pyplot as plot
import matplotlib.cm as cm
import argparse, sys
import seaborn


parser=argparse.ArgumentParser()
parser.add_argument('--file', help='The file to be visualized')
args = parser.parse_args()
data = read_array_pfb(args.file)

figure = plot.figure()
# axis = seaborn.heatmap(data[0])
plot.imshow(data[0], interpolation="nearest", cmap=cm.Greys_r)
plot.colorbar()
plot.show()