

def mydata(data):
    total = []
    for k in data:
        gob = k*k  #곱처리 1*1  2*2 3*3  4*4 5*5 
        total.append(gob)
    return total 
                      
x = list(range(1,6)) # [ 1, 2, 3, 4, 5]
print('초기값출력', x )
kimret = mydata(x)
print('일반식결과', kimret )    #일반식결과 [1, 4, 9, 16, 25]
print('일반식결과', mydata(x) ) #일반식결과 [1, 4, 9, 16, 25]
print()

print('람다식결과', (lambda n: n*n,x) ) #(<function <lambda> at 0x000001FFF1829A80>, [1, 2, 3, 4, 5])
print('람다식결과', map(lambda n: n*n,x) ) #(<function <lambda> at 0x000001FFF1829A80>)
print('람다식결과', list(map(lambda n: n*n,x)) ) # [1, 4, 9, 16, 25]
# 정석(lambda n: 수식)(x)  해법(lambda n: 수식,x)
print()

# 람다식에 if제어문대신 filter()함수사용
x = list(range(1,11)) # 1 2 3 4 5 6 7 8 9 10 
print('람다식filter적용', list(filter(lambda n: n%2 == 0, x)) ) 
# 참고 x = list(range(1,6)) # [ 1, 2, 3, 4, 5] 참고
# 참고 print('람다식결과', (lambda n: '짝수' if n%2 == 0 else '홀수')(34)) 



#힌트 list(), total=[]리스트선언후 연산처리후 total.append()
#람다식으로 구현  매개인자는 하나인데 값은 5개 if제어문없어요 for반복문...
#딕트형태 map()사용해서 LabelEnCoder()처럼

# lambda n: (수식)(5)
# lambda x,y: (수식)(7,2)
# lambda n: (수식 참 if  else 거짓)(5)
# 궁금한점 람다식 결과값이 숫자형태?, 문자열결과, 그리고 람다식에 조건if~else
# 궁금한점 람다식 매개인자 1개이상, 리턴값 1개이상 


















print()
print()