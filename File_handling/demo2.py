


def file_read(filename):
    print(filename)
    data = open(filename, 'r')
    print (data.read())




if __name__ == "__main__":
    print("Input the file to read:")
    file = input()
    file_read(file)
