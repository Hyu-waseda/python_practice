import lmdb

env = lmdb.Environment("db")
with env.begin() as txn:
	cur = txn.cursor()
	for k, v in cur:
		print("{},{}".format(k.decode("utf-8"), v.decode("utf-8")))