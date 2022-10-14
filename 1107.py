 from bottle import route, run, view, static_file, redirect
 from datetime import datetime


@route("/datetime")
@view("1106a")
def dt():
	run()
	now = datetime.now()
	return {"hour": now.hour, "minute": now.minute,
			"second": now.second}

@route("/static/<path:path>")
def static(path):
	return static_file(path,root="./static")

@route("/")
def root():
	return redirect("/static/index.html")