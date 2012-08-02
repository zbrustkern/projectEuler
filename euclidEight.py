def euclidEight():
	f = open('/Users/aliliang/Documents/Project Euler/prob8num.txt', 'r')
	d = f.readline()
	#d for digits
	largest = 1
	for i in range(0, len(d)-4, 1):
		if largest < int(d[i]) * int(d[1+i]) * int(d[i+2]) * int(d[i+3]) * int(d[i+4]):
			largest = int(d[i]) * int(d[1+i]) * int(d[i+2]) * int(d[i+3]) * int(d[i+4])
	return largest



if __name__ == "__main__":
	print euclidEight()

