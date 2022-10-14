import lmdb
import bottle

template1 = """<!DOCTYPE HTML>
<html>
<head>
</head>
<body>
	<h1>ようこそ</h1>
	<p>あなたは{{c}}人目の来場者です。</p>
</body>
</html>
"""

env = lmdb.Environment("dbcount")

def get_count():
	with env.begin(write=True) as txn:
		count = txn.get(b"count")
		if count is None:
			c=0
		else:
			c = int(count.decode("utf8"))
		c += 1
		txn.put(b"count", str(c).encode("utf8"))
	return c



@bottle.route("/")
@bottle.view("11")
def root():
	c = get_count()
	return bottle.template(template1, c=c)
	
bottle.run()




