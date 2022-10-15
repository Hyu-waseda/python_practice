from bottle import route, run, view
from datetime import datetime

@route("/")
@view("1106a")
def root():
	now = datetime.now()
	return {"hour": now.hour, "minute": now.minute,
			"second": now.second}

run()