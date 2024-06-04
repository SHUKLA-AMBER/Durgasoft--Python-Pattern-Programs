class pattern7:

	def __init__(self ,  n ):
		self.n = n 


	def pattern_logic_1(self ):

		for i in range(self.n):

			for ii in range(i+1):

				print("*" , end=' ')

			print()


		for i in range(self.n - 1):

			for ii in range(self.n - 1 - i):

				print("*" , end= ' ')

			print()


n = int(input(" n : "))
pattern7(n).pattern_logic_1()