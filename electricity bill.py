#bill calculator
ID = int(input('Enter your CustomerID :'))
Name = input('Enter your CustomerName :')
Unitconsumed =float(input('Enter your unitconsumed :'))

#calculating the total bill
def total_bill(Unitconsumed):
    if Unitconsumed <= 199 :
        total_bill= Unitconsumed * 1.20
    elif Unitconsumed >= 200 and Unitconsumed <= 400 :
        total_bill= Unitconsumed * 1.50
    elif Unitconsumed > 400 and Unitconsumed < 600:
        total_bill= Unitconsumed * 1.80
    elif Unitconsumed > 600:
        total_bill= Unitconsumed * 2.00
    return total_bill
print(f'Dear {Name} Your Total bill is {total_bill(Unitconsumed)}')




