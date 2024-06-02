class pattern4:


	def __init__(self,n):
		self.n = n



	def pattern_logic_1(self):

		for i in range(self.n):
			count = 1

			for j in range(self.n - i - 1):
				print(" ",end="")


			for k in range(2 * (i +1) -1):
				
				if k % 2 == 0:
					print(count, end="")
					count = count + 1

				else:
					print(" ", end="")




			print()

n = int(input("Enter n:"))
p = pattern4(n)
p.pattern_logic_1()