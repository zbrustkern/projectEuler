def naturalRangeAdder(min, max):
	x = 0
	for i in range (min, max):
		if i % 3 == 0 or i % 5 == 0:
			x = x + i
	return x
	
if __name__ == "__main__":
	print naturalRangeAdder(0,1000)