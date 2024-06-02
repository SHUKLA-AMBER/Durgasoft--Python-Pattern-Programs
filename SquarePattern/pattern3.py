class pattern3:

	""" To print square pattern with provided fixed digit """

	def __init__(self, n):
		self.n = n


	def pattern_logic_1(self):
		for i in range(self.n):
			for j in range(self.n):
				print(self.n , end=" ")
			print()

		print()


	def pattern_logic_2(self):

		for i in range(self.n):

			print( (str(self.n)+" ") * n)

		print()



n = int(input("enter value of n: "))
p = pattern3(n)
p.pattern_logic_1()
p.pattern_logic_2()
