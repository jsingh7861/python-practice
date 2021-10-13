###
# program to list directories 
###

import os 
from pprint import pprint as pp


def list_dir(path):
    try:
        dir = os.listdir(path)
        print("The given path has below directories:")
        pp(dir)
    except(OSError):
        pp('Error')

if __name__ == "__main__":
    print("Enter the path to list the directory:")
    path = input()
    list_dir(path)