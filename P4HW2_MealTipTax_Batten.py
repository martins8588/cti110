#CTI110
#P4HW2 Meal, Tip, Tax
#Shyann Batten
#10/21/19


Percent_sales_tax = 0.06

foodCharge = float(input("What is the price of the food?:"))
tip_percentage = float(input("What is the tip amount?;"))
if tip_percentage != .16 or tip_percentage != .18 or tip_percentage != .20:
    print("Error. tip needs to be .16, .18, .20.")

tip = (foodCharge * tip_percentage)


salesTax = (foodCharge * Percent_sales_tax)
total = (foodCharge + tip + salesTax)

print('The tip is',format(tip, '.2f'))
print('The salesTax is',format(salesTax, '.2f'))
print('The total is',format(total, '.2f'))

while True:
    #main program
    while True:
        answer = input('Run again? (y/n): ')
        if answer in ('y', 'n'):
            break
        print ('Invalid input.')
    if answer == 'y':
        continue
    else:
        print ('Goodbye')
        break
   
