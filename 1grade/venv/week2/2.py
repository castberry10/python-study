# 자동판매기 프로그램
# 물건값을 입력 받고, 사용자가 지불할 1000원권, 500원, 100원의 개수를 입력 받은 후 거스름돈을 500원, 100원, 10원, 1원 단위로 반환.

value = int(input("물건값을 입력하세요 : "))

print("====입력금액====")
money1000 = int(input("1000원 짜리 지폐개수 : ")) * 1000
money500 = int(input("500원 짜리 지폐개수 : ")) * 500
money100 = int(input("100원 짜리 지폐개수 : ")) * 100

moneySum = money100 + money1000 + money500

print("====거스름돈====")

change = moneySum - value

change500 = int(change / 500)
change = change % 500


change100 = int(change / 100)
change = change % 100


change10 = int(change / 10)
change = change % 10


print("500원" ,change500 ,"100원" , change100,"10원" ,change10 ,"1원", change)