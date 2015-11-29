for i in range(1,100):
	is_simple = True
	for m in range(2,i):
		if i % m == 0:
			is_simple = False
			break
	if is_simple:
		print i