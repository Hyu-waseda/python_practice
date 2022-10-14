<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>新規予約</title>                  
</head>
  <body>
    <h2>予約変更</h2>
    <h3>変更前</h3>
    <li>タイトル：{{title}}</li>
    <li>氏名：{{name}}</li>
    <li>{{year}} 年 {{month}} 月 {{day}}日</li>
    <li>{{hour}}時から1時間</li>
    <li>{{room}}</li>
    <h3>変更後</h3>
    <form method="POST" action="/change_result/{{user_id}}">
      <p>タイトル：<input type="text" name="title" placeholder={{title}} required/></p>
      <p>氏名：{{name}}<input type="hidden" name="name" value = {{name}} required/></p>
      <p>日付：<input type="date" name="date" required></input></p>
      <p>時間：<select name="hour" placeholder={{hour}} required>
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
      <input type="hidden" name="title_before" value = {{title}} required/>
			<input type="hidden" name="name_before" value = {{name}} required/>
			<input type="hidden" name="year_before" value = {{year}} required></input>
			<input type="hidden" name="month_before" value = {{month}} required></input>
			<input type="hidden" name="day_before" value = {{day}} required></input>
			<input type="hidden" name="hour_before" value = {{hour}} required></input>
			<input type="hidden" name="room_before" value = {{room}} required></input>
			<input type="hidden" name="user_id" value = {{user_id}} required></input>
      <input type="submit" />
    </form>
    <p><a href="/list/{{user_id}}">予約一覧</a></p>
    <p><a href="/">ログアウト</a></p>
  </body>
</html>