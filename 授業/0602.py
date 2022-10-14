fr = open("data.txt")
fw = open("data2.txt", "w")
for line in fr:
	line = line.rstrip()
	print(line, file=fw)
fr.close()
fw.close()