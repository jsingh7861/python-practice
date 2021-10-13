###
# program to create the directory
###

import os

def directory(dirname):
    try:
        os.mkdir(dirname)
    except(OSError):
        print("Encountered an error")  


if __name__ == "__main__":
    print("Enter the name of directory to be created:")
    dirname = input()
    directory(dirname)