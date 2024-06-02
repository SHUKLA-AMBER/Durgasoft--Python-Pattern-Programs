class pattern7:
	""" Right Angle Triangle pattern symbols in reverse of dictionary order in every row """

	def __init__(self,n):
		self.n = n

	def pattern_logic_1(self):

		for i in range(self.n):
			for j in range(i+1):

				print(chr(64 + self.n -j), end=" ")
			print()

		print()


n = int(input("enter n : "))
p = pattern7(n)
p.pattern_logic_1()