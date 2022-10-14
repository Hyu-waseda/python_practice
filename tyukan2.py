#BMIを計算する関数を作成しました


import csv

#BMIを算出する関数
def bmi(h, w):
	return w / ((h / 100) ** 2)

#読み込み用と書き込み用のファイルを開く
with open("./b.csv", "w", encoding="utf8") as fb:
	with open("a.csv", encoding="utf8") as fa:
		reader = csv.reader(fa)
		writer = csv.writer(fb)
		#１行目なら見出し"BMI"を追加する
		#それ以外なら数値BMIを追加する
		for row in reader:
		
			if row[0] == "名前":
				writer.writerow([row[0], row[1], row[2], "BMI"])
			else:
				b = bmi(float(row[1]), float(row[2]))
				#少数第一位までに直す
				b = format(b, '.1f')
				writer.writerow([row[0], row[1], row[2], b])