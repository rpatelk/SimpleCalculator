import unittest
import SimpleCalculator as sc

# Test class for SimpleCalculator class
# @author Raj Patel
class SimpleCalculatorTest(unittest.TestCase):

    # Tests the addition method.
    def test_addition(self): 
        # Passing Test
        self.assertEqual(sc.addition(2, 3), 5)
        self.assertEqual(sc.addition(50, 40), 90)
        self.assertEqual(sc.addition(3.567, 9.876), 13.443)
        self.assertEqual(sc.addition(-2, -3), -5)

        # Failing Test
        self.assertNotEqual(sc.addition(2, 3), 6)
        self.assertNotEqual(sc.addition(50, 40), 4000)
        self.assertNotEqual(sc.addition(3.567, 9.876), 15)
        self.assertNotEqual(sc.addition(-2, -3), -10)

    # Tests the subtraction method.
    def test_subtraction(self): 
        # Passing Test
        self.assertEqual(sc.subtraction(5, 3), 2)
        self.assertEqual(sc.subtraction(9678, 40), 9638)
        self.assertEqual(sc.subtraction(9.876, 3.567), 6.308999999999999)
        self.assertEqual(sc.subtraction(4, 10), -6)

        # Failing Test
        self.assertNotEqual(sc.subtraction(2, 3), 6)
        self.assertNotEqual(sc.subtraction(50, 40), 4000)
        self.assertNotEqual(sc.subtraction(3.567, 9.876), 15)
        self.assertNotEqual(sc.subtraction(4, 10), -20)

    # Tests the multiplication method.
    def test_multiplication(self): 
        # Passing Test
        self.assertEqual(sc.multiplication(2, 3), 6)
        self.assertEqual(sc.multiplication(50, 40), 2000)
        self.assertEqual(sc.multiplication(9.876, 3.567), 35.227692)
        self.assertEqual(sc.multiplication(4, -10), -40)

        # Failing Test
        self.assertNotEqual(sc.multiplication(2, 3), 5)
        self.assertNotEqual(sc.multiplication(50, 40), 90)
        self.assertNotEqual(sc.multiplication(3.567, 9.876), 15)
        self.assertNotEqual(sc.multiplication(4, -10), 20)

    # Tests the division method.
    def test_division(self): 
        # Passing Test
        self.assertEqual(sc.division(3, 2), 1.5)
        self.assertEqual(sc.division(2, 3), 0.6666666666666666)
        self.assertEqual(sc.division(6000, 20), 300)
        self.assertEqual(sc.division(9.876, 3.567), 2.7687132043734226)
        self.assertEqual(sc.division(4, -10), -2/5)

        # Failing Test
        self.assertNotEqual(sc.division(2, 3), 5)
        self.assertNotEqual(sc.division(50, 40), 90)
        self.assertNotEqual(sc.division(3.567, 9.876), 15)
        self.assertNotEqual(sc.division(4, -10), 20)

if __name__ == '__main__':
    unittest.main()