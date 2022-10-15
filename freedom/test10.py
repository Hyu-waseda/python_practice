import requests
import random
import time
import datetime

url = "https://docs.google.com/forms/d/e/1FAIpQLSeYH2l-gqySZ-OmZgYWprzT4tEYuK7ofUX1iLGq680rSCdQRQ/formResponse"

m = 0
M = 0


p2 = 0 #新潟など

def nigata():
  n = random.randint(1, 100)
  if n <= p2:
    return 0
  n = random.randint(m, M)
  print(n)
  time.sleep(n)
  for d in range(100):

    e = []

    n = random.randint(1, 100)
    if n <= 100:
      e.append("アシス")
    
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

for d in range(10):
  print(datetime.datetime.now())
  print(d)
  time.sleep(20)
  nigata()
  