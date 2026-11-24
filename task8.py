material = float(input("Enter material cost: "))
labour = float(input("Enter labour cost: "))
machine = float(input("Enter machine cost: "))
wastage = float(input("Enter wastage cost: "))
selling = float(input("Enter selling price: "))
quantity = int(input("Enter quantity produced: "))

total_cost = material + labour + machine + wastage
total_sales = selling * quantity

profit = total_sales - total_cost

print("Total Production Cost:", total_cost)
print("Total Sales:", total_sales)
print("Profit:", profit)

if profit > 0:
    print("Production is Profitable")
elif profit == 0:
    print("No Profit No Loss")
else:
    print("Production is in Loss")