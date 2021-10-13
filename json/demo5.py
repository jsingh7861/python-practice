###
#Program to read the json file
#Deserialisation
###

import json

def json_reader(FILE_NAME):
    with open(FILE_NAME, "r") as p:
        print(json.load(p))

if __name__ == "__main__":
    print("Input the json file name:")
    FILE_NAME = input()
    json_reader(FILE_NAME)


