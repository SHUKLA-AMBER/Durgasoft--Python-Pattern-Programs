class pattern1:
	""" To print given number of *s in a row """

	def __init__(self, n):
		self.n = n

	def pattern_logic_1(self):

		print("Logic 1")
		for i in range(self.n):
			print("*" , end=" ")

		print()

	def pattern_logic_2(self):

		print("Logic 2")
		print("* "* self.n)
		print()


n = int(input("Enter the value of n : "))


p = pattern1(n)
p.pattern_logic_1()
p.pattern_logic_2()

