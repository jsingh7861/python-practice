###
#Program for factorrial of a number
###
  
def output(num):
    print("Factorial of",num,"is", factorial(num)) 


def factorial(num):
    if num < 0:
        return 0
    elif num == 0 or num == 1:
        return 1
    else:
       fact = 1
       for i in range(1,num):
            fact = fact * num
            num -= 1
       return(fact)     
    
if __name__ == "__main__":
    print("Enter the number to find it's factorial:")
    num = int(input())
    factorial(num)
    output(num)

 


    
  
