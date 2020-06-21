###
# program to find the file path
###

import os

def file_path_finder(filename):
    try:
        file_path = os.stat(filename)
        print("The path of",filename, "is", file_path  )
    except(OSError):
        print("Encounter an error")    

if __name__ == "__main__":
    print("Enter the file whose path needs to be figured out")
    filename = input()
    file_path_finder(filename)