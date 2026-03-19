name = str(input("What is your name? "))
item_name1 = str(input("What is the name of the first item? "))
item_1_price = float(input("What is the price of the first item? "))
item_name2 = str(input("What is the name of the second item? "))
item_2_price = float(input("What is the price of the second item? "))
num_of_people = int(input("How many people are splitting the bill? "))

subtotal = item_1_price + item_2_price
tip = subtotal * 0.1
total = subtotal + tip
pre_person = total / num_of_people

print("=" * 30)
print("CAFE BILL".center(30))
print("=" * 30)
print(f"Customer : {name}")
print(f"{item_name1} : {item_1_price:.2f} KZT")
print(f"{item_name2} : {item_2_price:.2f} KZT")
print("-" * 30)
print(f"Subtotal : {subtotal:.1f} KZT")
print(f"Tip (10$) : {tip:.1f} KZT")
print(f"Total: {total:.1f} KZT")
print(f"Per person: {pre_person:.2f} KZT")
print("-" * 30)
print("Tip included: ", tip >0)
print("Bill over 5000  KZT: ", total > 5000)
print("=" * 30)
print("Thank you for dining with us!".center(30))