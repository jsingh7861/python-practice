###
# Program for string formatting
###

def string_formatter(name,age):
    print("Hello, %s. You are %s." % (name, age))


if __name__ == "__main__":
    print("Enter name:")
    name = input()
    print("Enter Age:")
    age = input()
    string_formatter(name,age)






