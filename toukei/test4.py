from asyncio.constants import LOG_THRESHOLD_FOR_CONNLOST_WRITES
from statistics import stdev

lists = [[65, 57, 83, 75, 80],[72, 76, 70, 74, 75],[65, 66, 80, 81, 80]]

for list in lists:
	print(stdev(list))