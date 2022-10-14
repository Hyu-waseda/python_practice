<!DOCTYPE HTML>
<html lang="ja">
<head>
<meta charset="UTF-8"></head>
<title>予約一覧</title>
<body>
<h2>予約一覧</h2>
<p>会議室A</p>
%for d in data:
%if d["room"] == "会議室A":
<p>{{d["year"]}}年{{d["month"]}}月{{d["day"]}}日{{d["hour"]}}, {{d["title"]}}, {{d["name"]}}</p>
%end
%end
<p>会議室B</p>
%for d in data:
%if d["room"] == "会議室B":
<p>
{{d["year"]}}年{{d["month"]}}月{{d["day"]}}日{{d["hour"]}}, {{d["title"]}}, {{d["name"]}}</p>
%end
%end
<p>会議室C</p>
%for d in data:
%if d["room"] == "会議室C":
<p>{{d["year"]}}年{{d["month"]}}月{{d["day"]}}日{{d["hour"]}}, {{d["title"]}}, {{d["name"]}}</p>
%end
%end
<p><a href="/">新規予約</a></p>
</body>
</html>