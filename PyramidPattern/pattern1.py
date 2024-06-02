class pattern1:

	def __init__(self,n):
		self.n = n


	def pattern_logic_1(self):

		for i in range(self.n ):
			for j in range(self.n - i - 1):
				print(" " , end="")

			for k in range(i+1):

				if (k ==0 or k % 2 == 0):
					print("*", end="")
				else:
					print(" ", end="")

			if (i > 0):
				for l in range(i):

					if i % 2 != 0:
						if l % 2 == 0:
							print('*' , end='')
						else:
							print(" ", end="")
					else:
						if l % 2 == 0:
							print(' ' , end='')
						else:
							print("*", end="")

			print()


	def pattern_logic_2(self):

		for i in range(self.n):
			print(" "*(self.n - 1 - i) , end = '')
			print("* " *(i+1), end="")
			print()


n= int(input("Enter : "))
p = pattern1(n)
p.pattern_logic_2()
