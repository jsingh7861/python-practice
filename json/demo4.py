###
# programs to write and create and json file
# Serialization
###
import json

def json_create(A):
    with open("sample4.json", "w") as p:
        json.dump(A, p)

if __name__ == "__main__":
    A = {"name": "jasvinder singh", "class": "b.tech", "country": "India", "Profession": "It engineer"}
    json_create(A)

