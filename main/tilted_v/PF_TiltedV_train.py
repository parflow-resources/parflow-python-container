# %%
import os
import pandas as pd
from parflow import Run
from parflow.tools.fs import cp, mkdir
from pathlib import Path
import numpy as np

# Helper function to link input directories
def link(src, dst):
  src_full = os.path.expandvars(src)
  dst_full = os.path.expandvars(dst)
  os.symlink(src_full, dst_full)

# %%
# -----------------------------------------------------------------------------
# Create ensemble settings
# -----------------------------------------------------------------------------
ensemble_name = 'TV-Ensemble-Training-InRange'  #name for the directory to put ensemble in
reference_run = 'overland_tiltedV.yaml' #yaml file for baseline run definition to use

# Variables to change
channel_slopes = [0.001,0.0025,0.005,0.0075, 0.01]
hill_slopes=[0.05, 0.1, 0.15, 0.2]
mannings = [3.e-6]
rainvals = [-0.005, -0.01, -0.015, -0.02]
#rainlens = list(range(1, 5, 2))
 
#df_names = ['channel_slope', 'hill_slopes', 'mannings', 'rain_value', 'rain_length']
df_names = ['channel_slope', 'hill_slopes', 'mannings', 'rain_value']

ensemble_settings = []
for cs in channel_slopes:
  for hs in hill_slopes:
    for man in mannings:
          for rval in rainvals:
                ensemble_settings.append((float(cs), float(hs), float(man), 
                              float(rval)))

n_run= len(ensemble_settings)
print("Ensemble will have", n_run, "members")

# Create a list of directories to run in
ensemble_paths = list(range(n_run))
padding=len(str(n_run-1))
ensemble_paths=[str(i).zfill(padding) for i in ensemble_paths]

# Make a dataframe of the settings
ensemble_df = pd.DataFrame(ensemble_settings, columns=df_names)
ensemble_df['path'] = ensemble_paths
ensemble_df['run_name']= ""

# %%
# -----------------------------------------------------------------------------
# Run Ensemble
# -----------------------------------------------------------------------------
# set the paths
THIS_DIR = os.path.dirname(__file__)
os.environ["BASE"] = os.path.join(THIS_DIR, ensemble_name)
os.environ["REF"] = os.path.join(THIS_DIR, reference_run)

#Make a directory for the ensemble 
# write the ensemble summary and copy the basline run infor for future reference
#mkdir('$BASE')
#csvfile = os.path.join(THIS_DIR, ensemble_name, 'ensemble_settings.csv')
#ensemble_df.to_csv(csvfile, index=False)
#cp('$REF', '$BASE')

# Run ensemble
for idx in range(n_run):
  #Get the settings:
  cs, hs, man, rval, = ensemble_settings[idx]

  #print('='*20)
  print(f'# {str(idx).rjust(len(str(n_run)))} Start compute {ensemble_settings[idx]}')
  print('='*20)

  # Make a directory for the run and copy the baselin yaml in
  run_dir = f'$BASE/{ensemble_paths[idx]}'
  mkdir(run_dir)
  cp('$REF', run_dir)
  #link('$INPUT', f'{run_dir}/input') #keep this for later if we want an indicator file

  #Read in the run
  run = Run.from_definition(f'{run_dir}/{reference_run}')

  #add run name to the ensemble settings
  ensemble_df.run_name.iloc[idx]=run.get_name()

  #change channel slopes
  run.TopoSlopesY.Geom.domain.Value = cs

  #change hillsopes
  run.TopoSlopesX.Geom.right.Value = hs
  run.TopoSlopesX.Geom.channel.Value = hs
  run.TopoSlopesX.Geom.left.Value = -hs

  #change the mannings
  run.Mannings.Geom.domain.Value = man

  # change rain length
  #run.Cycle.rainrec.rain.Length = int(rlen)

  # change rain val
  run.Patch.z_upper.BCPressure.rain.Value = rval

  #run.dist('input/SandTank_Indicator.pfb')
  run.run()

  print('='*20)


# Write out the ensemble settings  and copy the baseline run definition for reference
csvfile = os.path.join(THIS_DIR, ensemble_name, 'ensemble_settings.csv')
ensemble_df.to_csv(csvfile, index=False)
cp('$REF', '$BASE')

# %%
