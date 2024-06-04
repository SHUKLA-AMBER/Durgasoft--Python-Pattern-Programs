class pattern4:

	def __init__(self , n):
		self.n = n 


	def pattern_logic_1(self):

		for ii in range(self.n):
			print(" " * (self.n - 1 - ii) , end="")

			for i in range(ii+1):

				print(f"{chr(65+ii)} " , end="")

			print()

		for i in range(self.n - 1):

			print(" " * (i + 1) , end="")

			for j in range( self.n  - 1 - i):

				print(f"{chr(64+ self.n -1  - i)} " , end ="")

			print()


n = int(input(" n: "))
pattern4(n).pattern_logic_1()