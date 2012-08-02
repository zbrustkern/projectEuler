def pgtriplet(n):

	for j in range(1, n, 1):
		for h in range(2, n, 1):
			if j + h + ((j**2 + h**2)**0.5) == n:
				return j * h * int((j**2 + h**2)**0.5)
	

if __name__ == "__main__":
	print pgtriplet(1000)