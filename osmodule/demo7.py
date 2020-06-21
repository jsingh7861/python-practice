###
#program to execute the shell command
###
import os


def shell_executer(command):
    try:
        print("The output of", command,"is an below:")
        result = os.system(command)
        

    except(OSError):
        print("Encounter an error")    


if __name__ == "__main__":
    print("Ecxecute the below command:")
    command = input()
    shell_executer(command)