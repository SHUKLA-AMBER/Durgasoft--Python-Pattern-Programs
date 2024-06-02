class pattern6:

	def __init__(self,n):
		self.n = n 


	def pattern_logic_1(self):

		for i in range(self.n):

			#spaces 
			print("_" * (self.n -1 -i) , end="")


			for j in range((i+1)):

				print(f"{chr(65+j)} " , end="")


			print()



n = int(input("Enter n : "))
pattern6(n).pattern_logic_1()
