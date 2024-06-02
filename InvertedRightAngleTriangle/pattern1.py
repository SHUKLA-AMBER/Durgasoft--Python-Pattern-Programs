class pattern1:

	def __init__(self,n):
		self.n = n


	def pattern_logic_1(self):

		for i in range( self.n):
			for j in range(self.n - i):

				print("*" , end = " ")

			print()

		print()


	def pattern_logic_2(self):

		for i in range(self.n):

			print(f"{'x'} "* (self.n - i))



n = int(input("Enter n : "))
p = pattern1(n)
p.pattern_logic_2()