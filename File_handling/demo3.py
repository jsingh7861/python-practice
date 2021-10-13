

def file_writer(new_file):
    data = open(new_file, 'w')
    data.write("This is the my first file i am creating \nThis is the second line of the file \nThis is the third line of the file.")
    data.close()

    


if __name__ == "__main__":
    print("Name of the file to be created:")
    file = input()
    file_writer(file)