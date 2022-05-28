##Function Create
class Purchase(object):
    def __init__(self, amount):
        self.amount = amount
        
    def calculateTax(self, taxPercent):
        return self.amount * taxPercent/100.0

    def calculateTip(self, tipPercent):
        return self.amount * taxPercent/100.0

    def calculateTotal(self, taxPercent, tipPercent):
        return self.amount * (1 + taxPercent/100.0 + tipPercent/100.0)

#Generate value, again through input
purchase = Purchase(float(input("How much did you spend?")))

#Set values. I wanted to make these input too, but I don't have the time ='(
taxPercent = 7.5
tipPercent = 20.0

#Defining terms
tax = purchase.calculateTax(taxPercent)
tip = purchase.calculateTip(tipPercent)

#Results
print('Tax: ',round(tax,2))
print('Tip: ',round(tip,2))
print('Total: ', round(purchase.calculateTotal(taxPercent, tipPercent),2))
print('\nCode by Michael Pogue')