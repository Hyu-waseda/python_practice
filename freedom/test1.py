import requests
import time
import random



url = "https://docs.google.com/forms/d/1k6IW6gbX32a5GIAQuVpJcKJVwsa0x0FAsBCaZkIMHhg/formResponse"


n = 0
s = ""
def ans():
  t = random.randint(1, 5)
  s = ""
  if t == 1:
    s = "全くそう思わない"
  elif t == 2:
    s = "あまりそう思わない"
  elif t == 3:
    s = "どちらともいえない"
  elif t == 4:
    s = "まぁそう思う"
  elif t == 5:
    s = "とてもそう思う"
  print("ans = " + s)
  return s


def ans1():
  t = random.randint(1, 10)
  s = ""
  if t <= 6:
    s = "男性"
  else:
    s = "女性"
  print("ans1 = " + s)
  return s

def ans2():
  t = random.randint(1, 100)
  s = ""
  if t <= 20:
    s = "10代"
  elif t <= 95:
    s = "20代"
  elif t <= 97:
    s = "30代"
  elif t <= 98:
    s = "40代"
  elif t <= 99:
    s = "50代"
  else:
    s = "それ以上"
  print("ans2 = " + s)
  return s

def ans3():
  t = random.randint(1, 100)
  s = ""
  if t <= 60:
    s = "遠居"
  elif t <= 75:
    s = "同じ県内の住居"
  elif t <= 90:
    s = "同じ市内の住居"
  else:
    s = "同居"
  print("ans3 = " + s)
  return s

def ans4():
  t = random.randint(1, 100)
  s = ""
  if t <= 60:
    s = "ほぼしない"
  elif t <= 80:
    s = "年に1.2回"
  elif t <= 90:
    s = "月に1.2回"
  elif t <= 95:
    s = "週に1.2回"
  else:
    s = "ほぼ毎日"
  print("ans4 = " + s)
  return s

def ans5():
  t = random.randint(1, 100)
  s = ""
  if t <= 60:
    s = "5分以内"
  elif t <= 80:
    s = "5分~15分"
  elif t <= 90:
    s = "15分~30分"
  elif t <= 95:
    s = "30分~1時間"
  else:
    s = "1時間以上"
  print("ans5 = " + s)
  return s

def ans6():
  t = random.randint(1, 100)
  s = ""
  if t <= 50:
    s = "全く親しくない"
  elif t <= 60:
    s = "あまり親しくない"
  elif t <= 80:
    s = "やや親しい"
  else:
    s = "非常に親しい"
  print("ans6 = " + s)
  return s


def ans7():
  t = random.randint(1, 100)
  s = ""
  if t <= 30:
    s = "全く影響を受けていない"
  elif t <= 55:
    s = "あまり影響を受けていない"
  elif t <= 80:
    s = "やや影響を受けている"
  else:
    s = "非常に影響を受けている"
  print("ans7 = " + s)
  return s

def ans8():
  t = random.randint(1, 5)
  s = ""
  if t == 1:
    s = "全くそう思わない"
  elif t == 2:
    s = "あまりりそう思わない"
  elif t == 3:
    s = "どちらとも言えない"
  elif t == 4:
    s = "まぁそう思う"
  elif t == 5:
    s = "とてもそう思う"
  print("ans = " + s)
  return s

def ans9():
  t = random.randint(1, 5)
  s = ""
  if t == 1:
    s = "全くそう思わない"
  elif t == 2:
    s = "あまりそう思わない"
  elif t == 3:
    s = "どちらとも言えない"
  elif t == 4:
    s = "まぁそう思う"
  elif t == 5:
    s = "とてもそう思う"
  print("ans = " + s)
  return s

for d in range(10):
  t = random.randint(100, 100)
  print(t)
  time.sleep(t)
  for d in range(30):
    tmp = ans2()
    tmp1 = ""
    if tmp == "10代" or tmp == "20代":
      tmp1 = "学生"
    else:
      tmp1 = "社会人"

    tmp3 = ans3()
    tmp4 = ""
    tmp5 = ""
    if tmp3 == "遠居":
      tmp4 = "ほぼ会わない"
      n = random.randint(1, 10)
      if n <= 3:
        tmp5 = "15分以内"
      elif n <= 6:
        tmp5 = "15分~1時間"
      else:
        tmp5 = "半日"
    elif tmp3 == "同居":
      tmp4 = "ほぼ毎日"
      tmp5 = "それ以上"
    else:
      n = random.randint(1, 10)
      if n <= 6:
        tmp4 = "年に1.2回"
      elif n <= 8:
        tmp4 = "月に1.2回"
      else:
        tmp4 = "週に1.2回"
        n = random.randint(1, 10)
        if n <= 3:
          tmp5 = "半日"
        elif n <= 6:
          tmp5 = "15分~1時間"
        else:
          tmp5 = "1時間~3時間"
    #print(tmp, tmp1, tmp3, tmp4, tmp5)
    params = {
      'entry.1795380732' : ans1(),
      'entry.1904575943' : tmp,
      'entry.628330118' : tmp1,
      'entry.1882061028' : ans(),
      'entry.556809785' : ans(),
      'entry.1993475954' : ans(),
      'entry.1341932256' : ans(),
      'entry.279343542' : ans(),
      'entry.1333099139' : ans(),
      'entry.229125115' : ans(),
      'entry.659026227' : ans(),
      'entry.581360882' : ans(),
      'entry.824861725' : ans(),
      'entry.921432090' : ans(),
      'entry.30620208' : ans(),
      'entry.771168476' : ans(),
      'entry.1838063885' : ans(),
      'entry.1445081938' : tmp3,
      'entry.1803704038' : tmp4,
      'entry.95445775' : tmp5,
      'entry.653659087' : ans4(),
      'entry.1688065682' : ans5(),
      'entry.969181209' : ans4(),
      'entry.1803502866' : ans6(),
      'entry.875972479' : ans7(),
      'entry.1596598971' : ans7(),
      'entry.1011303435' : ans8(),
      'entry.1770281529' : ans8(),
      'entry.1159895358' : ans8(),
      'entry.43383982' : ans8(),
      'entry.64533528' : ans9(),
      'entry.1824231273' : ans9(),
      'entry.416993271' : ans(),
      'entry.1506906646' : ans9(),
      'entry.68409526' : ans9(),
      'entry.459613762' : ans9(),
      'entry.1321441484' : ans9(),
      'entry.1243446361' : ans9(),
      'entry.911117083' : ans9(),
      'entry.1158744348' : ans9(),
      'entry.2051457805' : ans9()
    }
    
    r = requests.get(url, params=params)
    #print(r.url)
    print(r.status_code)
    if(r.status_code == 200):
      break