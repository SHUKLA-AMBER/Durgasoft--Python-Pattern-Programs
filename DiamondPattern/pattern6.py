class pattern6:

	def __init__(self , n ):
		self.n = n 


	def pattern_logic_1(self):

		for i in range(self.n):
			print(" " * (self.n - i -1) , end='')

			for i in range(i+1):
				print(self.n - i , end=" ")

			print()


		for i in range(self.n - 1):
			print(" " * (i+1) , end='')


			for j in range(self.n - 1  - i):

				print(self.n  - j , end= " ")

			print() 


n  = int(input(" n : "))
pattern6(n).pattern_logic_1()