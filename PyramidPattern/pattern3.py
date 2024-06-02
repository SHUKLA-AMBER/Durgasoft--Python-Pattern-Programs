class pattern3:

	def __init__(self,n):
		self.n = n


	def pattern_logic_1(self):

		for z in range( self.n ):

			# Spaces
			for i in range(self.n-(z+1)):
				print("_",end="")


			#Characters first hafe
			for k in range((2 * (z+1) - 1)):

				if k % 2 == 0:
					print( chr(65+z) , end= "")
				else:
					print("_", end="")

				# print()

			print()


	def pattern_logic_2(self):

		for i in range(self.n):

			print(" "*(self.n-i -1) , end="")

			print(f"{chr(65+i)} "* (i+1) , end="")	
			print()		


n = 5
p = pattern3(n)
p.pattern_logic_1()
p.pattern_logic_2()