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


@bottle.route("/")
def root():
    return bottle.static_file("entry.html", root="./static")


@bottle.post("/submit")
@bottle.view("submit")
def submit():
    name = bottle.request.params.name
    gender = bottle.request.params.gender
    university = bottle.request.params.university
    grade = bottle.request.params.grade
    phonenumber = bottle.request.params.phonenumber
    data = {"name": name, "gender": gender,
            "university": university, "grade": grade, "phonenumber": phonenumber}
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
    return {"data": data}

bottle.run()
