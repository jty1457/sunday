
#11lambda.py문서
def mysu(a):
    return 5*a+2

#함수 매개인자1개, 리턴값1개 
ret = mysu(6)  
print('일반식결과', ret)                  #일반식결과 32

hongret = lambda a:5*a+2
print('람다식결과', hongret(6) )          #람다식결과 32
print('람다식결과', (lambda a:5*a+2)(6) ) #람다식결과 32

# 궁금한점 람다식 결과값이 숫자형태?, 문자열의 결과 람다식에 조건if~else
# 궁금한점 람다식에 조건if~else
# 궁금한점 람다식 결과값이 숫자형태일때 하나이상 34  78  64 데이터관리 























print()
print()