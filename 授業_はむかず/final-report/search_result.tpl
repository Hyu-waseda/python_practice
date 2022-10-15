<!DOCTYPE HTML>
<html lang="ja">
<head>
<meta charset="UTF-8"></head>
<title>条件付き予約検索結果</title>
	<body>
		<h2>条件付き予約検索結果</h2>
		<p><a href="/search/{{data[0]["user_id"]}}">条件付きで予約検索</a></p>
		<p>会議室A</p>
		<table border="2" style="border-collapse: collapse">
			<tr><td width="150">年月日</td><td width="100">利用時間</td><td width="150">利用目的</td><td width="95">利用者名</td></tr>
		</table>
		%for d in data:
			%if len(d) == 8 and d["room"] == "会議室A":
				%if d["user_id"] == data[0]["user_id"] or data[0]["user_id"] == "admin":
					<table border="1" style="border-collapse: collapse">
						<tr><td width="150">{{d["year"]}}年{{d["month"]}}月{{d["day"]}}日</td><td width="100">{{d["hour"]}}時〜{{d["hour"]+1}}時</td><td width="150">{{d["title"]}}</td><td width="95">{{d["name"]}}</td>
							<td width="50">
								<form method="POST" action="/change/{{str(data[0]["user_id"])}}">
									<input type="hidden" name="title" value = {{d["title"]}} required/>
									<input type="hidden" name="name" value = {{d["name"]}} required/>
									<input type="hidden" name="year" value = {{d["year"]}} required></input>
									<input type="hidden" name="month" value = {{d["month"]}} required></input>
									<input type="hidden" name="day" value = {{d["day"]}} required></input>
									<input type="hidden" name="hour" value = {{d["hour"]}} required></input>
									<input type="hidden" name="room" value = {{d["room"]}} required></input>
									<input type="hidden" name="user_id" value = {{d["user_id"]}} required></input>
									<input type="submit" value = "変更"/>
								</form>
							</td>
							<td width="50">
								<form method="POST" action="/delete/{{str(data[0]["user_id"])}}">
									<input type="hidden" name="title" value = {{d["title"]}} required/>
									<input type="hidden" name="name" value = {{d["name"]}} required/>
									<input type="hidden" name="year" value = {{d["year"]}} required></input>
									<input type="hidden" name="month" value = {{d["month"]}} required></input>
									<input type="hidden" name="day" value = {{d["day"]}} required></input>
									<input type="hidden" name="hour" value = {{d["hour"]}} required></input>
									<input type="hidden" name="room" value = {{d["room"]}} required></input>
									<input type="hidden" name="user_id" value = {{d["user_id"]}} required></input>
									<input type="submit" value = "削除"/>
								</form>
							</td>
						</tr>
					</table>
				%else:
					<table border="1" style="border-collapse: collapse">
						<tr><td width="150">{{d["year"]}}年{{d["month"]}}月{{d["day"]}}日</td><td width="100">{{d["hour"]}}時〜{{d["hour"]+1}}時</td><td width="150">{{d["title"]}}</td><td width="95">{{d["name"]}}</td></tr>
					</table>
				%end
			%end
		%end
		<p>会議室B</p>
		<table border="2" style="border-collapse: collapse">
			<tr><td width="150">年月日</td><td width="100">利用時間</td><td width="150">利用目的</td><td width="95">利用者名</td></tr>
		</table>
		%for d in data:
			%if len(d) == 8 and d["room"] == "会議室B":
				%if d["user_id"] == data[0]["user_id"] or data[0]["user_id"] == "admin":
					<table border="1" style="border-collapse: collapse">
						<tr><td width="150">{{d["year"]}}年{{d["month"]}}月{{d["day"]}}日</td><td width="100">{{d["hour"]}}時〜{{d["hour"]+1}}時</td><td width="150">{{d["title"]}}</td><td width="95">{{d["name"]}}</td>
							<td width="50">
								<form method="POST" action="/change/{{str(data[0]["user_id"])}}">
									<input type="hidden" name="title" value = {{d["title"]}} required/>
									<input type="hidden" name="name" value = {{d["name"]}} required/>
									<input type="hidden" name="year" value = {{d["year"]}} required></input>
									<input type="hidden" name="month" value = {{d["month"]}} required></input>
									<input type="hidden" name="day" value = {{d["day"]}} required></input>
									<input type="hidden" name="hour" value = {{d["hour"]}} required></input>
									<input type="hidden" name="room" value = {{d["room"]}} required></input>
									<input type="hidden" name="user_id" value = {{d["user_id"]}} required></input>
									<input type="submit" value = "変更"/>
								</form>
							</td>
							<td width="50">
								<form method="POST" action="/delete/{{str(data[0]["user_id"])}}">
									<input type="hidden" name="title" value = {{d["title"]}} required/>
									<input type="hidden" name="name" value = {{d["name"]}} required/>
									<input type="hidden" name="year" value = {{d["year"]}} required></input>
									<input type="hidden" name="month" value = {{d["month"]}} required></input>
									<input type="hidden" name="day" value = {{d["day"]}} required></input>
									<input type="hidden" name="hour" value = {{d["hour"]}} required></input>
									<input type="hidden" name="room" value = {{d["room"]}} required></input>
									<input type="hidden" name="user_id" value = {{d["user_id"]}} required></input>
									<input type="submit" value = "削除"/>
								</form>
							</td>
						</tr>
					</table>
				%else:
					<table border="1" style="border-collapse: collapse">
						<tr><td width="150">{{d["year"]}}年{{d["month"]}}月{{d["day"]}}日</td><td width="100">{{d["hour"]}}時〜{{d["hour"]+1}}時</td><td width="150">{{d["title"]}}</td><td width="95">{{d["name"]}}</td></tr>
					</table>
				%end
			%end
		%end
		<p>会議室C</p>
		<table border="2" style="border-collapse: collapse">
			<tr><td width="150">年月日</td><td width="100">利用時間</td><td width="150">利用目的</td><td width="95">利用者名</td></tr>
		</table>
		%for d in data:
			%if len(d) == 8 and d["room"] == "会議室C":
				%if d["user_id"] == data[0]["user_id"] or data[0]["user_id"] == "admin":
					<table border="1" style="border-collapse: collapse">
						<tr><td width="150">{{d["year"]}}年{{d["month"]}}月{{d["day"]}}日</td><td width="100">{{d["hour"]}}時〜{{d["hour"]+1}}時</td><td width="150">{{d["title"]}}</td><td width="95">{{d["name"]}}</td>
							<td width="50">
								<form method="POST" action="/change/{{str(data[0]["user_id"])}}">
									<input type="hidden" name="title" value = {{d["title"]}} required/>
									<input type="hidden" name="name" value = {{d["name"]}} required/>
									<input type="hidden" name="year" value = {{d["year"]}} required></input>
									<input type="hidden" name="month" value = {{d["month"]}} required></input>
									<input type="hidden" name="day" value = {{d["day"]}} required></input>
									<input type="hidden" name="hour" value = {{d["hour"]}} required></input>
									<input type="hidden" name="room" value = {{d["room"]}} required></input>
									<input type="hidden" name="user_id" value = {{d["user_id"]}} required></input>
									<input type="submit" value = "変更"/>
								</form>
							</td>
							<td width="50">
								<form method="POST" action="/delete/{{str(data[0]["user_id"])}}">
									<input type="hidden" name="title" value = {{d["title"]}} required/>
									<input type="hidden" name="name" value = {{d["name"]}} required/>
									<input type="hidden" name="year" value = {{d["year"]}} required></input>
									<input type="hidden" name="month" value = {{d["month"]}} required></input>
									<input type="hidden" name="day" value = {{d["day"]}} required></input>
									<input type="hidden" name="hour" value = {{d["hour"]}} required></input>
									<input type="hidden" name="room" value = {{d["room"]}} required></input>
									<input type="hidden" name="user_id" value = {{d["user_id"]}} required></input>
									<input type="submit" value = "削除"/>
								</form>
							</td>
						</tr>
					</table>
				%else:
					<table border="1" style="border-collapse: collapse">
						<tr><td width="150">{{d["year"]}}年{{d["month"]}}月{{d["day"]}}日</td><td width="100">{{d["hour"]}}時〜{{d["hour"]+1}}時</td><td width="150">{{d["title"]}}</td><td width="95">{{d["name"]}}</td></tr>
					</table>
				%end
			%end
		%end
		<p><a href="/list/{{data[0]["user_id"]}}">予約一覧</a></p>
		<p><a href="/entry/{{data[0]["user_id"]}}">新規予約</a></p>
		<p><a href="/">ログアウト</a></p>
	</body>
</html>