class pattern4:
	""" square pattern with provided fixed digit in every row """

	def __init__(self,n):
		self.n = n


	def pattern_logic_1(self):
		for i in range(self.n):
			for j in range(self.n):
				print(i+1 , end = " ")
			print()
		print()

	def pattern_logic_2(self):
		for i in  range(self.n):
			print( (str(i+1) +" ") * self.n)
		print()


n = int(input("Enter n : "))
p = pattern4(n)
p.pattern_logic_1()
p.pattern_logic_2()