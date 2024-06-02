class pattern1:
	""" to print Right Angle Triangle patter wit * symbols """

	def __init__(self,n):
		self.n = n 

	def pattern_logic_1(self):
		for i in range(self.n):
			for j in range(i+1):
				print("*" , end=" ")
			print()

	def pattern_logic_2(self):

		for i in range(self.n):
			print( str('*' + " ") * (i+1) , end="\n")


n = int(input("Enter n : "))
p = pattern1(n)
p.pattern_logic_1()
print()
p.pattern_logic_2()
