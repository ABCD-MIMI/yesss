import datetime
class BankAccount:
    def __init__(self, id, name, email, address, account_type):
        self.id = id
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.transactions = []
        self.loans_taken = 0

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(("deposit", amount, datetime.datetime.now()))
        return f"Deposited {amount}. New balance: {self.balance}"

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(("withdraw", -amount, datetime.datetime.now().date()))
            return f"Successfully withdrew {amount}. New balance: {self.balance}"
        else:
            print("Insufficient funds in your account or bank is bankrupt.")

    def check_balance(self):
        return self.balance

    def get_transactions(self):
        return f"transaction id:{self.transactions}"

    def loan(self, amount):
        if self.loans_taken < 2:
            if self.balance >= amount:
                self.balance += amount
                self.loans_taken += 1
                self.transactions.append(("loan", amount, datetime.datetime.now().date()))
                return f"Received loan of {amount}. New balance: {self.balance}"
            elif amount>0:
                print("The bank is bankrupt.")
        else:
            print("You have reached your loan limit.")

    def __repr__(self):
        return f"BankAccount(id={self.id}, name={self.name}, email={self.email}, account_type={self.account_type}, balance={self.balance})"


class Admin:
    accounts = []

    def __init__(self, email, password):
        self.email = email
        self.password = password
        # Rest of the init function here

    def create_account(self, id, name, email, address, account_type):
        new_account = BankAccount(id, name, email, address, account_type)
        self.accounts.append(new_account)
        return f"Account created. ID: {new_account.id}"
    def remove_account(self, id):
        for account in self.accounts:
            if account.id == id:
                self.accounts.remove(account)
                return f"Account deleted successfully.ID:{account.id}"
        return "Account not found"

    def find_account(self, id):
        for user in self.accounts:
            if user.account.id == id:
                return user.account
        return None

    def get_all_accounts(self):
        return self.accounts
    def get_total_balance(self):
        return sum(account.balance for account in self.accounts)

    def get_total_loan_amount(self):
        return sum(account.loans_taken for account in self.accounts)

    def toggle_loan_feature(self):
        self.loan_feature = not self.loan_feature

    def transfer(self, to_id, amount):
        to_account = self.admin.find_account(to_id)
        if to_account is not None:
            if self.account.balance >= amount:
                self.account.balance -= amount
                to_account.balance += amount
                print(f"{amount} transferred from your account to account ID {to_id}")
            else:
                print("Insufficient funds in your account for this transfer!")
        else:
            print("Account does not exist")



class User():

    def __init__(self, name, email, password, id, account_type):
        self.name = name
        self.email = email
        self.password = password
        self.account = BankAccount(id, name, email, 'address', account_type)

    def __repr__(self):
        return f"User(name={self.name}, email={self.email}, account={self.account})"

admin = Admin('admin@email.com', 'password')

while True:
    user_type = input("admin/user ? : ")
    if user_type == 'user':
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        ch = int(input("Enter your choice : "))

        if ch == 1:
            email = input("Enter your email : ")
            password = input("Enter your password : ")

            flag = False
            for user in admin.accounts:
                if user.email == email and user.password == password:
                    flag = True
                    print("Welcome ", user.name)
                    while True:
                        print("Options:\n")
                        print("1: Check available balance")
                        print("2: Check deposit amount")
                        print("3: Check withdraw amount")
                        print("4: Check transaction history")
                        print("5: Take a loan")
                        print("6: Transfer the amount")
                        print("7: Logout")

                        ch = int(input("\nEnter Option:"))

                        if ch == 1:
                            print(user.account.check_balance())
                        elif ch == 2:
                            amount = int(input("\tEnter deposit amount:"))
                            print(user.account.deposit(amount))
                        elif ch == 3:
                            amount = int(input("\tEnter withdraw amount:"))
                            print(user.account.withdraw(amount))
                        elif ch == 4:
                            print(user.account.get_transactions())
                        elif ch == 5:
                            amount = int(input("\tEnter loan amount:"))
                            print(user.account.loan(amount))
                        elif ch == 6:
                            to_id = input("\tEnter account id to transfer to:")
                            amount = int(input("\tEnter amount to transfer:"))
                            to_account = admin.find_account(to_id)
                            if to_account is not None:
                                print(admin.transfer(amount, user.account.id, to_id))
                        elif ch == 7:
                            break
                        else:
                            print("\n\t---> !!! Choose A Valid Option\n")

            if flag == False:
                print("Wrong email or password.")




        elif ch == 2:
            name = input("Enter your name : ")
            email = input("Enter your email : ")
            password = input("Enter your password : ")
            id = input("Enter your id : ")
            account_type = input("Enter your account type : ")

            new_user = User(name, email, password, id,account_type)
            admin.accounts.append(new_user)
            print("Registered successfully.")



        else:
            break

    elif user_type == 'admin':
        email = input("Enter your email : ")
        password = input("Enter your password : ")

        if email == 'admin@email.com' and password == 'password':

            print("Admin successfully login.")
            while True:
                print("Options:\n")
                print("1: Create account")
                print("2: Remove account")
                print("3: Find account")
                print("4: Get all accounts")
                print("5: Get total balance")
                print("6: Get total loan amount")
                print("7: Logout")

                ch = int(input("\nEnter Option:"))



                if ch == 1:
                    id = input("\tEnter account id:")
                    name = input("\tEnter account name:")
                    email = input("\tEnter account email:")
                    address = input("\tEnter account address:")
                    account_type = input("\tEnter account type:")
                    print(admin.create_account(id, name, email, address, account_type))


                elif ch == 2:
                    id = input("\tEnter account id to delete:")
                    print(admin.remove_account(id))
                elif ch == 3:
                    id = input("\tEnter account id to find:")
                    account = admin.find_account(id)
                    if account is not None:
                        print(account.name)
                elif ch == 4:
                    print(admin.get_all_accounts())
                elif ch == 5:
                    print(admin.get_total_balance())
                elif ch == 6:
                    print(admin.get_total_loan_amount())
                elif ch == 7:
                    break
        else:
            print("Wrong email or password.")

    else:
        print("Invalid")

