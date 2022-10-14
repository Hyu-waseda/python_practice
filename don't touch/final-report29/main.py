#学籍番号：1J20F037
#氏名：奥村飛悠

import bottle
import lmdb
import json
import datetime


env = lmdb.Environment("./dbreserve")
env1 = lmdb.Environment("./dbuser")


admin_name = "admin"
admin_password = "admin"
admin_email = "admin@gmail.com"


#id作成
def get_id(txn):
    cur = txn.cursor()
    ite = cur.iterprev()
    try:
        k, v = next(ite)
        last_id = int(k.decode("utf8"))
    except StopIteration:
        last_id = 0
    id = last_id + 1
    return "{:08d}".format(id)

#ユーザのアカウント情報をとってくる関数
def get_user_data(user_id):
    data = []
    with env1.begin() as txn:
        cur = txn.cursor()
        for k, v in cur:
            d = json.loads(v.decode("utf8"))
            if(k.decode("utf8") == user_id):
                d = json.loads(v.decode("utf8"))
                data.append(d)
                return data

#うるう年判定
def is_leap(n):
    if(n % 400 == 0):
        return True
    if(n % 4 == 0):
        if(n % 100 == 0):
            return False
        else:
            return True
    return False

#年月日時間のチェック
def is_ok_time(year, month, day, hour):
    dt_now = datetime.datetime.now()
    year = int(year)
    month = int(month)
    day = int(day)
    hour = int(hour)

    #過去の日付はFalse
    if(year < dt_now.year):
        return False
    elif(year == dt_now.year):
        if(month < dt_now.month):
            return False
        elif(month == dt_now.month):
            if(day < dt_now.day):
                return False
            elif(day == dt_now.day):
                if(hour <= dt_now.hour):
                    return False

    #存在しない日付はFalse
    if(month < 1 or 12 < month or day < 1 or 31 < day or hour < 0 or 24 < hour):
        return False
    elif(month == 2 or month == 4 or month == 6 or month == 9 or month == 11):
        if(day > 30):
            return False
    if(month == 2):
        if(day >= 30):
            return False
        if((not is_leap(year)) and day >= 29):
            return False


    #予約は１ヶ月後まで
    if(not month == 1):
        if(year > dt_now.year or month - dt_now.month > 2):
            return False
        elif(month - dt_now.month == 1):
            if(day > dt_now.day):
                return False
    elif(month == 1 and dt_now.month == 12 and year - dt_now.year == 1):
        if(day > dt_now.day):
                return False
    return True

#部屋の重複をチェック
def is_ok_room(year, month, day, hour, room):
    data = []
    with env.begin() as txn:
        cur = txn.cursor()
        for k, v in cur:
            d = json.loads(v.decode("utf8"))
            data.append(d)
    for tmp in data:
        if(tmp["year"] == year and tmp["month"] == month and tmp["day"] == day and tmp["hour"] == hour and tmp["room"] == room):
            return False
    return True



@bottle.route("/")
def root():
    return bottle.static_file("home.html", root="./static")


@bottle.route("/signup")
def signup():
    return bottle.static_file("signup.html", root="./static")

@bottle.post("/signup1")
@bottle.view("signup")
def signup1():
    user_name = bottle.request.params.username
    password = bottle.request.params.password
    mail = bottle.request.params.mail
    data = {"user_name": user_name, "password": password, "mail": mail}
    if user_name == admin_name or password == admin_password or mail == admin_email:
        return bottle.template("error_signup.tpl", flag = 2)
    with env1.begin() as txn:
        cur = txn.cursor()
        for k, v in cur:
            d = json.loads(v.decode("utf8"))
            if(d["mail"] == mail):
                return bottle.template("error_signup.tpl", flag = 2)
    with env1.begin(write=True) as txn:
        id = get_id(txn)
        txn.put(id.encode("utf8"), json.dumps(data).encode("utf8"))
    print("新規アカウント登録" + " " + user_name + " " + password + " " + mail)
    return data


@bottle.route("/login")
def login():
    return bottle.static_file("login.html", root="./static")

@bottle.post("/login")
def do_login():
    user_name = bottle.request.params.user_name
    password = bottle.request.params.password
    mail = bottle.request.params.mail
    if user_name == admin_name and password == admin_password and mail == admin_email:
        return bottle.redirect("/entry/admin")
    with env1.begin() as txn:
        cur = txn.cursor()
        for k, v in cur:
            d = json.loads(v.decode("utf8"))
            if(d["user_name"] == user_name and d["password"] == password and d["mail"] == mail):
                return bottle.redirect("/entry/" + str(k.decode("utf8")))
    return bottle.template("error_login.tpl")


@bottle.route("/entry/<user_id>")
def entry(user_id):
    data = []
    if user_id == "admin":
        data = [{"user_id": "admin", "user_name": admin_name}]
    else:
        tmp = get_user_data(user_id)
        data = [{"user_id": user_id, "user_name": tmp[0]["user_name"]}]
    #data += [{"test": "test"}]
    d_today = datetime.date.today()
    for d in range(30):
        #print(d_today)
        today = str(d_today)
        tmp = today.split("-")
        year = int(tmp[0])
        month = int(tmp[1])
        day = int(tmp[2])
        tmp_data = {"year": year, "month": month, "day": day}
        for hour in range(0, 24):
            room_a = "no"
            room_b = "no"
            room_c = "no"
            if(is_ok_room(year, month, day, hour, "会議室A")):
                room_a = "Yes"
            if(is_ok_room(year, month, day, hour, "会議室B")):
                room_b = "Yes"
            if(is_ok_room(year, month, day, hour, "会議室C")):
                room_c = "Yes"
            room = {"room_a": room_a, "room_b": room_b, "room_c": room_c}
            tmp_data.update({str(hour): room})
        data += [tmp_data]
        d_today += datetime.timedelta(days=1)
    return bottle.template("entry.tpl", data = data)

@bottle.post("/submit/<user_id>")
@bottle.view("submit")
def submit(user_id):
    title = bottle.request.params.title
    name = ""
    if user_id == "admin":
        name = admin_name
    else:
        user_data = get_user_data(user_id)
        name = user_data[0]["user_name"]
    date = bottle.request.params.date
    tmp = date.split("-")
    year = int(tmp[0])
    month = int(tmp[1])
    day = int(tmp[2])
    hour = int(tmp[3])
    room = str(tmp[4])
    data = {"title": title, "name": name, "year": year, "month": month, "day": day, "hour": hour, "room": room, "user_id": user_id}
    if(is_ok_room(year, month, day, hour, room) == False):
        return bottle.template("error_submit_overlapping_time", user_id = user_id)
    elif(is_ok_time(year, month, day, hour) == False):
        return bottle.template("error_submit_not_exist_time", user_id = user_id)
    with env.begin(write=True) as txn:
        id = get_id(txn)
        txn.put(id.encode("utf8"), json.dumps(data).encode("utf8"))
        print(str(data["year"])+"年"+str(data["month"])+"月"+str(data["day"])+"日"+str(data["hour"])+"時〜"+str(int(data["hour"])+1)+"時"+str(data["room"])+"の予約を登録")
    return data


@bottle.route("/list/<user_id>")

@bottle.view("list")
def list(user_id):
    data = []
    with env.begin(write=True) as txn:
        cur = txn.cursor()
        for k, v in cur:
            d = json.loads(v.decode("utf8"))
            #過去の日付があったら削除
            if(is_ok_time(d["year"], d["month"], d["day"], d["hour"]) == False):
                txn.delete(k)
                print(str(d["year"])+"年"+str(d["month"])+"月"+str(d["day"])+"日"+str(d["hour"])+"時〜"+str(int(d["hour"])+1)+"時"+str(d["room"])+"の予約を削除")
            else:
                data.append(d)
    data_sorted = sorted(data, key=lambda x:(x["room"], int(x["year"]), int(x["month"]), int(x["day"]), int(x["hour"])))
    if user_id == "admin":
        data = [{"user_id": "admin", "user_name": admin_name}]
    else:
        user_data = get_user_data(user_id)
        data = [{"user_id": user_id, "user_name": user_data[0]["user_name"]}]
    data += data_sorted
    return {"data": data}


@bottle.route("/search/<user_id>")
def root(user_id):
    return bottle.template("search", user_id = user_id)

@bottle.post("/search_result/<user_id>")
@bottle.view("search_result")
def list(user_id):
    name = ""
    room = ""
    date = ""
    name = bottle.request.params.name
    room = bottle.request.params.room
    date = bottle.request.params.date
    year = ""
    month = ""
    day = ""
    if(name == "" and room == "" and date == ""):
        return bottle.template("error_search", user_id = user_id)
    if(not date == ""):
        tmp = date.split("-")
        year = int(tmp[0])
        month = int(tmp[1])
        day = int(tmp[2])
    tmp = []
    with env.begin() as txn:
        cur = txn.cursor()
        for k, v in cur:
            d = json.loads(v.decode("utf8"))
            if((name == "" or name == d["name"]) and (month == "" or month == d["month"]) and (day == "" or day == d["day"]) and (room == "" or room == d["room"])):
                tmp.append(d)
    data_sorted = sorted(tmp, key=lambda x:(x["room"], int(x["year"]), int(x["month"]), int(x["day"]), int(x["hour"])))
    #data[0]はユーザ名を保持
    data = [{"user_id": user_id}]
    data += data_sorted
    return {"data": data}


@bottle.route("/delete/<user_id>")

@bottle.post("/delete/<user_id>")
@bottle.view("delete")
def delete(user_id):
    name = bottle.request.params.name
    room = bottle.request.params.room
    year = int(bottle.request.params.year)
    month = int(bottle.request.params.month)
    day = int(bottle.request.params.day)
    hour = int(bottle.request.params.hour)
    data = []
    with env.begin(write=True) as txn:
        cur = txn.cursor()
        for k, v in cur:
            d = json.loads(v.decode("utf8"))
            if(d["name"] == name and d["room"] == room and d["year"] == year and d["month"] == month and d["day"] == day and d["hour"] == hour):
                txn.delete(k)
                print(str(d["year"])+"年"+str(d["month"])+"月"+str(d["day"])+"日"+str(d["hour"])+"時〜"+str(int(d["hour"])+1)+"時"+str(d["room"])+"の予約を削除")
                data.append(d)
    data = data[0]
    return data


@bottle.route("/change/<user_id>")

@bottle.post("/change/<user_id>")
@bottle.view("change")
def delete(user_id):
    title = bottle.request.params.title
    name = bottle.request.params.name
    room = bottle.request.params.room
    year = int(bottle.request.params.year)
    month = int(bottle.request.params.month)
    day = int(bottle.request.params.day)
    hour = int(bottle.request.params.hour)
    user_id = bottle.request.params.user_id
    data = {"title": title, "name": name, "year": year, "month": month, "day": day, "hour": hour, "room": room, "user_id": user_id}
    return data


@bottle.route("/change_result/<user_id>")

@bottle.post("/change_result/<user_id>")
@bottle.view("change_result")
def change_result(user_id):
    #新規予約に使う
    title = bottle.request.params.title
    name = bottle.request.params.name
    hour = int(bottle.request.params.hour)
    room = bottle.request.params.room
    date = bottle.request.params.date
    tmp = date.split("-")
    year = int(tmp[0])
    month = int(tmp[1])
    day = int(tmp[2])

    #予約削除に使う
    title_before = bottle.request.params.title_before
    room_before = bottle.request.params.room_before
    year_before = int(bottle.request.params.year_before)
    month_before = int(bottle.request.params.month_before)
    day_before = int(bottle.request.params.day_before)
    hour_before = int(bottle.request.params.hour_before)
    print(title_before, room_before, year_before, month_before, day_before, hour_before, name)

    #変更前の予約を削除
    data = []
    with env.begin(write=True) as txn:
        cur = txn.cursor()
        for k, v in cur:
            d = json.loads(v.decode("utf8"))
            if(d["name"] == name and d["room"] == room_before and d["year"] == year_before and d["month"] == month_before and d["day"] == day_before and d["hour"] == hour_before):
                txn.delete(k)
                print(str(d["year"])+"年"+str(d["month"])+"月"+str(d["day"])+"日"+str(d["hour"])+"時〜"+str(int(d["hour"])+1)+"時"+str(d["room"])+"の予約を削除")
                data = {"title_before": title_before, "room_before": room_before, "year_before": year_before, "month_before": month_before, "day_before": day_before, "hour_before": hour_before}

    #変更後の予約
    data_reserve = {"title": title, "name": name, "year": year, "month": month, "day": day, "hour": hour, "room": room, "user_id": user_id}
    data.update({"title": title, "name": name, "year": year, "month": month, "day": day, "hour": hour, "room": room, "user_id": user_id})
    if(is_ok_room(year, month, day, hour, room) == False):
        return bottle.template("error_submit_overlapping_time", user_id = user_id)
    elif(is_ok_time(year, month, day, hour) == False):
        return bottle.template("error_submit_not_exist_time", user_id = user_id)
    with env.begin(write=True) as txn:
        id = get_id(txn)
        txn.put(id.encode("utf8"), json.dumps(data_reserve).encode("utf8"))
        print(str(data["year"])+"年"+str(data["month"])+"月"+str(data["day"])+"日"+str(data["hour"])+"時〜"+str(int(data["hour"])+1)+"時"+str(data["room"])+"の予約を登録")
    return data


bottle.run()