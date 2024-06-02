class pattern11:
	""" square pattern with alphabets in reverse of dictionary order """

	def __init__(self , n):
		self.n = n 


	def pattern_logic_1(self):

		for i in range(self.n):
			for j in range(self.n):

				print(f"{chr(69 - j) }", end=" ")
			print()


n = int(input("Enter n : "))
p = pattern11(n)
p.pattern_logic_1()
