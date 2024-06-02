class pattern2:

	def __init__(self,n):

		self.n = n


	def pattern_logic_1(self):

		for j in range(self.n):
			for i in range(self.n - j):

				print(j+1 , end=" ")
			print()


		print()


	def pattern_logic_2(self):

		for i in range(self.n):

			print(f"{i+1} " *( self.n - i))

		print()


n = int(input( "Enter n : "))
p = pattern2(n)
p.pattern_logic_1()
p.pattern_logic_1()

