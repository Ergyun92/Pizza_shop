import os,time

pizzas = []
try:
    with open("pizzashop.txt", "r") as f:
        pizzas = eval(f.read())
except:
    print("ERROR: No existing pizza list")

def addPizza():
    time.sleep(1)
    os.system("clear")
    name = input("Name: ")
    toppings = input("Toppings: ")
    size = input("Size (s/m/l): ")
    while True:
        try:
            qty = int(input("Quantity: "))
            break
        except:
            print("ERROR: Quantity must be a whole numerical number!")
    cost = 0
    if size == "s":
        cost = 5.99
    elif size == "m":
        cost = 9.99
    else:
        cost = 14.99
    total = cost * float(qty)
    total = round(total, 2)
    row = [name, toppings, size, qty, total]
    pizzas.append(row)

def viewPizza():
    h1 = "Name"
    h2 = "Topping"
    h3 = "Size"
    h4 = "Quantity"
    h5 = "Total"
    print(f"{h1:^10}{h2:^10}{h3:^10}{h4:^10}{h5:^10}")
    for row in pizzas:
        print(f"{row[0]:^10}{row[1]:^10}{row[2]:^10}{row[3]:^10}{row[4]:^10}")


while True:
    time.sleep(2)
    os.system("clear")
    print("Ergyun's super-duper pizzas")
    print()
    menu = input("1: Add Pizza\n2: View Pizzas\n> ")
    if menu == "1":
        addPizza()
    else:
        viewPizza()
    with open("pizzashop.txt", "w") as f:
        f.write(str(pizzas))
