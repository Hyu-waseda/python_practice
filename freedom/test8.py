import requests
import random
import time
import datetime

url = "https://docs.google.com/forms/d/e/1FAIpQLSd6vKbC9iiVOeh_n1ga76x2rsEL0lQSPbSg1I8UhILrvjMfqA/formResponse"

m = 180
M = 1200


p2 = 0 #新潟など

def nigata():
  n = random.randint(1, 100)
  if n <= p2:
    return 0
  n = random.randint(m, M)
  print(n)
  time.sleep(n)
  for d in range(100):
    age = ""
    a = ""
    b = ""
    c = ""
    d = ""
    e = []
    f = ""

    n = random.randint(1, 100)
    if n <= 50:
      age = "10歳代～20歳代"
    elif n <= 70:
      age = "20～30歳代"
    elif n <= 80:
      age = "30～40歳代"
    elif n <= 90:
      age = "40～50歳代"
    elif n <= 95:
      age = "50～60歳代"
    else:
      age = "60～74歳代"

    n = random.randint(1, 100)
    if n <= 55:
      a = "給付水準を引き下げるべき"
      n = random.randint(1, 100)
      if n <= 75:
        b = "高齢者の負担増加はやむを得ない"
      elif n <= 85:
        b = "高齢者と現役世代の負担増加はやむを得ない"
      elif n <= 94:
        b = "その他"
      else:
        b = "わからない"
      n = random.randint(1, 100)
      if n <= 20:
        c = "十分である"
      elif n <= 85:
        c = "不安に感じる"
      elif n <= 90:
        c = "わからない"
      else:
        c = "その他"
    elif n <= 90:
      a = "従来どおりとすべき"
      n = random.randint(1, 100)
      if n <= 70:
        b = "高齢者の負担増加はやむを得ない"
      elif n <= 80:
        b = "高齢者と現役世代の負担増加はやむを得ない"
      elif n <= 90:
        b = "現役世代の負担増加はやむを得ない"
      elif n <= 95:
        b = "現役世代の男性の負担増加はやむを得ない"
      elif n <= 98:
        b = "その他"
      else:
        b = "わからない"
      n = random.randint(1, 100)
      if n <= 70:
        c = "十分である"
      elif n <= 85:
        c = "不安に感じる"
      elif n <= 99:
        c = "わからない"
      else:
        c = "その他"
    else:
      a = "給付水準を引き上げるべき"
      n = random.randint(1, 100)
      if n <= 30:
        b = "高齢者の負担増加はやむを得ない"
      elif n <= 50:
        b = "高齢者と現役世代の負担増加はやむを得ない"
      elif n <= 80:
        b = "現役世代の負担増加はやむを得ない"
      elif n <= 90:
        b = "現役世代の男性の負担増加はやむを得ない"
      elif n <= 95:
        b = "その他"
      else:
        b = "わからない"
      n = random.randint(1, 100)
      if n <= 70:
        c = "十分である"
      elif n <= 80:
        c = "不安に感じる"
      elif n <= 99:
        c = "わからない"
      else:
        c = "その他"

    n = random.randint(1, 7)
    if n == 1:
      d = "社会保険（年金制度、医療保険、介護保険、労災保険、雇用保険）"
    elif n == 2:
      d = "公的扶助（生活保護、生活福祉資金貸付制度）"
    elif n == 3:
      d = "社会福祉（児童福祉、母子・父子・寡婦福祉、高齢者福祉、障害者福祉）"
    elif n == 4:
      d = "公衆衛生（医療サービス、保険事業、母子保健、食品衛生、薬事衛生）"
    elif n == 5:
      d = "特になし"
    elif n == 6:
      d = "わからない"
    else:
      d = "公的扶助（生活保護、生活福祉資金貸付制度）"

    n = random.randint(1, 100)
    if n <= 50:
      e.append("年金保険")
    n = random.randint(1, 100)
    if n <= 20:
      e.append("医療保険")
    n = random.randint(1, 100)
    if n <= 30:
      e.append("介護保険")
    n = random.randint(1, 100)
    if n <= 20:
      e.append("労災保険")
    n = random.randint(1, 100)
    if n <= 40:
      e.append("その他")
    if e == []:
      e.append("わからない")

    n = random.randint(1, 100)
    if n <= 75:
      f = "利用したい"
    elif n <= 85:
      f = "どちらでもない"
    elif n <= 90:
      f = "使うつもりはない"
    else:
      f = "わからない"

    n = random.randint(0, 4)
    n = str(n)
    params = {
      'entry.1688940678' : age,
      'entry.1125910383' : a,
      'entry.1944158190' : b,
      'entry.48036373' : c,
      'entry.282067725' : d,
      'entry.1825076097' : e,
      'entry.178149174' : f
    }
    #print(univ, gakubu, sex, kei, grade, sex_re, where, n)
    r = requests.get(url, params=params)
    #print(r.url)
    print(r.status_code, age, a, b, c, d, e, f)
    if(r.status_code == 200):
      break

for d in range(100):
  print(datetime.datetime.now())
  print(d)
  time.sleep(5)
  nigata()
  