import math

def keisan(p):
	return p * math.log(p, 2)

ans = 0
data = [64, 15, 10, 13, 3, 1]
s = 0
for d in data:
	s += d
s = float(s)
for d in data:
	ans += keisan(d/s)

print(-ans)