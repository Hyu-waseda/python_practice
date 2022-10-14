import json

f = open("sample.json")

data = json.load(f)

for x in data:
	print(x[])