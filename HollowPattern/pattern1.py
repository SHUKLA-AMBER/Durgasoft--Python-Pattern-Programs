class pattern1:

	def __init__(self,n):
		self.n =n

	def pattern_logic_1(self):

		for ii in range(self.n):
			print(" "  * (self.n - 1 - ii) , end="")
			for i in range( 2 * (ii+1) - 1):
				if i - 1 < 0 or i + 1  ==  (2 * (ii+1) - 1) :
					print("@" , end="")

				else:
					print(" "  ,end="")

			
			print()

		for ii in range(self.n - 1 ):

			print(" " * (ii+1) , end="")

			for i in range( self.n - 1 - ii):

				if i - 1 < 0 or i+ 1 == (self.n - 1 - ii):
					print("@" , end=" ")

				else:
					print(" ", end=" ")

			print()



pattern1(int( input(" n : "))).pattern_logic_1()