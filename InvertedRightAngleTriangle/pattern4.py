class pattern4:
	""" Inverted Right Angle Triangle pattern with fixed digit in every row """

	def __init__(self,n):
		self.n = n


	def pattern_logic_1(self):
		for i in range(self.n):
			for j in range(self.n-i):
				print(self.n -i , end = " ")
			print()

		print()



	def pattern_logic_2(self):
		for j in range(self.n):
			print(f"{self.n -j } "* (self.n - j))

		print()


n = int(input("Enter : "))
p = pattern4(n)
p.pattern_logic_1()
p.pattern_logic_2()	