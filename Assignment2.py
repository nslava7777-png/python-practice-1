subtotal = 0.0
tip = 0.0
items_count = 0
discount = 0.0
disk = "None"

name = input("Enter customer name: ")
#
if name[0].upper() in ["A", "S", "V"]: 
    status = "VIP"
    print("Welcome, VIP customer!")
else:
    status = "Regular"
    print("Welcome to our cafe!")

#
while True:
    item_name = input("Enter name of item (or 'done' to finish): ")
    if item_name.lower() == 'done':
        break
    item_price = float(input(f"Enter price of {item_name} (KZT): "))
    subtotal += item_price
    items_count += 1

num_of_people = int(input("Enter number of people: "))

#
while True:
    try:
        time = int(input("Enter time of day (0 - 23): "))
        if 0 <= time <= 23: 
            break
        else:       
            print("Time must be between 0 and 23.")
    except ValueError:
        print("Invalid input for time. Please enter an integer") 

#
if 17 <= time < 22:
    disk = "Time period: Evening"
    discount = subtotal * 0.05
elif 12 <= time < 17:
    disk = "Time period: Afternoon"
    discount = 0
elif 6 <= time < 12:
    disk = "Time period: Morning"
    discount = subtotal * 0.1
else: 
    print("Closed") 
    exit()

#
tip = (subtotal - discount) * 0.1
total = subtotal - discount + tip
per_person = total / num_of_people

# 
print("\n" + "-" * 30)
print("NAME ANALYSIS".center(30))
print("-" * 30)

print(f"{'Name Uppercase':<18} : {name.upper():>9}")
print(f"{'Name Lowercase':<18} : {name.lower():>9}")
print(f"{'Name Length':<18} : {len(name):>7} letters") 
print(f"{'Customer Status':<18} : {status:>9}")
print("-" * 30)

#
print("\n" + "=" * 30)
print("CAFE BILL".center(30))
print("=" * 30)

print(f"{'Customer':<15} : {name.upper():>12}")
print(f"{'Items':<15} : {items_count:>12}")
print(f"{'Subtotal':<15} : {subtotal:>9.1f} KZT")
print("-" * 30)

print(disk.center(30))
print(f"{'Discount':<15} : {discount:>9.1f} KZT")
print(f"{'Tip (10%)':<15} : {tip:>9.1f} KZT")
print(f"{'Total':<15} : {total:>9.1f} KZT")
print(f"{'Per person':<15} : {per_person:>9.1f} KZT")
print("-" * 30)

print(f"{'Tip included':<18} : {str(tip > 0):>9}")    
print(f"{'Bill over 5000':<18} : {str(total > 5000):>9}")
print("=" * 30)
print("Thank you for dining with us!".center(30))