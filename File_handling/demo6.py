
def file_word_finder(filename, string_search):
    count = 0
    data = open(filename, 'r')
    for i in data:
        i = i.strip()
 #       i = i.lower()
        words = i.split(" ")
        for word in words:
            if word == string_search:
                count = count + 1
    print("Numberr of reoccurence of searched word in given file:", count)


if __name__ == "__main__":
    print("How many times the below word exists in a file:")
    string_to_search = input()
    file = "demo6.txt"
    file_word_finder(file,string_to_search)

