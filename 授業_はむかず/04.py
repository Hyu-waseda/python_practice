def sum_list(list):
	sum = 0
	for n in list:
		sum += n
	return sum

list = [1, 2, 3, 4, 5]
print(sum_list(list))

def is_leap(n):
	if(n % 400 == 0):
		return True
	if(n % 4 == 0):
		if(n % 100 == 0):
			return False
		else:
			return True

print(is_leap(2004))
print(is_leap(2000))
print(is_leap(1900))

