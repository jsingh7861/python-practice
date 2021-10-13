
def file_with_function(filename):
    with open(filename, 'w') as data:
        data.write("This is the content of file created with 'with' function")


if __name__ == "__main__":
    print("File to be created")
    file = input() 
    file_with_function(file)
