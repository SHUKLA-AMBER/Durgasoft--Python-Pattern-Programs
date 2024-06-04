class pattern2:

	def __init__(self , n):
		self.n  = n 


	def pattern_logic_1(self):

		for ii in range (self.n ):

			for i in range ( ii+1):

				print(f"{chr(65+ii)} " , end='')

			print()

		for j in range(self.n -1):

			for i in range (self.n - 1 -j):

				print(f"{chr(64+ self.n - 1 - j)}" , end=' ')

			print()




pattern2(int(input(" n : "))).pattern_logic_1()