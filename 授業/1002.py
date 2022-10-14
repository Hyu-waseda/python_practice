import lmdb

env = lmdb.Environment("db")
with env.begin() as txn:
	v1 = txn.get(b"key1")
	print(v1.decode("utf-8"))
	v2 = txn.get(b"key3")
	print(v2)