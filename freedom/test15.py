import requests
import random
import time
import datetime

url = "https://docs.google.com/forms/d/e/1FAIpQLSeYH2l-gqySZ-OmZgYWprzT4tEYuK7ofUX1iLGq680rSCdQRQ/formResponse"

m = 0
M = 10

p0 = 5
p1 = 10
p2 = 20
p3 = 30
p4 = 40
p5 = 40
p6 = 60
p7 = 70
def nigata():
  n = random.randint(1, 100)
  if n <= p2:
    time.sleep(10)
  n = random.randint(m, M)
  #print(n)
  time.sleep(n)
  for d in range(100):

    e = []

    n = random.randint(1, 100)
    if n <= p4:
      e.append("アシス")
    n = random.randint(1, 100)
    if n <= p4:
      e.append("海坊主")
    n = random.randint(1, 100)
    if n <= p7:
      e.append("えろ爺")
    n = random.randint(1, 100)
    if n <= p7:
      e.append("天気の爺")
    n = random.randint(1, 100)
    if n <= p7:
      e.append("ジャス爺")
    n = random.randint(1, 100)
    if n <= p6:
      e.append("チー牛")
    n = random.randint(1, 100)
    if n <= p6:
      e.append("チー高")
    n = random.randint(1, 100)
    if n <= p7:
      e.append("ビニ爺＆ビニー")
    n = random.randint(1, 100)
    if n <= p7:
      e.append("ヒラ爺")
    n = random.randint(1, 100)
    if n <= p1:
      e.append("豚島")
    n = random.randint(1, 100)
    if n <= p1:
      e.append("まさたか")
    
    n = random.randint(0, 4)
    n = str(n)
    params = {
      'entry.201623774' : e
    }
    #print(univ, gakubu, sex, kei, grade, sex_re, where, n)
    r = requests.get(url, params=params)
    #print(r.url)
    print(r.status_code, e)
    if(r.status_code == 200):
      break

for d in range(10000):
  print(datetime.datetime.now())
  print(d)
  time.sleep(5)
  nigata()
  