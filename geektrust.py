from sys import argv

CATEGORY = {
    "Clothing":['TSHIRT','JACKET','CAP'],
    "Stationery":['NOTEBOOK','PENS','MARKERS']
}

DISCOUNT_SALE = {
    "TSHIRT":{"RUP":1000,"sale":10},
    "JACKET":{"RUP":2000,"sale":5},
    "CAP":{"RUP":500,"sale":20},
    "NOTEBOOK":{"RUP":200,"sale":20},
    "PENS":{"RUP":300,"sale":10},
    "MARKERS":{"RUP":500,"sale":5}
}

"""
- For each clothing item, the maximum quantity that can be purchased is 2.
- For each stationery item, the maximum quantity that can be purchased is 3.
"""
def check_valid_quantity(limit,quantity):
    return quantity > limit
        
def calculate_tax(amount):
    return amount*10/100

def generate_bill(cart,discount):
    discount_amount = 0
    generated_amount = sum(cart)
    #Discounts can be applied only if the total purchase amount is 1000 rupees or more.
    if generated_amount >= 1000:
        for price,dis in zip(cart,discount):
            discount_amount += price*dis/100
            
    #An additional discount of 5% can be applied if the total amount to pay is 3000 rupees or more.   
    generated_amount -= discount_amount
    if generated_amount >= 3000:
        discount_amount += generated_amount*5/100
        generated_amount -= generated_amount*5/100
    #There is a 10% sales tax on total bill, after calculation taxes
    tax = calculate_tax(generated_amount)
    final_amount = tax + generated_amount
    print("TOTAL_DISCOUNT {:.2f}".format(discount_amount))
    print("TOTAL_AMOUNT_TO_PAY {:.2f}".format(final_amount))

def main():
    if len(argv) != 2:
        raise Exception("File path not entered")

    file_path = argv[1]
    f = open(file_path, 'r')
    lines = f.readlines()
    cart = []
    discount = []
    for line in lines:
        #read the input command and split
        #we have three list items: COMMAND, ITEM and Quantity
        #generate bill when PRINT_BILL is trigerred
        
        user_choice = line.split()
        if user_choice[0] == "PRINT_BILL":
            generate_bill(cart,discount)
            break
        
        command,item,quantity = user_choice
        
        quantity = int(quantity)
        if item in CATEGORY["Clothing"]:
            limit = 2
            if check_valid_quantity(limit,quantity):
                print("ERROR_QUANTITY_EXCEEDED")
            else:
                print("ITEM_ADDED")
                cart.append(DISCOUNT_SALE[item]['RUP']*quantity)
                discount.append(DISCOUNT_SALE[item]['sale'])
            
        elif item in CATEGORY["Stationery"]:
            limit = 3
            if check_valid_quantity(limit,quantity):
                print("ERROR_QUANTITY_EXCEEDED")
            else:
                print("ITEM_ADDED")
                cart.append(DISCOUNT_SALE[item]['RUP']*quantity)
                discount.append(DISCOUNT_SALE[item]['sale'])

if __name__ == "__main__":
    main()
