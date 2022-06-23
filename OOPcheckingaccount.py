class CheckingAccount:
    overdraft_limit = 3500

    def __init__(self, owner, nr):
        self.owner = owner
        self.nr = nr
        self.balance = 0
        self.history = ["Account opening: 0 EUR"]

    def deposit(self, amount, note):
        self.balance += amount
        self.history.append("{}: +{} EUR".format(note,amount))
    def withdraw(self, amount, note):
        if amount > self.balance + CheckingAccount.overdraft_limit:
            raise Exception("Insufficient funds!")
        self.balance -= amount
        self.history.append("{}: -{} EUR".format(note,amount))
    def transfer (self, target_account, amount, note):
        self.withdraw(amount, note)
        target_account.deposit(amount, note)
    def statement(self):
            print("\n{}, Account Nr. {}\n{}".format(self.owner, self.nr, 35* "-"))
            for entry in self.history:
                print(entry)
            print("{}\nBalance: {} EUR".format(35* "-", self.balance))
            self.history = ["Balance: {} EUR".format(self.balance)]

m = CheckingAccount("Jane Smith", 123334)
w = CheckingAccount("John Doe", 9485)

m.deposit(200, "Cash deposit")
m.deposit(1938.5, "Salary")
m.deposit(345, "Dividends")
m.withdraw(87.4, "Purchase")
m.transfer(w, 1124, "Rent")

m.statement()