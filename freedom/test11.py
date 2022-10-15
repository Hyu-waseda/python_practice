import requests
import random
import time
import datetime

url = "https://docs.google.com/forms/d/e/1FAIpQLSefyZMojV8kRL7fZOmOayJonjSXC4Qzlm-HZ41xNqlY4F8StQ/formResponse"

m = 1000
M = 2200


p2 = 50 #青山
p_toukoudai = 50

def aoyama():
  n = random.randint(1, 100)
  if n <= p2:
    return 0
  n = random.randint(m, M)
  print(n)
  time.sleep(n)
  for d in range(100):
    univ = "青山学院大学"
    gakubu = ""
    sex = ""
    kei = ""
    grade = ""
    sex_re = ""
    job = "大学生"
    where = ""

    n = random.randint(1, 11)
    if n == 1:
      gakubu = "理工学部"
      kei = "理系"
    elif n == 2:
      gakubu = "文学部"
      kei = "文系"
    elif n == 3:
      gakubu = "経営学部"
      kei = "文系"
    elif n == 4:
      gakubu = "教育人間科学学部"
      kei = "文系"
    elif n == 5:
      gakubu = "経済学部"
      kei = "文系"
    elif n == 6:
        gakubu = "国際政治経済学部"
        kei = "文系"
    elif n == 7:
      gakubu = "総合文化政策学部"
      kei = "文系"
    elif n == 8:
      gakubu = "社会情報学部"
      kei = "文系"
    elif n == 9:
      gakubu = "地域社会共生学部"
      kei = "文系"
    elif n == 10:
      gakubu = "コミュニティ人間科学部"
      kei = "文系"
    else:
      gakubu = "法学部"
      kei = "文系"

    n = random.randint(1, 100)
    if n <= 25:
      sex = "男性"
      sex_re = "女性"
    else:
      sex = "女性"
      sex_re = "男性"

    n = random.randint(1, 4)
    if n == 1:
      grade = "1年生"
    elif n == 2:
      grade = "2年生"
    elif n == 3:
      grade = "3年生"
    else:
      grade = "4年生"

    n = random.randint(1, 100)
    if n <= 10:
      where = "大学の講義・クラス"
    elif n <= 30:
      where = "サークル"
    elif n <= 40:
      where = "アルバイト"
    elif n <= 50:
      where = "合コン"
    elif n <= 65:
      where = "ナンパ"
    elif n <= 90:
      where = "マッチングアプリ"
    else:
      where = "友人の紹介"

    n = random.randint(0, 4)
    n = str(n)
    params = {
      'entry.2035855537' : univ,
      'entry.1065195348' : gakubu,
      'entry.1729053084' : sex,
      'entry.48054318' : kei,
      'entry.481631409' : grade,
      'entry.39425829' : 'いる',
      'entry.597487448' : sex_re,
      'entry.1937439740' : '大学生',
      'entry.313404170' : univ,
      'entry.507670341' : gakubu,
      'entry.1800002619' : where,
      'entry.1102187314' : '',
      'entry.591427576' : n,
      'entry.58212762' : ''
    }
    #print(univ, gakubu, sex, kei, grade, sex_re, where, n)
    r = requests.get(url, params=params)
    #print(r.url)
    print(r.status_code, "Yes", univ, gakubu, sex, kei, grade, sex_re, where, n)
    if(r.status_code == 200):
      break

def keio():
  n = random.randint(1, 100)
  if n <= p2:
    return 0
  n = random.randint(m, M)
  print(n)
  time.sleep(n)
  for d in range(100):
    univ = "慶応大学"
    gakubu = ""
    sex = ""
    kei = ""
    grade = ""
    sex_re = ""
    job = "大学生"
    where = ""

    n = random.randint(1, 10)
    if n == 1:
      gakubu = "理工学部"
      kei = "理系"
    elif n == 2:
      gakubu = "医学部"
      kei = "文系"
    elif n == 3:
      gakubu = "文学部"
      kei = "文系"
    elif n == 4:
      gakubu = "経済学部"
      kei = "文系"
    elif n == 5:
      gakubu = "法学部"
      kei = "文系"
    elif n == 6:
      gakubu = "商学部"
      kei = "文系"
    elif n == 7:
      gakubu = "総合政策学部"
      kei = "文系"
    elif n == 8:
      gakubu = "環境情報学部"
      kei = "文系"
    elif n == 9:
      gakubu = "看護医療学部"
      kei = "理系"
    else:
      gakubu = "薬学部"
      kei = "理系"

    n = random.randint(1, 100)
    if n <= 20:
      sex = "男性"
      sex_re = "女性"
    else:
      sex = "女性"
      sex_re = "男性"

    n = random.randint(1, 4)
    if n == 1:
      grade = "1年生"
    elif n == 2:
      grade = "2年生"
    elif n == 3:
      grade = "3年生"
    else:
      grade = "4年生"

    n = random.randint(1, 100)
    if n <= 40:
      where = "大学の講義・クラス"
    elif n <= 70:
      where = "サークル"
    elif n <= 93:
      where = "アルバイト"
    else:
      where = "友人の紹介"

    n = random.randint(0, 4)
    n = str(n)
    params = {
      'entry.2035855537' : univ,
      'entry.1065195348' : gakubu,
      'entry.1729053084' : sex,
      'entry.48054318' : kei,
      'entry.481631409' : grade,
      'entry.39425829' : 'いる',
      'entry.597487448' : sex_re,
      'entry.1937439740' : '大学生',
      'entry.313404170' : univ,
      'entry.507670341' : gakubu,
      'entry.1800002619' : where,
      'entry.1102187314' : '',
      'entry.591427576' : n,
      'entry.58212762' : ''
    }
    #print(univ, gakubu, sex, kei, grade, sex_re, where, n)
    r = requests.get(url, params=params)
    #print(r.url)
    print(r.status_code, "Yes", univ, gakubu, sex, kei, grade, sex_re, where, n)
    if(r.status_code == 200):
      break

def toukoudai_not():
  n = random.randint(1, 100)
  if n <= p_toukoudai:
    return 0
  n = random.randint(m, M)
  print(n)
  time.sleep(n)
  for d in range(100):
    univ = "東京工業大学"
    gakubu = ""
    sex = ""
    kei = ""
    grade = ""
    sex_re = ""
    job = "大学生"
    where = ""

    n = random.randint(1, 6)
    if n == 1:
      gakubu = "理学院"
      kei = "理系"
    elif n == 2:
      gakubu = "工学院"
      kei = "理系"
    elif n == 3:
      gakubu = "物質理工学院"
      kei = "理系"
    elif n == 4:
      gakubu = "情報理工学院"
      kei = "理系"
    elif n == 5:
      gakubu = "生命理工学院"
      kei = "理系"
    else:
      gakubu = "環境社会理工学院"
      kei = "理系"
    

    n = random.randint(1, 100)
    if n <= 90:
      sex = "男性"
      sex_re = "女性"
    else:
      sex = "女性"
      sex_re = "男性"

    n = random.randint(1, 4)
    if n == 1:
      grade = "1年生"
    elif n == 2:
      grade = "2年生"
    elif n == 3:
      grade = "3年生"
    else:
      grade = "4年生"

    n = random.randint(0, 1)
    n = str(n)
    params = {
      'entry.2035855537' : univ,
      'entry.1065195348' : gakubu,
      'entry.1729053084' : sex,
      'entry.48054318' : kei,
      'entry.481631409' : grade,
      'entry.39425829' : 'いない',
      'entry.597487448' : '',
      'entry.1937439740' : '',
      'entry.313404170' : '',
      'entry.507670341' : '',
      'entry.1800002619' : '',
      'entry.1102187314' : '',
      'entry.591427576' : n,
      'entry.58212762' : ''
    }
    #print(univ, gakubu, sex, kei, grade, sex_re, where, n)
    r = requests.get(url, params=params)
    #print(r.url)
    print(r.status_code, "not", univ, gakubu, sex, kei, grade, sex_re, where, n)
    if(r.status_code == 200):
      break



for d in range(100):
  print(datetime.datetime.now())
  print(d)
  time.sleep(300)
  aoyama()
  keio()
  toukoudai_not()
