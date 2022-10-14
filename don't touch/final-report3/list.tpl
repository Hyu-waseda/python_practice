<!DOCTYPE HTML>
<html lang="ja">
<head>
<meta charset="UTF-8"></head>
<title>予約一覧</title>
<body>
<h2>予約一覧</h2>
%for d in data:
<p>{{d["room"]}} {{d["year"]}}年{{d["month"]}}月{{d["day"]}}日{{d["hour"]}}, {{d["title"]}}, {{d["name"]}}</p>
%end
<p><a href="/">新規予約</a></p>
</body>
</html>