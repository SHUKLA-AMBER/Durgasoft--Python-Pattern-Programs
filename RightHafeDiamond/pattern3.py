class pattern3:

	def __init__(self , n ):

		self. n = n 


	def pattern_logic_1(self):

		for i in range(self.n):

			for j in range(i+1):

				print(j+1 , end=" ")

			print()

		for i in range(self.n - 1):

			for j in range(self.n -1 -i):

				print(j+1 , end =" ")

			print()

pattern3(int(input("n : "))).pattern_logic_1()