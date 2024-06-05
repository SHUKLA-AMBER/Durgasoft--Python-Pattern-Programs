class pattern2:

	def __init__(self , n):
		self.n = n


	def pattern_logic_1(self):

		for i in range(self.n):

			print(" " * (self.n - 1 - i) , end="")

			for j in range(i+1):

				if j - 1 < 0 or  j+1 == (i+1):
					print(i+1 , end=" " )
				else:
					print(" " ,end=" ")


			print()

		for i in range(self.n - 1):

			print(" " * ( i + 1) , end="")

			for j in range(self.n - 1 - i):

				if j - 1 < 0 or j+1  == (self.n -1 - i):
					print(self.n - 1 - i, end=" ")
				else:
					print(" " , end=" ")

			print()


n = int(input(" n : "))
pattern2(n).pattern_logic_1()