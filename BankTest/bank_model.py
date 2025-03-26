class Bank:
    def __init__(self):
        self.users = {}  # Stores user data
        self.admins = {"admin": "admin123"}  # Admin credentials
        self.transactions = []
    def register_user(self, username, password, balance=0):
        if username in self.users:
            return "User already exists"
        self.users[username] = {"password": password, "balance": balance}
        return "User registered successfully"

    def login(self, username, password):
        if username in self.users and self.users[username]["password"] == password:
            return "Login successful"
        return "Invalid credentials"

    def deposit(self, username, amount):
        if username in self.users and amount > 0:
            self.users[username]["balance"] += amount
            return f"Deposited ${amount} successfully"
        return "Deposit failed"

    def withdraw(self, username, amount):
        if username in self.users and self.users[username]["balance"] >= amount:
            self.users[username]["balance"] -= amount
            return f"Withdrawn ${amount} successfully"
        return "Insufficient funds"
    def transfer(self, sender, receiver, amount):
        if sender in self.users and receiver in self.users:
            if self.users[sender]["balance"] >= amount:
                self.users[sender]["balance"] -= amount
                self.users[receiver]["balance"] += amount
                self.transactions.append((sender, receiver, amount))
                return "Transfer successful"
            return "Insufficient funds"
        return "Transfer failed"

    def check_balance(self, username):
        if username in self.users:
            return f"Balance: ${self.users[username]['balance']}"
        return "User not found"

    def approve_loan(self, username, amount):
        if username in self.users and self.users[username]["balance"] > amount * 0.2:
            return "Loan approved"
        return "Loan denied"

    def logout(self, username):
        if username in self.users:
            return "User logged out"
        return "Logout failed"
