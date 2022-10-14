import sys
from collections import Counter

counter = Counter()

with open(sys.argv[1]) as f:
	for line in f:
		line = line.rstrip()
		words = line.split(" ")
		#print(words)
		for w in words:
			if w != "":
				counter[w] += 1
print(counter.most_common(5))