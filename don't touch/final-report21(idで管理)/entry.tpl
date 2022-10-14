<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>予約登録</title>
</head>
  <body>
    <h2>予約登録</h2>
    <form method="POST" action="/submit/{{str(data["user_id"])}}">
      <p>タイトル：<input type="text" name="title" required/></p>
      <p>氏名：{{data["user_name"]}}<input type="hidden" name="name" value = {{data["user_name"]}} required/></p>
      <p>日付：<input type="date" name="date" required></input></p>
      <p>時間：<select name="hour" required>
      % for d in range(0, 24):
        <option value= {{d}}>{{d}}</option>
      % end
        <option value=0>0</option>
        <option value=1>1</option>
        <option value=2>2</option>
        <option value=3>3</option>
        <option value=4>4</option>
        <option value=5>5</option>
        <option value=6>6</option>
        <option value=7>7</option>
        <option value=8>8</option>
        <option value=9>9</option>
        <option value=10>10</option>
        <option value=11>11</option>
        <option value=12>12</option>
        <option value=13>13</option>
        <option value=14>14</option>
        <option value=15>15</option>
        <option value=16>16</option>
        <option value=17>17</option>
        <option value=18>18</option>
        <option value=19>19</option>
        <option value=20>20</option>
        <option value=21>21</option>
        <option value=22>22</option>
        <option value=23>23</option>
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
  </body>
</html>