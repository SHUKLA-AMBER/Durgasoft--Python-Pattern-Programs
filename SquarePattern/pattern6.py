class pattern6:
	""" To print square pattern with digits """

	def __init__(self,n):
		self.n = n


	def pattern_logic_1(self):

		for i in range(self.n):
			for j in range(self.n):
				print(j+1 , end=" ")
			print()


		print()



n = int(input("enter n: "))

p = pattern6(n)
p.pattern_logic_1()