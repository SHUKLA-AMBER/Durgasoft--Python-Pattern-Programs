class pattern4:

	def __init__(self , n ):
		self.n = n


	def pattern_logic_1(self):

		for i in range(self.n ):

			for j in range( i + 1):

				print(f"{chr(65+j)}" , end=" ")

			print()

		for i in range(self.n - 1):

			for i in range(self.n - 1 - i):

				print(f"{chr(65+i)}" , end=" ")

			print()


pattern4(int(input("n : "))).pattern_logic_1()