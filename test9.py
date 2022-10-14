import random

e = [""]
n = random.randint(1, 100)
if n <= 50:
  		e += "年金保険"
n = random.randint(1, 100)
if n <= 20:
		e += "医療保険"
n = random.randint(1, 100)
if n <= 30:
     	e.append("介護保険")
n = random.randint(1, 100)
if n <= 20:
    	e += "労災保険"
n = random.randint(1, 100)
if n <= 40:
      	e += "その他"
if e == []:
      	e += "わからない"

print(e)