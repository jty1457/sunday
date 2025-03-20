

def mydata(data):
    total = []
    for k in data:
        gob = k*k  #곱처리 1*1  2*2 3*3  4*4 5*5 
        total.append(gob)
    return total 
                      
x = list(range(1,11)) # [ 1, 2, 3, 4, 5]
print('초기값출력', x )
kimret = mydata(x)
print('일반식결과', kimret )    #일반식결과 [1, 4, 9, 16, 25]
print('일반식결과', mydata(x) ) #일반식결과 [1, 4, 9, 16, 25]
print()

print('람다식결과', (lambda n: n*n,x) ) #(<function <lambda> at 0x000001FFF1829A80>, [1, 2, 3, 4, 5])
print('람다식결과', map(lambda n: n*n,x) ) #(<function <lambda> at 0x000001FFF1829A80>)
print('람다식결과', list(map(lambda n: n*n,x)) ) # [1, 4, 9, 16, 25]
print()

# 람다식에 if제어문대신 filter()함수사용
x = list(range(1,21)) # 1  ~ 20
print('람다식filter적용', list(filter(lambda n: n%2 == 0, x)) ) 

















print()
print()