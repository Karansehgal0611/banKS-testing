# test_bank_functional.py
import pytest
from bank_model import Bank

@pytest.fixture
def bank():
    return Bank()

def test_register_user(bank):
    assert bank.register_user("alice", "password123") == "User registered successfully"
    assert bank.register_user("alice", "password123") == "User already exists"

def test_login(bank):
    bank.register_user("bob", "securepass")
    assert bank.login("bob", "securepass") == "Login successful"
    assert bank.login("bob", "wrongpass") == "Invalid credentials"

def test_deposit(bank):
    bank.register_user("charlie", "mypassword")
    assert bank.deposit("charlie", 100) == "Deposited $100 successfully"
    assert bank.check_balance("charlie") == "Balance: $100"

def test_withdraw(bank):
    bank.register_user("david", "pass123", 200)
    assert bank.withdraw("david", 100) == "Withdrawn $100 successfully"
    assert bank.withdraw("david", 200) == "Insufficient funds"

def test_transfer(bank):
    bank.register_user("alice", "pass", 300)
    bank.register_user("bob", "pass", 100)
    assert bank.transfer("alice", "bob", 100) == "Transfer successful"
    assert bank.transfer("alice", "bob", 300) == "Insufficient funds"

def test_check_balance(bank):
    bank.register_user("eve", "password", 500)
    assert bank.check_balance("eve") == "Balance: $500"

def test_admin_approval(bank):
    assert bank.admins["admin"] == "admin123"

def test_loan_approval(bank):
    bank.register_user("frank", "secure", 500)
    assert bank.approve_loan("frank", 1000) == "Loan approved"
    assert bank.approve_loan("frank", 200) == "Loan approved"

def test_failed_login(bank):
    assert bank.login("unknown_user", "password") == "Invalid credentials"

def test_logout(bank):
    bank.register_user("grace", "mypassword")
    assert bank.logout("grace") == "User logged out"
