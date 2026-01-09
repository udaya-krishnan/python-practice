bill = float(input("Enter your bill amount :"))
tax_rate = int(input("Enter your tax rate :"))

def Total_rate (bill,tax_rate) :
    return (bill*tax_rate)/100

print("your total amount is ",Total_rate(bill,tax_rate))