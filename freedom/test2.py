import requests
 
url = "https://docs.google.com/forms/d/e/1FAIpQLSefyZMojV8kRL7fZOmOayJonjSXC4Qzlm-HZ41xNqlY4F8StQ/formResponse"
univ = "早稲田大学"
gakubu = "人間科学部"
params = {
  'entry.2035855537' : '明治大学',
  'entry.1065195348' : '理工学部',
  'entry.1729053084' : '男性',
  'entry.48054318' : '理系',
  'entry.481631409' : '3年生',
  'entry.39425829' : 'いる',
  'entry.597487448' : '女性',
  'entry.1937439740' : '大学生',
  'entry.313404170' : '明治大学',
  'entry.507670341' : '理工学部',
  'entry.1800002619' : '大学の講義・クラス',
  'entry.1102187314' : '',
  'entry.591427576' : '2',
  'entry.58212762' : ''
}
 
r = requests.get(url, params=params)
print(r.url)
print(r.status_code)