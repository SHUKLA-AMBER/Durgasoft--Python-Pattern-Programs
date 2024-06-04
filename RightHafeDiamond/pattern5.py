class pattern5:

	def __init__(self , n):
		self.n = n 


	def pattern_logic_1(self):

		for i in range( self.n ):

			for j in range( i + 1):

				print(self.n - j , end=" ")

			print()


		for i in range(self.n - 1):

			for j in range(self.n - 1 - i):

				print(self.n - j , end=" ")

			print()


pattern5(int(input(" n : "))).pattern_logic_1()