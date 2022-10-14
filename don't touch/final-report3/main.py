import bottle
import lmdb
import json


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

def is_ok(year, month, hour, room):
    data = []
    with env.begin() as txn:
        cur = txn.cursor()
        for k, v in cur:
            d = json.loads(v.decode("utf8"))
            data.append(d)
    for tmp in data:
        if(tmp["year"] == year and tmp["month"] == month and tmp["hour"] == hour and tmp["room"] == room):
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
    year = bottle.request.params.year
    month = bottle.request.params.month
    day = bottle.request.params.day
    hour = bottle.request.params.hour
    room = bottle.request.params.room
    data = {"title": title, "name": name, "year": year, "month": month, "day": day, "hour": hour, "room": room}
    if(is_ok(year, month, hour, room) == False):
        data = {"title": 1, "name": 1, "year": 1, "month": 1, "day": 1, "hour": 1, "room": 1}
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
    for d in data:
        print(d)
    data_sorted = sorted(data, key=lambda x:x["room"])
    for d in data_sorted:
        print(d)
    return {"data": data_sorted}
"""
@bottle.route("/check")
def check():
    data = []
    hour = bottle.request.params.hour
    with env.begin() as txn:
        cur = txn.cursor()
        for k, v in cur:
            d = json.loads(v.decode("utf8"))
            data.append(d)
    for tmp in d:
        if(tmp[5] == hour):
            return False
        else:
            return True
"""

bottle.run()
