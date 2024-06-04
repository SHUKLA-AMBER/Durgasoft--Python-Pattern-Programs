class pattern2:

	def __init__(self , n):
		self.n = n 


	def pattern_logic_1(self):


		for i in range(self.n):

			print(" "* (self.n -1-i) , end="")

			count = 1
			for i in range( 1 + ((i+1) - 1) * 2):
				if i % 2 == 0:
					print(f"{count}" , end="")
					count = count + 1
				else:
					print(" " , end="")


			print()

		a = self.n - 1
		a =  a + (a - 1) 
		for i in range (self.n - 1):

			print(" " * (i+1) , end="")

			count = 1
			for i in range( a + ((i+1) - 1)* -2 ):
				if i % 2 ==0:
					print(f"{count}" ,end ="")
					count = count+1
				else:
					print(" ",end="")


			print()

	def pattern_logic_2(self):

		for i in range(self.n):

			print(" " * (self.n - 1 - i) , end="" )

			for j in range( i + 1):
				print(f"{j+1} " , end="")

			print()

		for i in range(self.n - 1):
			print(" " * (i+1) , end="")

			for i in range(self.n - 1 - i):
				print(f"{i+1} " , end="")

			print()
n = int(input(" n : "))
pattern2(n).pattern_logic_2()
pattern2(n).pattern_logic_1()