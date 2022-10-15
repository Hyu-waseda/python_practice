import statistics

s = """83,424
9,646
15,275
6,859
11,638
6,652
13,784
6,097
6,408
6,362
3,768
5,083
2,109
2,416
10,364
2,046
4,186
4,191
4,254
13,104
9,769
7,253
5,124
5,759
3,767
4,612
1,905
8,401
3,691
4,725
3,507
6,708
7,011
8,480
6,113
4,147
1,863
5,676
7,104
4,854
2,441
4,131
7,273
5,100
6,794
9,043
2,281"""

lists_str = s.split("\n")

lists_num = []
for list_str in lists_str:
	list_str = list_str.replace(",", "")
	lists_num.append(int(list_str))
print(lists_num)

print(statistics.mean(lists_num))
print(statistics.median(lists_num))