<!DOCTYPE HTML>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>予約削除完了</title>
</head>
	<body>
	<ul>
		<p>以下の内容を削除しました</p>
		<li>タイトル：{{title}}</li>
		<li>氏名：{{name}}</li>
		<li>{{year}} 年 {{month}} 月 {{day}}日</li>
		<li>{{hour}}時から1時間</li>
		<li>{{room}}</li>
	</ul>
	<p><a href="/entry/{{user_id}}">新規予約</a></p>
	<p><a href="/list/{{user_id}}">予約一覧</a></p>
	<p><a href="/">ログアウト</a></p>
</html>
