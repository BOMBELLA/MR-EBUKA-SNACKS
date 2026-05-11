total_bill = int(input("Enter total bill: "))
is_member = str("Are you a member? ")

discount_percentage = 10/100
discount = total_bill - discount_percentage


if total_bill >= 1000 and is_member == "yes":
    print("10% off")
elif total_bill >= 1000 and is_member != "No":
    print("5% off")
else:
    print("No discount")
print (discount)
