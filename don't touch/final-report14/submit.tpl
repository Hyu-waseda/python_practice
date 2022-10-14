<!DOCTYPE HTML>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>登録完了</title>
</head>
<body>
% if year == 1:
<h2>予約エラー</h2>
<p>予約が重複しています</p>
<p><a href="/">新規予約</a></p>
<p><a href="/list">予約一覧</a></p>
% elif year == 2:
<h2>予約エラー</h2>
<p>日付が不適切です</p>
<p><a href="/">新規予約</a></p>
<p><a href="/list">予約一覧</a></p>
% else:
<ul>
<p>以下の内容で登録しました</p>
<li>タイトル：{{title}}</li>
<li>氏名：{{name}}</li>
<li>{{year}} 年 {{month}} 月 {{day}}日</li>
<li>{{hour}}時から1時間</li>
<li>{{room}}</li>
</ul>
<p><a href="/">新規予約</a></p>
<p><a href="/list">予約一覧</a></p>
% end
</html>
