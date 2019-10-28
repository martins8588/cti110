#CTI110
#P3HW2-MealTipTax
#Shyann Batten
#10/09/19
#Program prompts user to enter charge for the meal.
#Program calculates the tax and tip once it is entered.


Percent_sales_tax = 0.06

foodCharge = float(input("What is the price of the food?:"))
tip_percentage = float(input("What is the tip amount?;"))
if tip_percentage != .16 or tip_percentage != .18 or tip_percentage != .20:
    print("Error. tip needs to be .16, .18, .20. defaulting to .16")
    tip_percentage = .16

tip = (foodCharge * tip_percentage)


salesTax = (foodCharge * Percent_sales_tax)
total = (foodCharge + tip + salesTax)

print('The tip is',format(tip, '.2f'))
print('The salesTax is',format(salesTax, '.2f'))
print('The total is',format(total, '.2f'))



