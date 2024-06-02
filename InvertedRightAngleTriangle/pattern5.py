class pattern5:


	def __init__(self,n):
		self.n = n


	def pattern_logic_1(self):

		for i in range(self.n):
			for j in range(self.n  - i):
				print(f"{chr(self.n+64 - i)}" , end = ' ')
			print()


	def pattern_logic_2(self):

		for j in range(self.n):
			print(f"{chr(self.n + 64 - j)} "* (self.n - j))

n = int(input("Enter : "))
p = pattern5(n)
p.pattern_logic_1()
p.pattern_logic_2()