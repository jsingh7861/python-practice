###
# program to change the directory name
###

import os

def rename(dir, new_name):
    try:
        os.rename(dir, new_name)
        print("Directory whose name got changed is:", dir )
    except(OSError):
        print("Encounter an error")


if __name__ == "__main__":
    print("Enter the name of directory to rename:")
    dir = input()
    print("Enter the new name of the directory:")
    new_name = input()
    rename(dir, new_name)