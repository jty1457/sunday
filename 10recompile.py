import re

#  정규식 compile함수(1키워드,2옵션)
msg = "apple is big company and Apple 7app7le7 is very delicious apple my Apple"

ret  = re.compile('apple',re.I) #re.I대소문자무시 compile()-> findall(대상문자열)
print(ret)                      #re.compile('apple', re.IGNORECASE)
print(re.compile('apple',re.I)) #re.compile('apple', re.IGNORECASE)
print(ret.findall(msg)) #최종결과['Apple', 'apple', 'apple', 'Apple']
print()

ret  = re.compile('apple') #정확하게 소문자데이터 조회 
print(ret.findall(msg))





























print()
print()