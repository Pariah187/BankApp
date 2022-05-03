class Account():
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = balance
        self.password = password

    def deposit(self, amount_to_deposit, password):
        if password != self.password:
            print('Sorry, incorrect password')
            return None
        self.balance = self.balance + amount_to_deposit
        return self.balance

    def withdraw(self, amount_to_withdraw, password):
        if password != self.password:
            print('Sorry, incorrect password')
            return None

        if amount_to_withdraw < 0:
            print('You cannot withdraw a negative amount')
            return None

        if amount_to_withdraw > self.balance:
            print('You cannot withdraw more currency than is currently held in this account')
            return None

        self.balance = self.balance - amount_to_withdraw
        return self.balance

    def get_balance(self, password):
        if password != self.password:
            print('Sorry. Incorrect password')
            return None
        return self.balance

    # Added for debugging
    def show(self):
        print('     Name:', self.name)
        print('     Balance:', self.balance)
        print('     Password:', self.password)
        print()


