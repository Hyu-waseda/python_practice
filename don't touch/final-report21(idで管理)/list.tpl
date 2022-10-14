<!DOCTYPE HTML>
<html lang="ja">
<head>
<meta charset="UTF-8"></head>
<title>予約一覧</title>
<body>
<h2>予約一覧</h2>
<p><a href="/search/{{data[0]["user_id"]}}">条件付きで予約検索</a></p>
<p>会議室A</p>
<table border="2" style="border-collapse: collapse">
<tr><td width="150">年月日</td><td width="100">利用時間</td><td width="150">利用目的</td><td width="95">利用者名</td></tr>
</table>
%for d in data:
	%if len(d) == 7 and d["room"] == "会議室A":
		<table border="1" style="border-collapse: collapse">
		<tr><td width="150">{{d["year"]}}年{{d["month"]}}月{{d["day"]}}日</td><td width="100">{{d["hour"]}}時〜{{d["hour"]+1}}時</td><td width="150">{{d["title"]}}</td><td width="95">{{d["name"]}}</td></tr>
		</table>
	%end
%end
<p>会議室B</p>
<table border="2" style="border-collapse: collapse">
<tr><td width="150">年月日</td><td width="100">利用時間</td><td width="150">利用目的</td><td width="95">利用者名</td></tr>
</table>
%for d in data:
%if len(d) == 7 and d["room"] == "会議室B":
<table border="1" style="border-collapse: collapse">
<tr><td width="150">{{d["year"]}}年{{d["month"]}}月{{d["day"]}}日</td><td width="100">{{d["hour"]}}時〜{{d["hour"]+1}}時</td><td width="150">{{d["title"]}}</td><td width="95">{{d["name"]}}</td></tr>
</table>
%end
%end
<p>会議室C</p>
<table border="2" style="border-collapse: collapse">
<tr><td width="150">年月日</td><td width="100">利用時間</td><td width="150">利用目的</td><td width="95">利用者名</td></tr>
</table>
%for d in data:
%if len(d) == 7 and d["room"] == "会議室C":
<table border="1" style="border-collapse: collapse">
<tr><td width="150">{{d["year"]}}年{{d["month"]}}月{{d["day"]}}日</td><td width="100">{{d["hour"]}}時〜{{d["hour"]+1}}時</td><td width="150">{{d["title"]}}</td><td width="95">{{d["name"]}}</td></tr>
</table>
%end
%end
<p><a href="/entry/{{data[0]["user_id"]}}">新規予約</a></p>
</body>
</html>