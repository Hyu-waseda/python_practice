import bottle
from datetime import datetime
@bottle.route("/")
def root():
	n=datetime.now()
	return f"今の日時 : {n}"
bottle.run()