#checking the string if it is palindrome or not
def palindrome_string_checker(str1):
    if  str1 == str1[::-1]:
        print("It is palindrome")
    else:
        print("It is not a palindrome")    


if __name__ == "__main__":
    print("Enter the string:")
    str1 = input()
    palindrome_string_checker(str1)
