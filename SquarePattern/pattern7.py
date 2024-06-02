class pattern7:
	""" square pattern with alphabet symbols in dictionary order """

	def __init__(self,n):
		self.n = n


	def pattern_logic_1(self):

		for i in range(self.n):
			for j in range(self.n):
				print( chr(j+65) , end=" ")
			print()

		print()


n = int(input("Enter n : "))
p = pattern7(n)
p.pattern_logic_1()