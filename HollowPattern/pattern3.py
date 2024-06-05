class pattern3:

	def __init__(self , n):

		self.n = n 


	def pattern_logic_1(self):

		for i in range(self.n):

			print(" " * (self.n - 1 - i) , end="")

			for j in range( i + 1):

				if  j - 1 < 0 or j+1 == i+1:
					print(self.n - i , end =" ")

				else:
					print(" " , end=" ")

			print()

		for i in range(self.n - 1):

			print(" " * (i+1) , end="")

			for j in range( self.n - 1 - i ):

				if j - 1 < 0 or j + 1 == (self.n - 1 - i):
					print(i+2, end=" ")

				else:
					print(" " , end=" ")

			print()



pattern3(int(input(" n : "))).pattern_logic_1()

