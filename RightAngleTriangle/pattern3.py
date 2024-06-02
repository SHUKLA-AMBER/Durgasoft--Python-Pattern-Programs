class pattern3:
	""" To print Right Angle Triangle pattern with fixed alphabet symbol in every """

	def __init__(self,n):
		self.n = n


	def pattern_logic_1(self):

		for i in  range(self.n):

			for j in range(i+1):

				print(chr(65+i) , end=" ")
			print()


		print()

	def pattern_logic_2(self):
		for j in range(self.n):
			print(f"{chr(65+j)} "* (j+1))

n = int(input("Enter n : "))
p = pattern3(n)
p.pattern_logic_1()
print()
p.pattern_logic_2()