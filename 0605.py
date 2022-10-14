# -*- coding: utf-8 -*-

import csv
import sys

f = open(sys.argv[1])
for row in csv.reader(f):
	print(row)
f.close()