<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>新規予約</title>                  
</head>
  <body>
    <h2>予約変更</h2>
    <p>以下の内容に変更しました</p>
    <h3>変更前</h3>
    <li>タイトル：{{title_before}}</li>
    <li>氏名：{{name}}</li>
    <li>{{year_before}} 年 {{month_before}} 月 {{day_before}}日</li>
    <li>{{hour_before}}時から1時間</li>
    <li>{{room_before}}</li>
    <h3>変更後</h3>
    <li>タイトル：{{title}}</li>
    <li>氏名：{{name}}</li>
    <li>{{year}} 年 {{month}} 月 {{day}}日</li>
    <li>{{hour}}時から1時間</li>
    <li>{{room}}</li>
    <p><a href="/list/{{user_id}}">予約一覧</a></p>
    <p><a href="/">ログアウト</a></p>
  </body>
</html>