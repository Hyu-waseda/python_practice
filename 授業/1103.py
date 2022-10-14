import bottle

html_doc="""
<!DOCTYPE HTML>
<html>
<head>
<title>Hello</title>
</head>
<body>
<h1>Hello!</h1>
</body>
</html>
"""
@bottle.route("/")
def root():
	return html_doc

bottle.run()