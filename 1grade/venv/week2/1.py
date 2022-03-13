# 원금, 이자율, 투자기간을 입력받아 복리를 계산하는 프로그램
# 복리 계산 수식 : A(1+r)^n
# 소수점 첫째자리에서 반올림하여 정수부분만 출력

import math

start = int(input("초기금 : "))
per = int(input("이율 : "))  / 100
day = int(input("기간 : "))

m = start * ((1 + per) ** day)

print(round(m) )
