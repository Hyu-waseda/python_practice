# -*- coding: utf-8 -*-

import datetime
from fractions import Fraction

d1 = datetime.date(2016, 5, 17)
d2 = datetime.date(2017, 1, 1)
td = d2 - d1
print("2016年5月17日から2017年1月1日まで{}日あります".format(td.days))

a = Fraction(25787, 287635)
b = Fraction(40563, 923845)
print("25787/287635 + 40563/923845")
print("= {}".format(a + b))