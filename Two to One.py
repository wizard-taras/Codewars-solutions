def longest(a1, a2):
	l = list(a1 + a2)
	
	for i in l:
		while l.count(i) != 1:
			l.reverse()
			l.remove(i)
			l.reverse()
	l.sort()
	return ''.join(l)