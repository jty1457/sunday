print()

import math
import time
# from datetime import datetime 
import datetime #권장

dt = datetime.datetime.now()
print(dt.year,'년', dt.month,'월', dt.day,'일', dt.hour,'시', dt.minute,'분', dt.second,'초')
jumin = '951230-1835064'

#해결 95
my = jumin[0:2]

#해결 나이 계산 2025 - (1900+95)
myage = int(dt.year)  - (1900+int(my))
print('나희동님의 나이는',myage,'세')
print()
print(dt.strftime('현재날짜 %Y년-%m월-%d일'))
print(dt.strftime('현재날짜 %H시-%M분-%S초'))















print()
print()