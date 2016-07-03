import unittest
from primes import is_prime

class PrimesTestCase(unittest.TestCase):

    #Check is is prime
    def test_is_five_prime(self):
        self.assertTrue(is_prime(5))

    #Check is four is not prime
    def test_four_is_not_prime(self):
        self.assertFalse(is_prime(4), msg='Four is not prime')

    #Check if 0 is not prime
    def test_zero_is_not_prime(self):
        self.assertFalse(is_prime(0), msg="Zero is not prime")

    #Ensure all negative numbers are not prime    
    def test_negative_number(self):
        for index in range (-1, -10, -1):
            self.assertFalse(is_prime(index))

if __name__ == '__main__':
    unittest.main()
    

