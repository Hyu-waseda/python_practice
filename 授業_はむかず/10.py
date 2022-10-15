
import csv
import lmdb
import json


env = lmdb.Environment("nikkei")

with open("nikkei_stock_average_daily_jp.csv", encoding="sjis") as f:
	reader = csv.reader(f)
	next(reader)
	for row in csv.reader(f):
		if len(row)>1:
			with env.begin(write=True) as txn:
				key = row[0].encode("utf-8")
				d = {"終値":row[1],"始値":row[2],"高音":row[3],"安値":row[4]}
				value = json.dumps(d)
				bvalue = value.encode("utf-8")

with env.begin() as txn:	

"""
import csv
import lmdb
import json

env = lmdb.Environment("nikkei")

with open("nikkei_stock_average_daily_jp.csv", encoding="sjis") as f:
	reader = csv.reader(f)
	next(reader)
	for row in reader:
		if len(row) > 1:
			with env.begin(write=True) as txn:
				bkey = row[0].encode("utf-8")
				d = {"終値": row[1], "始値": row[2], "高値": row[3], "安値": row[4]}
				value = json.dumps(d)
				bvalue = value.encode("utf-8")
				txn.put(bkey, bvalue)

with env.begin() as txn:
	bvalue = txn.get(b"2020/10/01")
	d = json.loads(bvalue.decode("utf-8"))
	print("2020年10月1日の日経平均")
	print("始値:{}".format(d["始値"]))
	print("終値:{}".format(d["終値"]))
	print("高値:{}".format(d["高値"]))
	print("安値:{}".format(d["安値"]))
	"""