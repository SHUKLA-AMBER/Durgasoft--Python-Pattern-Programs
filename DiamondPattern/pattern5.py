class pattern5:


	def __init__(self,n):
		self.n = n

	def pattern_logic_1(self):

		for i in range(self.n):

			print(" "* (self.n - 1 - i) , end ="")

			for j in range( i + 1 ):

				print(f"{chr(65+j)} " , end='')

			print()

		for j in range(self.n - 1):

			print(" " * (j + 1 ) , end='')

			for i in range( self.n - 1 - j):
				print(f"{chr(65+ i)} " , end='')

			print()


n = int(input(" n : "))
pattern5(n).pattern_logic_1()
