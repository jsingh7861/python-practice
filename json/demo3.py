###
# program to show that json supports lists, tuples and object
###

import json


def json_dumps(a,b,c,d,e,f,g,h):
    i = json.dumps(a)
    print(i)
    print(type(i))
    print(json.dumps(b))
    print(json.dumps(c))
    print(json.dumps(d))
    j = json.dumps(e)
    print(j)
    print(type(j))
    k = json.dumps(g)
    print(k)
    print(type(k))
    print(json.dumps(h))



if __name__ == "__main__":
    a = ["let's", "do", "json"]
    b = ("let's", "do", "json")
    c = "Hi"
    d = 123
    e = 23.673
    f = True
    g = False
    h = None
    json_dumps(a,b,c,d,e,f,g,h)



