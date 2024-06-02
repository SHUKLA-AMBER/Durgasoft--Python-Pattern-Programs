class pattern9:
	""" square pattern with alphabets in reverse of dictionary order """

	def __init__(self,n):
		self.n = n

	def pattern_logic_1(self):

		for i in range(self.n):
			for j in range(self.n):

				print( chr(69 - i) , end=" ")

			print()

	def pattern_logic_2(self):

		for j in range(self.n):

			print( f"{chr(69 - j)} "* self.n)

n = int(input("Enter n : "))
p = pattern9(n)
p.pattern_logic_1()
print()
p.pattern_logic_2()