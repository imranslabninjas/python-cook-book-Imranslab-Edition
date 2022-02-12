#It's a simple calculator for doing Addition, Subtraction, Multiplication, Division and Percentage.

first_number    = int(input("Enter your first number: "))
operators       = input("Enter what you wanna do +,-,*,/,%: ")
second_number   = int(input("Enter your second Number: "))

if operators == "+" :
    first_number +=  second_number
    print(f"Your Addition result is: {first_number}")
elif operators == "-" :
    first_number -= second_number
    print(f"Your Subtraction result is: {first_number}")
elif operators == "*" :
    first_number *= second_number
    print(f"Your Multiplication result is: {first_number}")
elif operators == "/" :
    first_number /= second_number
    print(f"Your Division result is: {first_number}")
elif operators == "%" :
    first_number %= second_number
    print(f"Your Modulus result is: {first_number}")
else :
    print("You have chosen a wrong operator")