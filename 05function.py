print()


# 함수=처리=기능=function=procedure=method
# 작성하는 이유는 가독성
# 작성하는 이유는 반복처리 구현후 호출
# 작성하는 이유는 한번호출 메모리로드기억놓고 필요할때 호출

# 함수 4패턴
# 리턴x, 매개인자x 표준 조건없이 오직 처리=구현
# 리턴O, 매개인자x
# 리턴x, 매개인자O
# 리턴O, 매개인자O

# 첫번째  리턴x, 매개인자x
def myloop():  #함수 구현
    su, total = 0, 0
    flag = True 
    while flag:
        su = su + 1
        if su==5:
            continue
        print(su , end=' ')
        total = total + su 
        if su == 10 :
            break 
    print('합계 =',total)


myloop() #함수호출 calll
























print()
print()