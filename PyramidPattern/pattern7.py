
class pattern7:


	def __init__(self ,n):
		self.n = n


	def pattern_logic_1(self):

		for i in range(self.n ):

			print(" " * (self.n -1 -i) ,end="")


			for j in range(i+1):

				print(f"{self.n -j} " , end="")


			print()




n = int(input("Enter n: "))
pattern7(n).pattern_logic_1()