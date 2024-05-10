import sys

insert_price = input("Insert : ")
if not insert_price.isdecimal():
    print("Please input your insert money")
    sys.exit()

product_price = input("Product : ")
if not product_price.isdecimal():
    print("Please input your product price")
    sys.exit()

change = int(insert_price) - int(product_price)
if change < 0:
    print("Please Input your more money and try again")
    sys.exit()

coin=[5000, 1000, 500, 100, 50, 10, 1]

for i in coin:
    #How many papers the customer will take??
    howManyPapers, change = divmod(change, i)
    print(str(i), ':', str(howManyPapers))

    
