class pattern5:
	""" Right Angle Triangle pattern with alphabet symbols in dictionary order in every row """

	def __init__(self, n):
		self.n = n

	def pattern_logic_1(self):

		for i in range(self.n):
			for j in range(i+1):
				print(chr(65+j) , end=" ")
			print()


n = int(input("Enter n : "))
p = pattern5(n)
p.pattern_logic_1()