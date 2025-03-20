import re

msg = 'The color is blue'

# 순서1 sub
print(msg)
print(msg.replaces('blue','orange'))
print()

ret5 = re.sub('blue', 'hotpink', msg)  #msg.replace(구,신)함수역할
print(ret5)
print(re.sub('blue', 'hotpink', msg)) #msg.replace(구,신)함수역할
print('- ' * 30)
print()

# 순서2 findall 특수문자추출,   특수문자제외추출=문자와숫자, 
msg = 'my best $#@ 오렌지 color @#&%# 345 is orange'
print('원본', msg)

# 첫번째 특수문자제외한 문자,숫자만 추출 findall(1패턴형식,2msg)
# 힌트 w워드word응용 +1회이상 a-zA-Z0-9가-힣
# \w Matches any alphanumeric character;
ret6 = re.findall( '[\w]+' , msg) 
print('패턴6', ret6)
ret7 = re.findall( '[a-zA-Z0-9가-힣]+' , msg) 
print('패턴7', ret7)
print()


# 두번째 특수문자추출  ^부정not사용
ret2 = re.findall( '[^\w]+' , msg) 
print('점심전패턴2', ret2)
ret3 =  re.findall( '[^a-zA-Z0-9가-힣]+' , msg)  #25번라인 비교 
print('점심전패턴3', ret3)






































print()
print()