class pattern2:
	""" to print square pattern with * symbols """


	def __init__(self, n):
		self.n = n


	def pattern_logic_1(self):

		for i in range(self.n):
			for j in range (self.n):

				print("*", end= " ")
			print()


		print()


	def pattern_logic_2(self):

		for i in range(self.n):

			print("* " * self.n)

		print()


n = int(input("Enter value of n : "))
p = pattern2(n)

p.pattern_logic_1()
p.pattern_logic_2()