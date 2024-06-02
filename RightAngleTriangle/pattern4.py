class pattern4:
	""" Right Angle Triangle pattern with digits in ascending order in every row """

	def __init__(self,n):
		self.n = n


	def pattern_logic_1(self):
		for i in range(self.n):
			for j in range(i+1):

				print(j+1 , end=" ")
			print()


		print()


n = int(input("Enter n : "))
p = pattern4(n)
p.pattern_logic_1()