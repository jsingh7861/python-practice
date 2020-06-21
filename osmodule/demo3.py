###
# Program to delete the directory
###

import os

def directorydel(dirname):
    try:
        os.rmdir(dirname)
    except(OSError):
        print("Encounter an error")


if __name__ == "__main__":
    print("Enter the directory to be removed:")
    dirname = input()
    directorydel(dirname)
