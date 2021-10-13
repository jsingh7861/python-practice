


def file_reader(file_name):
    data = open(file_name, 'r' )
    for i in data:
        print(i)

if __name__ == "__main__":
    file = "/Users/jasvindersingh/Desktop/Python_practice/learning.txt"
    file_reader(file)