class pattern8:

	def __init__(self,n):
		self.n = n

	def pattern_logic_1(self):
		for i in range(self.n):
			for j in range(self.n - i):

				print(f"{chr(64+self.n - j)} ", end=" ")
			print()
		print()


n = int(input("Enter : "))
p = pattern8(n)
p.pattern_logic_1()