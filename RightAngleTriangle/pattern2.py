class pattern2:
	""" To print Right Angle Triangle pattern with fixed digit in every row """

	def __init__(self, n):
		self.n = n

	def pattern_logic_1(self):

		for i in range(self.n):
			for j in range(i+1):

				print(i+1 , end=" ")

			print()

	def pattern_logic_2(self):

		for i in range(self.n):
			print(f"{i+1} "* (i+1) )



n = int(input("Enter n : "))
p = pattern2(n)
p.pattern_logic_1()
print()
p.pattern_logic_2()
print()
