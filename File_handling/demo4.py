## Read the file and append the data


###
#Reading and appending the file
###
def file_appender(file_append):
    data = open(file_append, 'a')
    data.write("\nThis is the third appending line.")
    data.close()
    print("File to check:", file_append)

###
#Creating and writing the file 
###
def file_appender_reader(filename):
    data = open(filename, 'w')
    data.write("This is the first line of the file. \nThis is the second line of the file")
    data.close()
    file_appender(filename)

###
#Main function
###

if __name__ == "__main__":
    print("Name of the file to create:")
    file = input()
    file_appender_reader(file)
    




