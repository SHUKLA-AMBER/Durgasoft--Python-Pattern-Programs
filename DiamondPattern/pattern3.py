class pattern3:

	def __init__(self,n):
		self.n = n


	def pattern_logic_1(self):

		for i in range( self.n ):

			print( " " * (self.n - 1 - i) , end="")

			for ii in range( i+1):

				print(i+1 , end=" ")

			print()

		for ii in range(self.n - 1):

			print(" "* (ii+1) , end='')

			for i in range(self.n - 1 - ii):

				print(self.n - ii - 1 , end=' ')

			print()

n = int(input("enter n : "))
pattern3(n).pattern_logic_1()