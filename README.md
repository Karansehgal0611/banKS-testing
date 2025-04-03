# # 🏦 banKS - Testing Documentation

## 📌 Overview
This document provides an overview of the testing process conducted for the **banKS - Online Bank Management System** project. The testing phase includes **functional** and **non-functional** test cases executed using **pytest** to ensure the reliability, security, and performance of the system.

## 🔍 Testing Objectives
- Validate the **core functionalities** of the banking system.
- Ensure data integrity and security measures.
- Test the **user authentication**, transactions, and loan approval system.
- Measure the **performance** of key operations.
- Check for **UI/UX consistency** and usability.

## 🛠️ Tools & Technologies Used
- **Python** for backend logic
- **Pytest** for automated testing
- **SQLite/MySQL** for database testing
- **Postman** for API testing

---

## 🧪 Functional Test Cases
Functional tests ensure that the system's core operations work as expected.

| **Test Case ID** | **Test Description** | **Expected Result** | **Status** |
|---------------|----------------|------------------|-----------|
| TC-01 | User registration with valid credentials | User successfully registered | ✅ |
| TC-02 | Login with correct credentials | Redirect to dashboard | ✅ |
| TC-03 | Login with incorrect credentials | Error message displayed | ✅ |
| TC-04 | Check account balance retrieval | Displays correct balance | ✅ |
| TC-05 | Money transfer between accounts | Amount deducted & credited correctly | ✅ |
| TC-06 | Withdrawal exceeding balance | Transaction denied | ✅ |
| TC-07 | Loan approval process | Approved only if conditions met | ✅ |
| TC-08 | Loan rejection for insufficient balance | Loan denied | ✅ |
| TC-09 | Logout functionality | User successfully logged out | ✅ |
| TC-10 | Session timeout handling | User redirected to login page | ✅ |

---

## ⚙️ Non-Functional Test Cases
These tests focus on system performance, security, and usability.

| **Test Case ID** | **Test Description** | **Expected Result** | **Status** |
|---------------|----------------|------------------|-----------|
| NFT-01 | Load testing for concurrent users (100 users) | System handles load without failure | ✅ |
| NFT-02 | Security test: SQL Injection attempt | System prevents unauthorized access | ✅ |
| NFT-03 | Security test: XSS attack attempt | Input fields sanitize malicious scripts | ✅ |
| NFT-04 | Performance test: Account balance retrieval speed | Response time < 1s | ✅ |
| NFT-05 | Usability test: Responsive design across devices | UI adjusts correctly | ✅ |
| NFT-06 | Accessibility check for visually impaired users | Meets WCAG guidelines | ✅ |
| NFT-07 | Database recovery test after crash | Data remains intact | ✅ |
| NFT-08 | Stress test: 1000 transactions in 1 min | No major performance degradation | ✅ |
| NFT-09 | API response time for critical operations | < 500ms | ✅ |
| NFT-10 | Error handling for unexpected inputs | System shows meaningful error messages | ✅ |

---

## 🚀 Running the Tests
To execute the test cases using **pytest**, follow these steps:

```bash
# Install pytest if not installed
pip install pytest

# Navigate to the project directory
cd banKS

# Run all test cases
pytest

# Run specific test file
pytest test_banks.py

# Generate a test report
pytest --html=report.html --self-contained-html
```

## 📈 Test Summary
✅ All functional and non-functional test cases have been successfully executed. The **banKS** system meets the required standards for **functionality, security, performance, and usability**. 🚀

---

### 📌 Next Steps
- Integrate continuous testing into CI/CD pipeline.
- Optimize response time for high-load scenarios.
- Conduct further penetration testing to enhance security.

---

📌 **Developed & Tested by:** *Karan Sehgal* 👨‍💻
