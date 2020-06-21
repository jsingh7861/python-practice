###
# program to get environment variables
###


import os
import pprint

def env_var_getter():
    data = os.environ
    pprint.pprint(dict(data), width=1)


if __name__ == "__main__":
    env_var_getter()
