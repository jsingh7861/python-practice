
# mulptiple exceeption handling
def exception_manager(x):
    try:
        print(x/(x-5))
        print("value of b:", b)
    except(ZeroDivisionError,NameError):
        print("An error occured") 
    print(x)   

if __name__ == "__main__":
    a = 5
    exception_manager(a)
