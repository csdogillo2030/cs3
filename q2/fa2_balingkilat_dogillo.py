'''
Dogillo, Charlize Sky A.
9 - Balingkilat
Oct. 22, 2026
'''

class Patient:
    def __init__(self, name, bill_amount=0):
        self.name = name
        self.bill_amount = float(bill_amount)
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def get_bill_amount(self):
        return self.bill_amount
    
    def set_bill_amount(self, bill_amount):
        self.bill_amount = float(bill_amount)
    
    def calculate_bill(self):
        return self.bill_amount

class Senior(Patient):
    def __init__(self, name, sdiscount = 0.20, bill_amount = 0):
        super().__init__(name, bill_amount)
        self.sdiscount = sdiscount
    
    def get_sdiscount(self):
        return self.sdiscount
    
    def set_sdiscount(self, sdiscount):
        self.sdiscount = sdiscount
    
    def set_bill_amount(self, bill_amount):
        self.bill_amount = float(bill_amount)
    
    def calculate_bill(self):
        discount_amount = self.bill_amount * self.sdiscount
        return self.bill_amount - discount_amount

class PhilHealth(Patient):
    def __init__(self, name, pdiscount = 0.15, bill_amount = 0):
        super().__init__(name, bill_amount)
        self.pdiscount = pdiscount
    
    def get_pdiscount(self):
        return self.pdiscount
    
    def set_pdiscount(self, pdiscount):
        self.pdiscount = pdiscount
    
    def calculate_bill(self):
        discount_amount = self.bill_amount * self.pdiscount
        return self.bill_amount - discount_amount
       
patient1 = Patient("Katniss Everdeen", 15000)
patient2 = Senior("Haymitch Abernathy", 0.20, 15000)
patient3 = PhilHealth("Lucy Gray Baird", 0.15, 15000)

print("Hospital Billing System")
print("-----------------------")
print(f'Patient Name: {patient1.get_name()}')
print(f'Original Bill: ₱{patient1.get_bill_amount():,.2f}')
print(f'Final Bill: ₱{patient1.calculate_bill():,.2f}')
print("")
print(f'Patient Name: {patient2.get_name()}')
print(f'Original Bill: ₱{patient2.get_bill_amount():,.2f}')
print(f'Final Bill: ₱{patient2.calculate_bill():,.2f}')
print("")
print(f'Patient Name: {patient3.get_name()}')
print(f'Original Bill: ₱{patient3.get_bill_amount():,.2f}')
print(f'Final Bill: ₱{patient3.calculate_bill():,.2f}')
