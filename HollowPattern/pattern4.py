class pattern4:

	def __init__(self , n):
		self.n = n


	def pattern_logic_1(self):

		for i in range(self.n):

			print(" " * (self.n - 1 - i) , end="")

			for j in range(i+1):

				if j-1 < 0 or j +1 == (i+1):
					print(f"{chr(65+i)}" , end=" ")

				else:

					print(" " , end=" ")

			print()

		for j in range(self.n - 1):

			print(" " * (j+1) , end="")

			for i in range(self.n - 1 - j):

				if i- 1 < 0 or i+1 == (self.n - 1 - j):
					print(f"{chr(self.n + 64 - 1- j)}" , end=" ")

				else:
					print(" " , end=" ")

			print()


pattern4(int(input(" n : "))).pattern_logic_1()