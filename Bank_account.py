import sys 
# import array as arr

# For getting input from input.txt file 
sys.stdin = open('input.txt', 'r')  
  
# Printing the Output to output.txt file 
sys.stdout = open('output.txt', 'w') 


#Define a class fro bank account.
class BankAccount :
    def __init__(self,owner,balance=0):
        """constructor to initialize the owner  and balance"""
        self.owner=owner  #public attribute
        self.__balance=balance #private attribute(encapsulation)
    def deposite(self,amount):
        """MEthod to Deposite money"""
        if amount>0:
            self.__balance+=amount
            print(f"{amount} deposited successful.")  
        else:
            print("Deposite amount must be positive.")
    def withdraw(self,amount):
        """Method to withdraw money"""
        if 0< amount<=self.__balance:
            self.__balance-=amount
            print(f"{amount} withdraw successful.")  
        else:
            print("Insufficient balance or Invalide balance. ")
    def check_balance(self):
        """Method to check your balance"""
        print(f"Current balance: {self.__balance}")


# Subclass of BankAccount demonstrate Inheritance
class SavingAccount(BankAccount):
    def __init__(self,owner, balance=0,interest=0.02):
        super().__init__(owner, balance)


account=BankAccount("Vishal",1000)
account.deposite(500)
account.withdraw(200)
account.check_balance()

#hello