<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>予約検索</title>
</head>
	<body>
		<h2>予約検索</h2>
		<form method="POST" action="/search_result/{{user_id}}">
			<p>氏名：<input type="text" name="name"/></p>
			<p>日付：<input type="date" name="date"></input></p>
			<p><select name="room">
			<option value="">会議室を選択</option>
			<option value="会議室A">会議室A</option>
			<option value="会議室B">会議室B</option>
			<option value="会議室C">会議室C</option>
			</select></p>
			<input type="submit"  value="検索"/>
		</form>
		<p><a href="/list/{{user_id}}">予約一覧</a></p>
		<p><a href="/">ログアウト</a></p>
	</body>
</html>