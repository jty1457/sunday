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
def myloop():  #함수구현정의define 사용할때 호출
    print("1 2 3 4 6 7 8 9 10 합계 = 50")
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



# myloop() # 첫번째  리턴x, 매개인자x

##############################################################
def mytest(x,y):
    total = x+y
    if total >= 140: message = '축합격'
    else: message = '재시험'
    #학점 100~90 A  89~80 B  79~70 C   69~60 D 59~0 F  
    return total, (total)/2, message

# 리턴O , 매개인자O 
# 매개인자값으로 2개를 주고,  리턴값으로 3개 뽑기 
kor = int(input('국어점수입력 '))
eng = int(input('영어점수입력 '))
total, avg, result = mytest(kor,eng)
print('총합계 =', total)
print('평균대 =', avg)
print('최종결과 =', result)
















print()
print()