###
# Program to print number form 1 to 100
###

def fizz_buzz(n):
    m = []
    for i in range(1,n+1):
        if i % 3 == 0 and i % 7 == 0:
            m.append("Fizzbuzz")
        elif i % 3 == 0:
            m.append("Fizz")   
        elif i % 7 == 0:
            m.append("Buzz")   
        else:
            m.append(i)    
    return m        

def test_case(k , expected_output):
    if k == expected_output:
        print("Test case pass")
    else:
        print("Test case failed")    

if __name__ == "__main__":
    k = fizz_buzz(5)
    print(k)
    expected_output = [1, 2, 'Fizz', 4, 5]
    test_case(k , expected_output)