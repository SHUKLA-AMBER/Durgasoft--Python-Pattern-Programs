class pattern6:

	def __init__(self,n):
		self.n = n


	def pattern_logic_1(self):

		for i in range(self.n):
			for j in range(i+1):

				print(self.n - j , end=" ")
			print()


n = int(input("enter n : "))
p = pattern6(n)
p.pattern_logic_1()