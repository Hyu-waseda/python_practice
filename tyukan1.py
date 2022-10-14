#３があるかどうかをチェックする関数
def check_3(n):
	while n != 0:
		tmp = n % 10
		n /= 10
		if tmp == 3:
			return True

#1から1000までチェックし、３があれば出力
for n in range(1, 1001):
	if check_3(n):
		print(n)
