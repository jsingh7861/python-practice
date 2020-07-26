###
# Program to show usage of json module
###

import json

def json_gen(a):
    print(json.dumps(a))


if __name__ == "__main__":
    a = {"name": "Jasvinder singh", "country": "India", "Phone number": "+91-9663911130"}
    json_gen(a)





