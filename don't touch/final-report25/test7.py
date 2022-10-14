import datetime

d_today = datetime.date.today()

print(d_today)
for d in range(30):
	print(d_today)
	d_today += datetime.timedelta(days=1)