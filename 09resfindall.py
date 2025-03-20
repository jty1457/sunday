import re

#  정규식 findall함수(1패턴형식,2msg)
# 힌트 w워드word응용 +1회이상 a-zA-Z0-9가-힣
# \w Matches any alphanumeric character;
msg = 'my best $#@ 오렌지 color @#&%# 345 is orange'
ret6 = re.findall( '[\w]+' , msg) 
print('패턴6', ret6)
ret7 = re.findall( '[a-zA-Z0-9가-힣]+' , msg) 
print('패턴7', ret7)
print(': ' * 40)
print()

# 두번째 특수문자추출  ^부정not사용
ret1 = re.findall( '[\W]+' , msg)  # \W대문자
print('점심후패턴1', ret1)
ret2 = re.findall( '[^\w]+' , msg)  # \W대문자
print('점심후패턴2', ret2)
ret3 =  re.findall( '[^a-zA-Z0-9가-힣]+' , msg)  #25번라인 비교 
print('점심후패턴3', ret3)






































print()
print()