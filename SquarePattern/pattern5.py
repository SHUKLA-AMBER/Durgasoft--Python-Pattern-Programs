class pattern5:
	""" To print square pattern with fixed alphabet symbol """

	def __init__(self,n):
		self.n = n

	def pattern_logic_1(self):
		for i in range(self.n):
			for j in range(self.n):

				print( chr(65) , end=" ")

			print()
		print()

	def pattern_logic_2(self):
		for j in range(self.n):
			print( (chr(65) + " ") * self.n )


n= int(input("Enter value on n: "))
p = pattern5(n)
p.pattern_logic_1()
p.pattern_logic_2()