k = int(input("Enter k = "))
r = int(input("Enter r = "))
x0 = int(input("Enter x0 < 2^k = "))

n = int(input("How many pserandom number you need? = "))

while (n):
	x0 = r*x0 % pow(2,k)
	print(x0/pow(2,k))


	n -= 1


	"""
	k = 7	r = 5 	x0 = 3
	answer: x1 = 0.1172 x2 = 0.5859 x3 = 0.9297

	k = 7	r = 5 	x0 = 9
	answer: x1 = 0.3516 x2 = 0.7578 x3 = 0.7891
		
	"""