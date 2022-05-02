import sys
import os
import subprocess


# Get the list of all files and directories
# in the root directory
path = sys.argv[1]
dir_list = os.listdir(path)
  
print("Files and directories in '", path, "' :") 
print(dir_list)