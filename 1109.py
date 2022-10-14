import bottle
 tpl = """<!DOCTYPE HTML>
 <html><head></head>
 <body><p>パラメータの値は<br/>{{a}}<br/>です</p></body>
 </html>"""
 @bottle.route("/")
 def root():
 return bottle.static_file(“1109.html", root="./static")
 @bottle.get("/param")
 def param():
 a = bottle.request.params.a
 return bottle.template(tpl, a=a)
bottle.run()