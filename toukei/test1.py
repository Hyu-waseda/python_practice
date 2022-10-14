from re import S
import numpy as np
import matplotlib.pyplot as plt
# matplotlib.use('Agg') # この行を追記

s = "41 17 35 23 28 7 43 31 54 25 56 64 33 46 3 26 18 37 21 36 13 47 58 55 27 37 44 59 44 27 50 52 52 61 62 66 48 18 40 11 32 48 30 22 40 51 26 68 57 32 23 45 34 41 20 39 29 24 30 42"
# s = "27 30 37 14 21 41 11 15 36 3 17 45 8 27 25 33 28 47 22 2 40 29 12 52 18 32 9 34 31 42 29 12 16 38 6 49 13 33 36 26 23 46 28 10 54 14 26 43 35 39 34 37 32 50 5 20 57 24 61 22"
# x = np.random.normal(50, 10, 1000)
x = s.split(" ")
for i, v in enumerate(x):
	x[i] = int(v)

print(x)
plt.hist(x, bins=20)

plt.savefig("z1.png") # この行を追記