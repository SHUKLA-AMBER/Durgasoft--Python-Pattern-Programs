class pattern2:

	def __init__(self, n):
		self.n = n

	def pattern_logic_1(self):
		for i in range(self.n):

			for j in range(self.n - 1 - i):
				print(" ",end="")


			for k in range(i+1):

				if k == 0 or k % 2 ==0:
					print( i+1 , end="")
				else:
					print(" " , end="")
			
			# if i >0:
			# 	for j in range(i):
			# 		if i % 2 != 0 or j % 2 == 0:
			# 			print(i+1, end="")
			# 		else:
			# 			print(" ",end="")

			if (i > 0):
				for l in range(i):

					if i % 2 != 0:
						if l % 2 == 0:
							print(i+1 , end='')
						else:
							print(" ", end="")
					else:
						if l % 2 == 0:
							print(' ' , end='')
						else:
							print(i+1, end="")
			print()


	def pattern_logic_2(self):

		for i in range(self.n):

			print(" "* (self.n-(i+1)) , end="")

			print(f"{i+1} " * (1+i) , end="")
			print()




			


n = int(input())
p = pattern2(n)
p.pattern_logic_1()

