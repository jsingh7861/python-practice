###
# program to find the operating system 
###

import os

def osfinder():
    try:
        print(os.name)
    except(OSError):
        print("Encountered an error")   

if __name__ == "__main__":
    osfinder()







