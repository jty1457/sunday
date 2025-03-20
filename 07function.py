print()
# 함수 4패턴
# 리턴x, 매개인자x 표준 조건없이 오직 처리=구현
# 리턴O, 매개인자x
# 리턴x, 매개인자O
# 리턴O, 매개인자O

print("리턴값 3개, 매개인자X")
def mysj(): # 리턴O, 매개인자X
    kor = int(input('국어점수입력 '))
    eng = int(input('영어점수입력 '))
    total = kor + eng
    if total >= 140: message = '축합격'
    else: message = '재시험'
    return total , (total)/2, message

total, avg, result = mysj()
print('총합계 =', total)
print('평균대 =', avg)
print('최종결과 =', result)







def mytest(x,y): # 리턴O, 매개인자O
    total = x+y
    if total >= 140: message = '축합격'
    else: message = '재시험'
    return total , (total)/2, message

# 리턴O, 매개인자O
# kor = int(input('국어점수입력 '))
# eng = int(input('영어점수입력 '))
# total, avg, result = mytest(kor,eng)
# print('총합계 =', total)
# print('평균대 =', avg)
# print('최종결과 =', result)
















print()
print()