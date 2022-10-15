import requests
import random
import time
import datetime

# from test3 import kyoudai

url = "https://docs.google.com/forms/d/e/1FAIpQLScq_Bvn-uqmjHOxU9x3OSSlPcor-d289mKeOo05-DmSpF8iuw/formResponse"

m = 10
M = 400


p1 = 90 #その他
p2 = 98 #新潟など
p3 = 60 #工業系
p4 = 60 #東京一工
p5 = 60 #旧帝大
p6 = 50 #理系
p7 = 90 #日東駒専
p8 = 90 #ネタ枠
p9 = 95 #一橋仮
p_kinki = 30
p_keizai = 60
p_seizikeizai = 95
p_bun = 60
p_shou = 60
p_hou = 60
p_kyoiku = 60
p_kou = 60
p_yaku = 60
p_rikei = 60
p_toukoudai = 60

def toukoudai():
  n = random.randint(1, 100)
  if n <= p4:
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
      gakubu = "生命理工学院"
      kei = "理系"
    elif n == 5:
      gakubu = "環境社会理工学院"
      kei = "理系"
    else:
      gakubu = "情報理工学院"
      kei = "理系"

    n = random.randint(1, 2)
    if n == 1:
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
    if n <= 85:
      where = "二次元世界の住人"
    elif n <= 90:
      where = "大学の講義・クラス"
    elif n <= 95:
      where = "サークル"
    elif n <= 98:
      where = "アルバイト"
    else:
      where = "友人の紹介"

    n = random.randint(0, 1)
    n = str(n)
    aite = "大学生"
    univ1 = univ
    gakubu1 = gakubu
    sonota = ""
    if where == "二次元世界の住人":
      aite = ""
      univ1 = ""
      gakubu1 = ""
      where = "その他"
      q = random.randint(1, 8)
      if q == 1:
        sonota = "音ゲー"
      elif q == 2:
        sonota = "ゲーム"
      elif q == 3:
        sonota = "デレマス"
      elif q == 4:
        sonota = "ウマ娘"
      elif q == 5:
        sonota = "Twitter"
      else:
        sonota = "アニメ"

    params = {
      'entry.2035855537' : univ,
      'entry.1065195348' : gakubu,
      'entry.1729053084' : sex,
      'entry.48054318' : kei,
      'entry.481631409' : grade,
      'entry.39425829' : 'いる',
      'entry.597487448' : sex_re,
      'entry.1937439740' : aite,
      'entry.313404170' : univ1,
      'entry.507670341' : gakubu1,
      'entry.1800002619' : where,
      'entry.1102187314' : sonota,
      'entry.591427576' : n,
      'entry.58212762' : ''
    }
    #print(univ, gakubu, sex, kei, grade, sex_re, where, n)
    r = requests.get(url, params=params)
    #print(r.url)
    print(r.status_code, "Yes", univ, gakubu, sex, kei, grade, sex_re, where, n)
    if(r.status_code == 200):
      break

def keizai_not():
  n = random.randint(1, 100)
  if n <= p_keizai:
    return 0
  n = random.randint(m, M)
  print(n)
  time.sleep(n)
  for d in range(100):
    univ = ""
    gakubu = "経済学部"
    sex = ""
    kei = "文系"
    grade = ""
    sex_re = ""
    job = "大学生"
    where = ""

    n = random.randint(1, 13)
    if n == 1:
      univ = "東北学院大学"
    elif n == 2:
      univ = "慶応大学"
    elif n == 3:
      univ = "法政大学"
    elif n == 4:
      univ = "國學院大学"
    elif n == 7:
      univ = "埼玉大学"
    elif n == 8:
      univ = "青山学院大学"
    elif n == 9:
      univ = "学習院大学"
    elif n == 10:
      univ = "中央大学"
    elif n == 11:
      univ = "國學院大学"
    elif n == 12:
      univ = "武蔵野大学"
    else:
      univ = "神奈川大学"

    n = random.randint(1, 100)
    if n <= 80:
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

    n = random.randint(0, 3)
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

def seizikeizai_not():
  n = random.randint(1, 100)
  if n <= p_seizikeizai:
    return 0
  n = random.randint(m, M)
  print(n)
  time.sleep(n)
  for d in range(100):
    univ = ""
    gakubu = "政治経済学部"
    sex = ""
    kei = "文系"
    grade = ""
    sex_re = ""
    job = "大学生"
    where = ""

    n = random.randint(1, 4)
    if n == 1:
      univ = "駒澤大学"
    elif n == 2:
      univ = "東洋大学"
    elif n == 3:
      univ = "駒澤大学"
    elif n == 4:
      univ = "専修大学"

    n = random.randint(1, 100)
    if n <= 80:
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

    n = random.randint(0, 2)
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

def bun_not():
  n = random.randint(1, 100)
  if n <= p_bun:
    return 0
  n = random.randint(m, M)
  print(n)
  time.sleep(n)
  for d in range(100):
    univ = ""
    gakubu = "文学部"
    sex = ""
    kei = "文系"
    grade = ""
    sex_re = ""
    job = "大学生"
    where = ""

    n = random.randint(1, 8)
    if n == 1:
      univ = "法政大学"
    elif n == 2:
      univ = "玉川大学"
    elif n == 3:
      univ = "北海道大学"
    elif n == 4:
      univ = "中央大学"
    elif n == 5:
      univ = "金沢学院大学"
    elif n == 6:
      univ = "愛知大学"
    elif n == 7:
      univ = "國學院大学"
    else:
      univ = "熊本大学"

    n = random.randint(1, 100)
    if n <= 80:
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

    n = random.randint(0, 3)
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

def shou_not():
  n = random.randint(1, 100)
  if n <= p_shou:
    return 0
  n = random.randint(m, M)
  print(n)
  time.sleep(n)
  for d in range(100):
    univ = ""
    gakubu = "商学部"
    sex = ""
    kei = "文系"
    grade = ""
    sex_re = ""
    job = "大学生"
    where = ""

    n = random.randint(1, 7)
    if n == 1:
      univ = "日本大学"
    elif n == 2:
      univ = "専修大学"
    elif n == 3:
      univ = "同志社大学"
    elif n == 4:
      univ = "関西学院大学"
    elif n == 5:
      univ = "函館大学"
    elif n == 6:
      univ = "一橋大学"
    else:
      univ = "早稲田大学"

    n = random.randint(1, 100)
    if n <= 80:
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

    n = random.randint(0, 2)
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

def hou_not():
  n = random.randint(1, 100)
  if n <= p_hou:
    return 0
  n = random.randint(m, M)
  print(n)
  time.sleep(n)
  for d in range(100):
    univ = ""
    gakubu = "法学部"
    sex = ""
    kei = "文系"
    grade = ""
    sex_re = ""
    job = "大学生"
    where = ""

    n = random.randint(1, 10)
    if n == 1:
      univ = "國學院大学"
    elif n == 3:
      univ = "法政大学"
    elif n == 4:
      univ = "中央大学"
    elif n == 6:
      univ = "青山学院大学"
    elif n == 7:
      univ = "学習院大学"
    elif n == 8:
      univ = "上智大学"
    elif n == 9:
      univ = "神奈川大学"
    else:
      univ = "熊本大学"

    n = random.randint(1, 100)
    if n <= 80:
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

    n = random.randint(0, 2)
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

def kyoiku_not():
  n = random.randint(1, 100)
  if n <= p_kyoiku:
    return 0
  n = random.randint(m, M)
  print(n)
  time.sleep(n)
  for d in range(100):
    univ = ""
    gakubu = "教育学部"
    sex = ""
    kei = "文系"
    grade = ""
    sex_re = ""
    job = "大学生"
    where = ""

    n = random.randint(1, 11)
    if n == 1:
      univ = "愛媛大学"
    elif n == 2:
      univ = "熊本大学"
    elif n == 3:
      univ = "高知大学"
    elif n == 4:
      univ = "玉川大学"
    elif n == 6:
      univ = "関西国際大学"
    elif n == 7:
      univ = "東北福祉大学"
    elif n == 8:
      univ = "茨城大学"
    elif n == 9:
      univ = "埼玉大学"
    else:
      univ = "武蔵野大学"

    n = random.randint(1, 100)
    if n <= 80:
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

    n = random.randint(0, 2)
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

def kou_not():
  n = random.randint(1, 100)
  if n <= p_kou:
    return 0
  n = random.randint(m, M)
  print(n)
  time.sleep(n)
  for d in range(100):
    univ = ""
    gakubu = "工学部"
    sex = ""
    kei = "理系"
    grade = ""
    sex_re = ""
    job = "大学生"
    where = ""

    n = random.randint(1, 15)
    if n == 1:
      univ = "宇都宮大学"
    elif n == 2:
      univ = "東海大学"
    elif n == 3:
      univ = "北海道学園大学"
    elif n == 4:
      univ = "山形大学"
    elif n == 6:
      univ = "千葉大学"
    elif n == 7:
      univ = "東京農工大学"
    elif n == 8:
      univ = "武蔵野大学"
    elif n == 9:
      univ = "福井大学"
    elif n == 10:
      univ = "山梨大学"
    elif n == 11:
      univ = "岐阜大学"
    elif n == 12:
      univ = "三重大学"
    elif n == 13:
      univ = "富山大学"
    else:
      univ = "武蔵野大学"

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

    n = random.randint(0, 2)
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

def yaku_not():
  n = random.randint(1, 100)
  if n <= p_yaku:
    return 0
  n = random.randint(m, M)
  print(n)
  time.sleep(n)
  for d in range(100):
    univ = ""
    gakubu = "薬学部"
    sex = ""
    kei = "理系"
    grade = ""
    sex_re = ""
    job = "大学生"
    where = ""

    n = random.randint(1, 10)
    if n == 1:
      univ = "富山大学"
    elif n == 2:
      univ = "武蔵野大学"
    elif n == 3:
      univ = "近畿大学"
    elif n == 4:
      univ = "福岡大学"
    elif n == 6:
      univ = "長崎国際大学"
    elif n == 7:
      univ = "広島大学"
    elif n == 8:
      univ = "徳島大学"
    elif n == 9:
      univ = "熊本大学"
    else:
      univ = "武蔵野大学"

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

    n = random.randint(0, 2)
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

def kinki_not():
  n = random.randint(1, 100)
  if n <= p_kinki:
    return 0
  n = random.randint(m, M)
  print(n)
  time.sleep(n)
  for d in range(100):
    univ = "近畿大学"
    gakubu = ""
    sex = ""
    kei = ""
    grade = ""
    sex_re = ""
    job = "大学生"
    where = ""

    n = random.randint(1, 14)
    if n == 1:
      gakubu = "法学部"
      kei = "文系"
    elif n == 2:
      gakubu = "経済学部"
      kei = "文系"
    elif n == 3:
      gakubu = "経営学部"
      kei = "文系"
    elif n == 4:
      gakubu = "文芸学部"
      kei = "文系"
    elif n == 5:
      gakubu = "国際学部"
      kei = "文系"
    elif n == 6:
      gakubu = "総合社会学部"
      kei = "文系"
    elif n == 7:
      gakubu = "理工学部"
      kei = "理系"
    elif n == 8:
      gakubu = "建築学部"
      kei = "理系"
    elif n == 9:
      gakubu = "薬学部"
      kei = "理系"
    elif n == 10:
      gakubu = "農学部"
      kei = "理系"
    elif n == 11:
      gakubu = "理工学部"
      kei = "理系"
    elif n == 12:
      gakubu = "生物理工学部"
      kei = "理系"
    elif n == 13:
      gakubu = "工学部"
      kei = "理系"
    else:
      gakubu = "産業理工学部"
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

    n = random.randint(0, 2)
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

def tokyonogyo_not():
  n = random.randint(1, 100)
  if n <= p_rikei:
    return 0
  n = random.randint(m, M)
  print(n)
  time.sleep(n)
  for d in range(100):
    univ = "東京農業大学"
    gakubu = ""
    sex = ""
    kei = ""
    grade = ""
    sex_re = ""
    job = "大学生"
    where = ""

    n = random.randint(1, 9)
    if n == 2:
      gakubu = "応用生物科学学部"
      kei = "理系"
    elif n == 3:
      gakubu = "生命科学部"
      kei = "理系"
    elif n == 4:
      gakubu = "地域環境科学部"
      kei = "理系"
    elif n == 5:
      gakubu = "国際食糧情報学部"
      kei = "理系"
    elif n == 1:
      gakubu = "生物産業学部"
      kei = "理系"
    else:
      gakubu = "農学部"
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

    n = random.randint(0, 2)
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

def tokyodenki_not():
  n = random.randint(1, 100)
  if n <= p_rikei:
    return 0
  n = random.randint(m, M)
  print(n)
  time.sleep(n)
  for d in range(100):
    univ = "東京電機大学"
    gakubu = ""
    sex = ""
    kei = ""
    grade = ""
    sex_re = ""
    job = "大学生"
    where = ""

    n = random.randint(1, 6)
    if n == 1:
      gakubu = "情報環境学部"
      kei = "理系"
    elif n == 2:
      gakubu = "システム工学部"
      kei = "理系"
    elif n == 3:
      gakubu = "未来科学部"
      kei = "理系"
    elif n == 4:
      gakubu = "工学部"
      kei = "理系"
    else:
      gakubu = "理工学部"
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

    n = random.randint(0, 2)
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

def tokyokouka_not():
  n = random.randint(1, 100)
  if n <= p_rikei:
    return 0
  n = random.randint(m, M)
  print(n)
  time.sleep(n)
  for d in range(100):
    univ = "東京工科大学"
    gakubu = ""
    sex = ""
    kei = ""
    grade = ""
    sex_re = ""
    job = "大学生"
    where = ""

    n = random.randint(1, 6)
    if n == 1:
      gakubu = "コンピュータサイエンス学部"
      kei = "理系"
    elif n == 2:
      gakubu = "メディア学部"
      kei = "理系"
    elif n == 3:
      gakubu = "応用生物学部"
      kei = "理系"
    elif n == 4:
      gakubu = "デザイン学部"
      kei = "理系"
    elif n == 5:
      gakubu = "医療保健学部"
      kei = "理系"
    else:
      gakubu = "工学部"
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

    n = random.randint(0, 2)
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
  time.sleep(0)
  keizai_not()
  toukoudai()
  seizikeizai_not()
  bun_not()
  toukoudai()
  shou_not()
  toukoudai()
  kyoiku_not()
  kou_not()
  toukoudai()
  yaku_not()
  toukoudai()
  kinki_not()
