import bottle
from datetime import datetime

template1 = """<!DOCTYPE HTML>
<html>
<head>
</head>
<body>
	<h1>現在の日時</h1>
	<p>今日は{{year}}年{{month}}月{{day}}日です。</p>
	<p>現在の時刻は{{hour}}時{{minute}}分{{second}}秒です</p>
</body>
</html>
"""

@bottle.route("/")
def root():
	now = datetime.now()
	return bottle.template(template1, year=now.year,
							month=now.month, day=now.day,
							hour=now.hour, minute=now.minute,
							second=now.second)
bottle.run()