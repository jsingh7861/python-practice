###
# Program to create the json file
###

import json

def json_gen(dic):
    json_dumps = json.dumps(dic)
    print(json_dumps)
    print(type(json_dumps))

if __name__ == "__main__":
    print("Input the data for json")
    dic = input()
    json_gen(dic)