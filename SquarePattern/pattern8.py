class pattern8:
	""" To print square pattern with digits in descending order """

	def __init__(self,n):
		self.n = n

	def pattern_logic_1(self):

		for i in range(self.n):
			for j in range(self.n):

				print( self.n - i , end=" ")
			print()


	def pattern_logic_2(self):

		for j in range(self.n):
			print( (str( self.n - j) + " ") * self.n)


n = 5
p = pattern8(n)
p.pattern_logic_1()
print()
p.pattern_logic_2()