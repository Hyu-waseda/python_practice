import bottle
import lmdb
import json
import datetime


env = lmdb.Environment("./dbcircle")


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
                if(hour < dt_now.hour):
                    return False

    #存在しない日付はFalse
    if(month < 1 or 12 < month or day < 1 or 31 < day or hour < 0 or 24 < hour):
        return False
    elif(month == 2 or month == 4 or month == 6 or month == 9 or month == 11):
        if(day > 30):
            return False
    elif(month == 2):
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
    with env.begin(write=True) as txn:
        cur = txn.cursor()
        for k, v in cur:
            d = json.loads(v.decode("utf8"))
            #過去の日付があったら削除
            if(is_ok_time(d["year"], d["month"], d["day"], d["hour"]) == False):
                txn.delete(k)
            else:
                data.append(d)
    for tmp in data:
        if(tmp["year"] == year and tmp["month"] == month and tmp["day"] == day and tmp["hour"] == hour and tmp["room"] == room):
            return False
    return True


@bottle.route("/")
def root():
    return bottle.static_file("entry.html", root="./static")


@bottle.post("/submit")
@bottle.view("submit")
def submit():
    title = bottle.request.params.title
    name = bottle.request.params.name
    hour = int(bottle.request.params.hour)
    room = bottle.request.params.room
    date = bottle.request.params.date
    tmp = date.split("-")
    year = int(tmp[0])
    month = int(tmp[1])
    day = int(tmp[2])
    data = {"title": title, "name": name, "year": year, "month": month, "day": day, "hour": hour, "room": room}
    if(is_ok_room(year, month, day, hour, room) == False):
        data = {"title": 1, "name": 1, "year": 1, "month": 1, "day": 1, "hour": 1, "room": 1}
        return data
    elif(is_ok_time(year, month, day, hour) == False):
        data = {"title": 2, "name": 2, "year": 2, "month": 2, "day": 2, "hour": 2, "room": 2}
        return data
    with env.begin(write=True) as txn:
        id = get_id(txn)
        txn.put(id.encode("utf8"), json.dumps(data).encode("utf8"))
    return data


@bottle.route("/list")
@bottle.view("list")
def list():
    data = []
    with env.begin() as txn:
        cur = txn.cursor()
        for k, v in cur:
            d = json.loads(v.decode("utf8"))
            data.append(d)
    data_sorted = sorted(data, key=lambda x:(x["room"], int(x["year"]), int(x["month"]), int(x["day"]), int(x["hour"])))
    for d in data_sorted:
        print(d)
    return {"data": data_sorted}

bottle.run()
