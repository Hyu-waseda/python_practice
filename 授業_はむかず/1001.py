import lmdb

env = lmdb.Environment("db")
with env.begin(write=True) as txn:
	txn.put(b"key1", b"value1")
	txn.put(b"key2", b"value2")