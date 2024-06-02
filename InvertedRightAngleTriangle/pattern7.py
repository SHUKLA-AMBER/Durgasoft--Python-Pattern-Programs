class pattern7:

	def __init__(self,n):
		self.n = n


	def pattern_logic_1(self):
		for j in range(self.n):
			for i in range(self.n - j):
				print(self.n - i , end= ' ')
			print()
		print()


n = int(input("Enter : "))
p = pattern7(n)
p.pattern_logic_1()