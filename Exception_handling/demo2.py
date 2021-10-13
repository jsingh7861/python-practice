


# converting an exception to error

def exception_manager(a):
    try:
        print("Second element:",a[1])
        print("Fifth element:",a[4])
    except IndexError:
        print ("An error occured")

    

if __name__ == "__main__":
    x = [1,2,3,4]
    exception_manager(x)