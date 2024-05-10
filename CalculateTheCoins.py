import sys

input_price=input("Input : ")
if not input_price.isdecimal():
    print("정수를 입력하세요")
    sys.exit()

product_price=input("Product : ")
if not product_price.isdecimal():
    print("정수를 입력하세요.")
    sys.exit()

change=int(input_price) - int(product_price)

if change < 0:
    print("금액이 부족합니다.")
    sys.exit()

coin=[5000, 1000, 500, 100, 10, 1]

for x in coin:
    #매수를 계산
    howManyPapers = change // x
    #남은 금액을 계산
    change %= x
    #출력
    print(str(x), ':', str(howManyPapers))

    
