class BalanceException(Exception):
    pass
class BankAccount:
    def __init__(self,initialamount,accountname):
        self.balance=initialamount
        self.accountname=accountname

        print("account " + self.accountname + " created ✅." )
        print("balance: " + "$" ,"{:.2f}".format(self.balance))
    def getbalance(self):

        print("account "+ self.accountname)
        print("balance: " + "$" ,"{:.2f}".format(self.balance))


    def deposit(self,amount):

        self.balance=self.balance+amount
        print("Deposit completed 📩")
        self.getbalance()

    def viable_transaction(self,amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException( "sorry " + self.accountname + " only has a balance of $" + "{:.2f}".format(self.balance) )


    def withdraw(self,amount):
        try:
            self.viable_transaction(amount)
            self.balance=self.balance-amount
            print("Withdraw completed 👍")
            self.getbalance()
        except BalanceException as error:
            print("Withdraw failed 🙁" + str(error))

    def transfer(self,amount,accountname):
        try:
            print("**********Beggining Transfer 🚀 ****************")
            self.viable_transaction(amount)
            self.withdraw(amount)
            accountname.deposit(amount)
            print("Transfer completed ✅")
        except BalanceException as error:
            print("Transfer failed 🙁" + str(error))

class IntrestRewardAct(BankAccount):
    def deposit(self,amount):
        self.balance=self.balance+(amount * 1.05)
        print("Deposit completed ✔️")
        self.getbalance()

class SavingsAccount(IntrestRewardAct):
    def __init__(self,initialamount,accountname):
        super().__init__(initialamount,accountname)
        self.fee = 5

    def withdraw(self,amount):
        try:
            self.viable_transaction(amount + self.fee)
            self.balance=self.balance-(amount + self.fee)
            print("Withdraw completed ")
            self.getbalance()
        except BalanceException as error:
            print("Withdraw failed ")

prithi= BankAccount(2000,"prithi")
gayathri= BankAccount(2000,"gayathri")
prithi.getbalance()
gayathri.getbalance()
prithi.deposit(500)
gayathri.deposit(1000)
prithi.withdraw(500)
prithi.transfer(1000,gayathri)
swathi = IntrestRewardAct(1000,"swathi")
swathi.getbalance()
swathi.deposit(500)
devi = SavingsAccount(5000,"devi")
devi.getbalance()
devi.withdraw(500)