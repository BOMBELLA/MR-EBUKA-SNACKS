first_number = int(input(" Enter first number; "))
second_number = int(input("Enter second number "))

if first_number > 0 and second_number > 0:
    print("Q1")
elif first_number < 0 and second_number > 0:
    print("Q2")
elif first_number < 0 and y <0:
    print("Q3")
elif first_number > 0 and second_number < 0:
    print("Q4")
elif first_number == 0 and second_number ==0:
    print("Origin")
elif first_number != 0 and second_number == 0:
    print("X-axis")
elif first_number == 0 and second_number == 0:
    print("Y-axis")
else:
       print("invalid")
