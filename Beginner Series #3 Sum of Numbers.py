def get_sum(a,b):
	nums = []
	if a < b:
		ll = a
		ul = b
		for i in range(ll, ul + 1): nums.append(i)
		snums = sum(nums)
	elif b < a:
		ll = b
		ul = a
		for i in range(ll, ul + 1): nums.append(i)
		snums = sum(nums)
	else:
		snums = a
	
	return snums