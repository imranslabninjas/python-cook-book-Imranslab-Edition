# import datetime
# now = datetime.datetime.now()
# C_Date = now.strftime("%d-%m-%y")
# C_Time = now.strftime("%H:%M:S")
#
# for date in C_Date:
#     print(date)

# print("Current date and time is:")
# print(now.strftime("%y-%m-%d %H:%M:%S"))

age = 2022
birth_year = int(input("Enter your birth year: "))
age -= (birth_year)     #Augmented assignment operator.
print(f"Your current age is {age} years")   #Formatted string to simplify the code.