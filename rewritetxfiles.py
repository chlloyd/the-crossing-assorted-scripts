import glob
import os
import subprocess

maketx = "C:\\solidangle\\mtoadeploy\\2018\\bin\\maketx.exe -u --oiio --checknan --filter lanczos3" # path to maketx.exe

path = 'P:\\OneDrive - Birmingham City University\\Final Year Project Animation\\Production\\Environment\\sourceimages\\' #path to sourceimages folder

tif_files = [f for f in glob.glob(path + "**/*.tif", recursive=True)]

for file in tif_files:
    output_file = os.path.splitext(file)[0] + ".tx"
    subprocess.run(maketx + " " + file +" -o " +output_file)
