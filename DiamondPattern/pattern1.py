class pattern1:


	def __init__(self,n):
		self.n = n

	def pattern_logic_1(self):


		for i in range(self.n):

			print("_" * (self.n -1 -i) , end="")

			for i in range( 2 * ( i+1) - 1):
				if i % 2 == 0:
					print("*" , end="")
				else:
					print("_" ,end ="")


			print()

		for j in range(self.n-1):

			print("_" * (j+1),end="")


			for  j in range( 9 - 2 * (j+1)):
				if j % 2 == 0:
					print("*" ,end="")
				else:
					print("_",end="")

			print()

m = int(input(" n : "))
pattern1(m).pattern_logic_1() 