from multiprocessing import Process, freeze_support
import lmdb

env = lmdb.Environment("count")

def countup_db():
	with env.begin(write=True) as txn:
		b = txn.get(b"count")
		count = int(b)
		count += 1
		txn.put(b"count", str(count).encode("utf-8"))


def main():
	with env.begin(write=True) as txn:
		txn.put(b"count", b"0")
	jobs = []
	n_jobs = 100
	for i in range(n_jobs):
		p = Process(target=countup_db)
		jobs.append(p)
		p.start()
	for i in range(n_jobs):
		jobs[i].join()
	with env.begin() as txn:
		count = int(txn.get(b"count"))
		print(count)

if __name__ == "__main__":
 	main()