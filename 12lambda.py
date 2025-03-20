

def mysu(a):
    return 5*a+2

#함수 매개인자1개, 리턴값1개 
ret = mysu(6)  
print('일반식결과', ret)                  #일반식결과 32

hongret = lambda a:5*a+2
print('람다식결과', hongret(6) )          #람다식결과 32
print('람다식결과', (lambda a:5*a+2)(6) ) #람다식결과 32
print()

# 궁금한점 람다식 결과값이 숫자형태?, 문자열결과, 그리고 람다식에 조건if~else
# 궁금한점 람다식 매개인자 1개이상, 리턴값 1개이상 
# 24숫자값이 짝수? 홀수? if~else구별
def myExpress(n):
    if n%2 == 0:
        msg='짝수'
    else:
        msg='홀수'
    return msg

ret = myExpress(34)
parkret = lambda n: '짝수' if n%2 == 0 else '홀수'
print('일반식결과', ret)  
print('람다식결과', parkret(34)) 
print('람다식결과', (lambda n: '짝수' if n%2 == 0 else '홀수')(34)) 

# 궁금한점 람다식 결과값이 숫자형태?, 문자열결과, 그리고 람다식에 조건if~else
# 궁금한점 람다식 매개인자 1개이상, 리턴값 1개이상 


















print()
print()