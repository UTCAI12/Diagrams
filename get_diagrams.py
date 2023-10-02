import shutil
import sys
import os
sourceFolder = "./out/sequence/"
# This folder contains one folder per diagram
# Must move all diagrams on a single folder called "diagrams"
# must print all the names of the diagrams on a file called "diagrams.txt"
# They must be printed in the same order as they are on the folder
# They must be printed without the extension
# They must be printed in a Python / JS list format


# Get the list of diagrams folders
diagrams = os.listdir(sourceFolder)

# Create the new folder "diagrams"
if not os.path.exists(sourceFolder + "diagrams"):
    os.makedirs(sourceFolder + "diagrams")

# for each folder, get the diagram inside
for diagram in diagrams:
    diagrams_folder = os.listdir(sourceFolder + diagram)
    # for each diagram, get the name of the diagram
    for file in diagrams_folder:
        # move the diagram into the new folder
        shutil.move(sourceFolder + diagram + "/" + file,
                    sourceFolder + "diagrams/" + file)

# remove the old folders
for diagram in diagrams:
    shutil.rmtree(sourceFolder + diagram)
