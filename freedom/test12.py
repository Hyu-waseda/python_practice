import requests
import random
import time
import datetime

url = "https://docs.google.com/forms/d/e/1FAIpQLSfa6s6xEjIZ2M60M-kAVANxVY3gNO3eqe2O0mGzkKXui9SSqg/formResponse"

m = 50
M = 600


p2 = 30

def a():
  n = random.randint(1, 100)
  if n <= p2:
    return 0
  n = random.randint(m, M)
  print(n)
  time.sleep(n)
  for d in range(100):
    univ = "欲しい"
    params = {
      'entry.692011076' : univ
    }
    #print(univ, gakubu, sex, kei, grade, sex_re, where, n)
    r = requests.get(url, params=params)
    #print(r.url)
    print(r.status_code, "Yes", univ)
    if(r.status_code == 200):
      break



for d in range(100):
  print(datetime.datetime.now())
  print(d)
  time.sleep(200)
  a()

