print("数字を入力してください")
x = input()
n = int(x)
s = 0
for i in range(1, n+1):
	s += i
print(f"1から{n}までの和は{s}です")