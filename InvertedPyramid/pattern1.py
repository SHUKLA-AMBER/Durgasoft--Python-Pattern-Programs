class pattern1:

	def __init__(self,n):
		self.n = n


	def pattern_logic_1(self):

		for i in range(self.n):

			if i > 0:
				print(" "*(i), end="")

			for i in range(self.n - i):
				print("* ", end="")

			print()

n =int(input("e : "))
pattern1(n).pattern_logic_1()