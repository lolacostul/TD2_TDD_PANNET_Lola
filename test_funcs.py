import unittest
import funcs

class TestFuncs(unittest.TestCase):

	def test_mirror(self):
		self.assertEqual(funcs.mirror("", 2), IndexError)
		self.assertEqual(funcs.mirror(" ", 0), "  ")
		self.assertEqual(funcs.mirror("", 0), "")
		self.assertEqual(funcs.mirror(123456789, 5), TypeError)
		self.assertEqual(funcs.mirror("bonjour", -1), "bonjourruojnob")
		self.assertEqual(funcs.mirror("bonjour", -3), "bonjoojnob")
		self.assertEqual(funcs.mirror("bonjour", 0), "bb")
		self.assertEqual(funcs.mirror("salut", 7), IndexError)
		self.assertEqual(funcs.mirror("Hello World!", -1), "Hello World!!dlroW \
															olleH")
		self.assertEqual(funcs.mirror("hey you", 4), "hey yy yeh")
		self.assertRaises(funcs.mirror([0,1,2,3,4,5], 4), TypeError)
		self.assertRaises(funcs.mirror(["p","a","o"], 1), TypeError)

if __name__ == '__main__':
	unittest.main()