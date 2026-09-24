'''
Charlize Sky A. Dogillo
September 24, 2026
'''

#bank, acc, savings acc
#i probably wont finish this on time
print("Welcome to Metrobank")

class Bank:
  def __init__(self, name, number, type, balance= 0, accounts):
    self.accounts = Account()
  def openAccount(self):
    print("Ready to open an account")
    accname = str(input("Account Name: "))
    accnumber = str(input("Account Number: "))
    acctype = str(input("Account Type (savings or checking): "))
    print("Account Created")
    print(f"{self.name) [{self.number}] P {self.__balance}")
    
  def showAccounts(self):
    
  def deposit(self):
    
  def addInterest():
    
  def closeAccount():

  def __del__(self):
    

class Account:
  def __init__(name, number, type, balance= 0):
    self.name = accname
    self.number = accnumber
    self.type = acctype
    self.__balance = balance
    

class SavingsAccount(Account):
  def __init__(self, name, number, balance= 0, interest= 0.05):
    super().__init__(name, number, balance= 0)
    self.interest = interest
  

mbtc = Bank("Metrobank")
mbtc.openAccount()
mbtc.openAccount()
mbtc.showAccounts()
mbtc.deposit()
mbtc.deposit()
mbtc.addInterest()
mbtc.closeAccount()
del bank #(add later)
