class pattern3:
	""" Inverted Right Angle Triangle pattern with fixed alphabet symbol in every row """
	def __init__(self,n):
		self.n = n


	def pattern_logic_1(self):

		for i in range(self.n):
			for j in range(self.n -i):
				print( chr(65+i) , end=" ")
			print()

		print()

	def pattern_logic_2(self):

		for i in range(self.n):
			print(f"{chr(65+i)} "*( self.n - i))


n = int(input("enter n: "))
p = pattern3(n)
p.pattern_logic_2()
print() 
p.pattern_logic_1()