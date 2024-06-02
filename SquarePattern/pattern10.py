class pattern10:
	""" To print square pattern with digits in descending order """

	def __init__(self,n):
		self.n = n

	def pattern_logic_1(self):

		for j in range(self.n):
			for i in range(self.n):

				print(self.n - i , end=" ")
			print()


n = int(input("Enter n : "))
p = pattern10(n)
p.pattern_logic_1()

