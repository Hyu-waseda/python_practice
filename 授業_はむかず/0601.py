f = open("data.txt")
for line in f:
	line = line.rstrip()
	print(line)
f.close()