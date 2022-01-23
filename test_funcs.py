import unittest
import funcs

class TestFuncs(unittest.TestCase):

	def test_mirror(self):
		self.assertEqual(funcs.mirror("bonjour", 6), "bonjourruojnob")
		self.assertEqual(funcs.mirror("salut", 3), "saluulas")
		self.assertEqual(funcs.mirror("bonjour", 0), "bb")
		self.assertEqual(funcs.mirror("hey you", 4), "hey yy yeh")
		self.assertEqual(
			funcs.mirror("Hello World!", 11),
			"Hello World!!dlroW olleH"
		)
		self.assertEqual(
			funcs.mirror("Hello World!", 5),
			"Hello  olleH"
		)
		self.assertEqual(
			funcs.mirror("Hello World!", 2),
			"HelleH"
		)

		with self.assertRaises(TypeError):
			funcs.mirror(123456789, 5)
			funcs.mirror([0,1,2,3,4,5], 4)
			funcs.mirror(["p","a","o"], 1)
		with self.assertRaises(IndexError):
			funcs.mirror("salut", 7)
			funcs.mirror("", 2)

if __name__ == '__main__':
	unittest.main()