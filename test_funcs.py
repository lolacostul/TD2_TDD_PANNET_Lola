import math
import unittest

import sympy as sym

import funcs


class TestFuncs(unittest.TestCase):
    def test_mirror(self):
        self.assertEqual(funcs.mirror("bonjour", 6), "bonjourruojnob")
        self.assertEqual(funcs.mirror("salut", 3), "saluulas")
        self.assertEqual(funcs.mirror("bonjour", 0), "bb")
        self.assertEqual(funcs.mirror("hey you", 4), "hey yy yeh")
        self.assertEqual(funcs.mirror("Hello World!", 11), "Hello World!!dlroW olleH")
        self.assertEqual(funcs.mirror("Hello World!", 5), "Hello  olleH")
        self.assertEqual(funcs.mirror("Hello World!", 2), "HelleH")

        self.assertEqual(funcs.mirror("bonjour", -1), "rr")
        self.assertEqual(funcs.mirror("bonjour", -2), "urru")
        self.assertEqual(funcs.mirror("bonjour", -3), "ourruo")
        self.assertEqual(funcs.mirror("bonjour", -7), "bonjourruojnob")
        self.assertEqual(funcs.mirror("Hello World!", -1), "!!")
        self.assertEqual(funcs.mirror("Hello World!", -8), "o World!!dlroW o")
        self.assertEqual(funcs.mirror(" ", 0), "  ")

        with self.assertRaises(TypeError):
            funcs.mirror(123456789, 5)
            funcs.mirror([0, 1, 2, 3, 4, 5], 4)
            funcs.mirror(["p", "a", "o"], 1)
            funcs.mirror("bonjour", 6, 0)
            funcs.mirror("Hello World!", 5, "hey")
            funcs.mirror("Hello World!", 5, [0, 1, 2])
            funcs.mirror("Hello World!", [0, 1, 2])

        with self.assertRaises(IndexError):
            funcs.mirror("salut", 7)
            funcs.mirror("", 2)
            funcs.mirror("", 0)
            funcs.mirror("bonjour", -8)

    def test_derivee(self):
        self.assertNotEqual(
            funcs.derivee([1, 2, 3, 4, 5], 2), [0.5, 0.5, 0.5, 0.5, 0.5]
        )
        self.assertEqual(funcs.derivee([1, 2, 3, 4, 5], 2), [0.5, 0.5, 0.5, 0.5])
        self.assertEqual(funcs.derivee([5, 2, 4, 1, 3], 2), [-1.5, 1.0, -1.5, 1.0])
        self.assertNotEqual(funcs.derivee([1, 2, 3, 4, 5], 1), [1, 1, 1, 1, 1])
        self.assertEqual(funcs.derivee([1, 2, 3, 4, 5], 1), [1, 1, 1, 1])
        self.assertEqual(
            funcs.derivee([-1, -2.5, -0.03, 17], 0.25), [-6.0, 9.88, 68.12]
        )
        self.assertEqual(
            funcs.derivee([12.94, 28.272, 3.728, 20.26], 0.25),
            [61.328, -98.176, 66.128],
        )
        self.assertEqual(
            funcs.derivee([61.328, -98.176, 66.128], 0.25), [-638.016, 657.216]
        )
        self.assertEqual(
            funcs.derivee([36.848, 29.28, 32.048], 0.25), [-30.272, 11.072]
        )
        self.assertEqual(
            funcs.derivee([1.2, 1.5, 1.68, 1.98, 2.1, 2.25], 0.01), [30, 18, 30, 12, 15]
        )
        self.assertEqual(
            funcs.derivee([30, 18, 30, 12, 15], 0.01), [-1200.0, 1200.0, -1800.0, 300.0]
        )
        self.assertEqual(
            funcs.derivee([5.245, 8.48, 15.548, 16.48, 21.545], 0.25),
            [12.94, 28.272, 3.728, 20.26],
        )

        with self.assertRaises(TypeError):
            funcs.derivee(["1", "2", "3"], 2)  # array of string as input, not float
            funcs.derivee({1, 2, 3}, 2)  # dictionnary as input, not array
            funcs.derivee(25, 2)  # not an array as input

        with self.assertRaises(ValueError):
            funcs.derivee([], 0.2)  # empty array
            funcs.derivee([1, 2.5, 0.03, 17], -13)  # negative time interval

        with self.assertRaises(ZeroDivisionError):
            funcs.derivee([1, 2.5, 0.03, 17], 0)

    def test_derivee_seconde(self):
        self.assertNotEqual(funcs.derivee_seconde([1, 2, 3, 4, 5], 2), [0, 0, 0, 0, 0])
        self.assertEqual(funcs.derivee_seconde([1, 2, 3, 4, 5], 2), [0.0, 0.0, 0.0])
        self.assertEqual(funcs.derivee_seconde([5, 2, 4, 1, 3], 2), [1.25, -1.25, 1.25])
        self.assertNotEqual(
            funcs.derivee_seconde([1, 2, 3, 4, 5], 1), [0.0, 0.0, 0.0, 0.0, 0.0]
        )
        self.assertEqual(funcs.derivee_seconde([1, 2, 3, 4, 5], 1), [0.0, 0.0, 0.0])
        self.assertEqual(
            funcs.derivee_seconde([5.245, 8.48, 15.548, 16.48, 21.545], 0.25),
            [61.328, -98.176, 66.128],
        )
        self.assertEqual(
            funcs.derivee_seconde([12.94, 28.272, 3.728, 20.26], 0.25),
            [-638.016, 657.216],
        )
        self.assertEqual(
            funcs.derivee_seconde([1.2, 1.5, 1.68, 1.98, 2.1, 2.25], 0.01),
            [-1200, 1200, -1800, 300],
        )

        with self.assertRaises(TypeError):
            funcs.derivee_seconde(
                ["1", "2", "3"], 2
            )  # array of string as input, not float
            funcs.derivee_seconde({1, 2, 3}, 2)  # dictionnary as input, not array
            funcs.derivee(25, 2)  # not an array as input

        with self.assertRaises(ValueError):
            funcs.derivee_seconde([], 0.2)  # empty array
            funcs.derivee_seconde([1, 2.5, 0.03, 17], -13)  # negative time interval

        with self.assertRaises(ZeroDivisionError):
            funcs.derivee_seconde([1, 2.5, 0.03, 17], 0)


    def test_approximation_derivee(self):
        x = sym.Symbol('x')
        # Derive cos
        self.assertEqual(funcs.approximation_derivee(sym.sin(x), sym.pi/2, 0.01), 0.00)
        self.assertEqual(funcs.approximation_derivee(sym.sin(x), -sym.pi/2, 0.01), 0.00)
        self.assertEqual(funcs.approximation_derivee(sym.sin(x), 0, 0.1), 1.0)
        self.assertEqual(funcs.approximation_derivee(sym.sin(x), sym.pi, 0.1), -1.0)
        self.assertEqual(funcs.approximation_derivee(sym.sin(x), -sym.pi, 0.1), -1.0)
        self.assertEqual(funcs.approximation_derivee(sym.sin(x), sym.pi/4, 0.00001), 0.70711)
        self.assertEqual(funcs.approximation_derivee(sym.sin(x), -sym.pi/4, 0.0001), 0.7071)
        # Derive -sin
        self.assertEqual(funcs.approximation_derivee(sym.cos(x), sym.pi/2, 0.01), -1.00)
        self.assertEqual(funcs.approximation_derivee(sym.cos(x), sym.pi/3, 0.00001), -0.86603)
        self.assertEqual(funcs.approximation_derivee(sym.cos(x), -sym.pi/3, 0.00001), 0.86603)
        self.assertEqual(funcs.approximation_derivee(sym.cos(x), sym.pi/3, 0.000001), -0.866025)
        self.assertEqual(funcs.approximation_derivee(sym.cos(x), sym.pi/6, 0.1), -0.5)

        # Derive exp
        self.assertEqual(funcs.approximation_derivee(sym.exp(x), 0, 0.1), 1)
        self.assertEqual(funcs.approximation_derivee(sym.exp(x), 1, 0.000000000000001), 2.718281828459045)
        self.assertEqual(funcs.approximation_derivee(sym.exp(x), -1, 0.0001), 0.3679)
        self.assertEqual(funcs.approximation_derivee(sym.exp(x), -1, 0.00001), 0.36788)
"""

        # Derivee 1/x
        self.assertEqual(funcs.approximation_derivee(math.log, 1, 0.1), 1.0)
        self.assertEqual(funcs.approximation_derivee(math.log, math.e, 0.0000001), 0.3678794)
        
        # Derivee 1/(2*math.sqrt)
        self.assertEqual(funcs.approximation_derivee(math.sqrt, 2, 0.0000001), 0.3535534)

        # Derivee -1/x**2
        self.assertEqual(funcs.approximation_derivee(1/x, 1, 0.1), -1.0)
        self.assertEqual(funcs.approximation_derivee(1/x, -1, 0.1), 1.0)
        self.assertEqual(funcs.approximation_derivee(1/x, 4, 0.1), -0.1)
        self.assertEqual(funcs.approximation_derivee(1/x, 4, 0.001), -0.063)
        self.assertEqual(funcs.approximation_derivee(1/x, 4, 0.0001), -0.0625)
        self.assertEqual(funcs.approximation_derivee(1/x, -4, 0.0001), 0.0625)

        # Derivee u*x**(u-1)
        self.assertEqual(funcs.approximation_derivee(x**2, math.sqrt(2), 0.1), 2.8)
        self.assertEqual(funcs.approximation_derivee(x**2, math.sqrt(2)/2, 0.0001), 1.4142)
        self.assertEqual(funcs.approximation_derivee(x**2, math.sqrt(45.54548)/13, 0.0000001), 1.0382676)
        self.assertEqual(funcs.approximation_derivee(x**3, 4.16, 0.001), 51.917)
        self.assertEqual(funcs.approximation_derivee(x**6, -3.48, 0.0001), -3062.2981)

        with self.assertRaises(ValueError):
            funcs.approximation_derivee(math.log, 0, 0.01)  # math domain error
            funcs.approximation_derivee(math.log, 0, 42)  # invalid accuracy
            funcs.approximation_derivee(math.sqrt, -5, 0.001)

        with self.assertRaises(TypeError):
            funcs.approximation_derivee(math.log, math.exp, 0.1)
            funcs.approximation_derivee("exp", 0, 0.1)  # str in arg

        with self.assertRaises(ZeroDivisionError):
            funcs.approximation_derivee(1/x, 0, 0.01)
            funcs.approximation_derivee(math.sqrt, 0, 0.0001)
"""

if __name__ == "__main__":
    unittest.main()
