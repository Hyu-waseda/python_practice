<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>新規予約</title>                  
</head>
  <body>
    <h2>新規予約</h2>
    <form method="POST" action="/submit/{{str(data["user_id"])}}">
      <p>タイトル：<input type="text" name="title" required/></p>
      <p>氏名：{{data["user_name"]}}<input type="hidden" name="name" value = {{data["user_name"]}} required/></p>
      <p>日付：<input type="date" name="date" required></input></p>
      <p>時間：<select name="hour" required>
      % for d in range(0, 24):
        <option value= {{d}}>{{d}}</option>
      % end
        </select>時から1時間</p>
      <p>※予約は１ヶ月後までしか選べません</p>
      <p><select name="room" required>
        <option value="会議室A">会議室A</option>
        <option value="会議室B">会議室B</option>
        <option value="会議室C">会議室C</option>
        </select></p>
      <input type="submit" />
    </form>
    <p><a href="/list/{{data["user_id"]}}">予約一覧</a></p>
    <p><a href="/">ログアウト</a></p>
  </body>
</html>