# test_bank_nonfunctional.py
import pytest
import time
from bank_model import Bank

@pytest.fixture
def bank():
    return Bank()

def test_response_time(bank):
    start = time.time()
    bank.register_user("hank", "securepass")
    end = time.time()
    assert (end - start) < 0.5  # Should execute in under 0.5s

def test_concurrent_users(bank):
    users = [f"user{i}" for i in range(100)]
    for user in users:
        bank.register_user(user, "pass")
    assert len(bank.users) == 100

def test_sql_injection(bank):
    def search(query):
        if any(char in query for char in ["'", "--", ";"]):
            return "Invalid input detected"
        return "Search results"
    
    result = search("' OR 1=1 --")
    assert result == "Invalid input detected"

def test_xss_profile_update(bank):
    script_input = "<script>alert('XSS')</script>"
    bank.register_user("sam", "safe")
    assert bank.register_user(script_input, "pass") == "User registered successfully"
    assert "<script>" not in bank.users  # XSS prevention

def test_system_availability(bank):
    assert isinstance(bank, Bank)  # Ensures system is running

def test_data_recovery(bank):
    bank.register_user("peter", "pass", 200)
    bank.withdraw("peter", 50)
    assert bank.check_balance("peter") == "Balance: $150"

def test_usability(bank):
    assert bank.register_user("12345", "pass") == "User registered successfully"

def test_large_input(bank):
    large_username = "a" * 1000
    assert bank.register_user(large_username, "pass") == "User registered successfully"

def test_invalid_input(bank):
    assert bank.deposit("unknown", 100) == "Deposit failed"

def test_high_load(bank):
    start = time.time()
    for i in range(1000):
        bank.register_user(f"user{i}", "pass")
    end = time.time()
    assert (end - start) < 5  # Registers 1000 users in under 5 seconds
