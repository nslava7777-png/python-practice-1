name = input("Enter customer name: ")
item_name1 = input("Enter name of item 1: ")
item_1_price = float(input("Enter price of item 1 (KZT): "))
item_name2 = input("Enter name of item 2: ")
item_2_price = float(input("Enter price of item 2 (KZT): "))
num_of_people = int(input("Enter number of people: "))

subtotal = item_1_price + item_2_price
tip = subtotal * 0.1
total = subtotal + tip
per_person = total / num_of_people

print("=" * 30)
print("CAFE BILL".center(30))
print("=" * 30)
print(f"{'Customer':<15} : {name:>7}")
print(f"{item_name1:<15} : {item_1_price:>8.1f} KZT")
print(f"{item_name2:<15} : {item_2_price:>8.1f} KZT")
print("-" * 30)
print(f"{'Subtotal':<15} : {subtotal:>8.1f} KZT")
print(f"{'Tip (10%)':<15} : {tip:>8.1f} KZT")
print(f"{'Total':<15} : {total:>8.1f} KZT")
print(f"{'Per person':<15} : {per_person:>8.1f} KZT")
print("-" * 30)
print(f"{'Tip included':<15} : {tip > 0}")
print(f"{'Bill over 5000 KZT':<15} : {total > 5000}")
print("=" * 30)
print("Thank you for dining with us!".center(30))