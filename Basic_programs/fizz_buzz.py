###
# Program to print number form 1 to 100
###
import unittest

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

class test_case(unittest.TestCase):
    def test_case_number(self):
        self.assertEqual(fizz_buzz(1)[0],1)
        self.assertEqual(fizz_buzz(2)[1],2)
        self.assertEqual(fizz_buzz(4)[3],4)

  
if __name__ == "__main__":
    k = fizz_buzz(100)
    print(k)
    unittest.main()
    