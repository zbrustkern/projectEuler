def diffSums(a,b):
	x = 0
	y = 0
	for i in xrange(a,b+1,1):
		x += i
		y += i**2
	return x**2 - y

if __name__ == "__main__":
	print diffSums(1,100)