###
# Program to print number form 1 to 100
###

def fizz_buzz():
    for i in range(1,100):
        if i % 3 == 0 and i % 7 == 0:
            print("Fizz buzz")
        elif i % 3 == 0:
            print("Fizz")    
        elif i % 7 == 0:
            print("buzz")
        else:
            print(i)            

if __name__ == "__main__":
    fizz_buzz()