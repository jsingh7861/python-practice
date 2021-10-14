#python program to check if number is palindrome or not 


def palindrome_num_checker(num):
    reverse_num = 0
    temp = num
    while num >0:
        digit = num%10
        reverse_num = reverse_num*10 + digit 
        num = num//10 #Gets the last digit
    print("Reverse number:", reverse_num) 
    if (temp == reverse_num):
        print("It is a palindrome number")
    else:
        print("It is not a palindrome number")


if __name__ == "__main__":
    print("Enter the number: ")
    num = int(input())
    palindrome_num_checker(num)



