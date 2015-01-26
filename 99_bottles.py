for i in range(99, 0, -1):
	b = ""
	c = ""
	if(i == 1):
		b = "bottle"
		c = "bottles"
	elif(i == 2):
		b = "bottles"
		c = "bottle"
	else:
		b = "bottles"
		c = "bottles"

	print "%d %s of beer on the wall" % (i, b)
	print "%d %s of beer" % (i, b)
	print "Take one down, pass it around"
	print "%d %s of beer on the wall\n" % (i - 1, c)
