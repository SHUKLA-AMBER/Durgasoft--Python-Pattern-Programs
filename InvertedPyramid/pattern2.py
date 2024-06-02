class pattern2:

	def __init__(self,n):
		self.n = n


	def pattern_logic_1(self):

		for ii in range(self.n):

			if ii > 0:

				print(" "  * ii , end="")

			for i in range(self.n - ii):
				print(f"{ii+1} " ,end="")


			print()

n = int(input(" enter : "))
pattern2(n).pattern_logic_1()