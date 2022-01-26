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

		self.assertEqual(funcs.mirror("bonjour", -1), "rr")
		self.assertEqual(funcs.mirror("bonjour", -2), "urru")
		self.assertEqual(funcs.mirror("bonjour", -3), "ourruo")
		self.assertEqual(funcs.mirror("bonjour", -7), "bonjourruojnob")
		self.assertEqual(
			funcs.mirror("Hello World!", -1),
		 	"!!"
		 )
		self.assertEqual(
			funcs.mirror("Hello World!", -8),
		 	"o World!!dlroW o"
		 )
		self.assertEqual(funcs.mirror(" ", 0), "  ")

		with self.assertRaises(TypeError):
			funcs.mirror(123456789, 5)
			funcs.mirror([0,1,2,3,4,5], 4)
			funcs.mirror(["p","a","o"], 1)
			funcs.mirror("bonjour", 6, 0)
			funcs.mirror("Hello World!", 5, "hey")
			funcs.mirror("Hello World!", 5, [0,1,2])
			funcs.mirror("Hello World!", [0,1,2])

		with self.assertRaises(IndexError):
			funcs.mirror("salut", 7)
			funcs.mirror("", 2)
			funcs.mirror("", 0)
			funcs.mirror("bonjour", -8)

	def test_derivee(self):
		self.assertEqual(funcs.derivee([1,2,3,4,5], 2), [0.5,0.5,0.5,0.5,0.5])
		self.assertEqual(funcs.derivee([1,2,3,4,5], 1), [1,1,1,1,1])
		self.assertEqual(funcs.derivee([1.2, 1.5,1.68,1.98,2.1,2.25], 0.01), [30,18,30,12,15])

		with self.assertRaises(TypeError):
			funcs.derivee(["1", "2", "3"], 2)
			funcs.derivee({1, 2, 3}, 2)

		with self.assertRaises(ValueError):
			funcs.derivee([-1, -2.5, -0.03,17], 0.25)
			funcs.derivee([], 0.2)

		with self.assertRaises(ValueError):
			funcs.derivee([1,2.5,0.03,17], 0)


if __name__ == '__main__':
	unittest.main()
