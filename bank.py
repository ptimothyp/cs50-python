class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self,n):
        self._balance += n

    def withdraw(self,n):
        global balance
        self._balance -= n

    def __str__(self):
        return f"Balance is  {self._balance}"



def main():
    account = Account()
    print(account)
    account.deposit(100)
    account.withdraw(10)

    print(account)


if __name__ == "__main__" :
    main()
