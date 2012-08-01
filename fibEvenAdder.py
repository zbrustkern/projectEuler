def fibEvenAdder():
	x = 0
	i = 2
	j = 1
	k = 0
	while i < 4000000:
		if i % 2 == 0:
			x += i
		k = i
		i += j
		j = k
	return x


print fibEvenAdder()