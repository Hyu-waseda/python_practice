<script type="text/javascript">
  function isCheck() {
    var arr_checkBoxes = document.getElementsByClassName("check");
    var count = 0;
    for (var i = 0; i < arr_checkBoxes.length; i++) {
        if (arr_checkBoxes[i].checked) {
            count++;
        }
    }
    if (count == 1) {
        return true;
    } else {
        window.alert("予約時間は1時間までです。");
        return false;
    };
  }
</script>


<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="UTF-8">
    <title>新規予約</title>                  
  </head>
  <body>
    <h2>新規予約</h2>
    <form method="POST" onsubmit="return isCheck()" action="/submit/{{str(data[0]["user_id"])}}">
      <p>タイトル：<input type="text" name="title" required/></p>
      <p>氏名：{{data[0]["user_name"]}}<input type="hidden" name="name" value = {{data[0]["user_name"]}} required/></p>
      <p>※予約は１ヶ月後までしか選べません</p>
    <table border="1" style="border-collapse: collapse">
      <tr>
        <td width="140"></td>
        % for d in range(0, 24):
            <td width="35">{{d}}時</td>
        % end
      </tr>
    <p>会議室A</p>
		</table>
    % for d in data:
      % if len(d) == 27:
        <table border="1" style="border-collapse: collapse">
          <tr>
            <td width="140">{{d["year"]}}年{{d["month"]}}月{{d["day"]}}日</td>
            % for h in range(0, 24):
              % if d[str(h)]["room_a"] == "Yes":
                <td width="35">
                    <input type="checkbox" name="date" class="check" value = {{str(d["year"]) + "-" + str(d["month"]) + "-" + str(d["day"]) + "-" + str(h) + "-" + "会議室A"}}>
                </td>
              % else:
                <td width="35">
                ×
                </td>
              % end
            % end
          </tr>
				</table>
      % end
    % end
    <table border="1" style="border-collapse: collapse">
      <tr>
        <td width="140"></td>
        % for d in range(0, 24):
            <td width="35">{{d}}時</td>
        % end
      </tr>
    <p>会議室B</p>
		</table>
    % for d in data:
      % if len(d) == 27:
        <table border="1" style="border-collapse: collapse">
          <tr>
            <td width="140">{{d["year"]}}年{{d["month"]}}月{{d["day"]}}日</td>
            % for h in range(0, 24):
              % if d[str(h)]["room_b"] == "Yes":
                <td width="35">
                    <input type="checkbox" name="date" class="check" value = {{str(d["year"]) + "-" + str(d["month"]) + "-" + str(d["day"]) + "-" + str(h) + "-" + "会議室B"}}>
                </td>
              % else:
                <td width="35">
                ×
                </td>
              % end
            % end
          </tr>
				</table>
      % end
    % end
    <table border="1" style="border-collapse: collapse">
      <tr>
        <td width="140"></td>
        % for d in range(0, 24):
            <td width="35">{{d}}時</td>
        % end
      </tr>
    <p>会議室C</p>
		</table>
    % for d in data:
      % if len(d) == 27:
        <table border="1" style="border-collapse: collapse">
          <tr>
            <td width="140">{{d["year"]}}年{{d["month"]}}月{{d["day"]}}日</td>
            % for h in range(0, 24):
              % if d[str(h)]["room_c"] == "Yes":
                <td width="35">
                    <input type="checkbox" name="date" class="check" value = {{str(d["year"]) + "-" + str(d["month"]) + "-" + str(d["day"]) + "-" + str(h) + "-" + "会議室C"}}>
                </td>
              % else:
                <td width="35">
                ×
                </td>
              % end
            % end
          </tr>
				</table>
      % end
    % end
    <input type="submit"　/>
    </form>
    <p><a href="/list/{{data[0]["user_id"]}}">予約一覧</a></p>
    <p><a href="/">ログアウト</a></p>
  </body>
</html>