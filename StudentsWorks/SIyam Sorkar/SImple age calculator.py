                        #The simple one to calculate only the year

age = 2022
birth_year = int(input("Enter your birth year: "))
age -= (birth_year)     #Augmented assignment operator.
print(f"Your are currently {age} years old")   #Formatted string to simplify the code.





        #The perfect one for calculating exact year month and days. Note: It's not done yet

import datetime
# current_date  = int(datetime.datetime.now().strftime("%d"))
# current_month = int(datetime.datetime.now().month)
# current_year  = (datetime.datetime.year)

# birth_date    = int(input("Enter your birth Date  here:    "))
# birth_month   = int(input("Enter your birth month here:    "))
# birth_year    = int(input("Enter your birth Year  here:    "))

# age_date      = current_date  - birth_date
# age_month     = current_month - birth_month
# age_year      = 2022  - birth_year

# print(f"Your current age is {age_year} year {age_month} month {age_date} days")