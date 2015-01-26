from math import pow

def checkTriangle():
	triangle = []
	for i in range(3):
		a = int(raw_input("Enter a side of the triangle: "))
		triangle.append(a)

	triangle.sort()

	if((pow(triangle[0], 2) + pow(triangle[1], 2)) == pow(triangle[2], 2)):
		print "Yes, it is a pythaogrean triple."
	else:
		print "No, it is not a pythaogrean triple."
	
	choice = raw_input("Try again? y/n: " )
	if choice == 'y':
		checkTriangle()
		
checkTriangle()


