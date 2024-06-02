class pattern5:

	def __init__(self,n):
		self.n = n 


	def pattern_logic_1(self):

		for i in range(self.n):

			if i > 0 :

				print(" "*i ,end="")

			for j in range(self.n - i):
				print(f"{ chr(65+j) } ", end='')

			print()

n = int(input(" n : "))
pattern5(n).pattern_logic_1()

