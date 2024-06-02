class pattern5:

	def __init__(self,n):
		self.n = n


	def pattern_logic_1(self):

		for i in range(self.n):

			#spaces
			print(" "* (self.n - i - 1) , end="")


			for j in range( i+1):

					print(f"{chr(64+self.n-j)} " , end="")


			print()

		print()


n = int(input("Enter n:"))

pattern5(n).pattern_logic_1()