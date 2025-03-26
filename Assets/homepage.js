// Login and Authentication functionality

document.addEventListener('DOMContentLoaded', function() {
    // Login type selector handling
    const customerSelector = document.getElementById('customer-selector');
    const employeeSelector = document.getElementById('employee-selector');
    const customerForm = document.getElementById('customer-login-form');
    const employeeForm = document.getElementById('employee-login-form');

    customerSelector.addEventListener('click', function() {
        customerSelector.classList.add('active');
        employeeSelector.classList.remove('active');
        customerForm.classList.add('active');
        employeeForm.classList.remove('active');
    });

    employeeSelector.addEventListener('click', function() {
        employeeSelector.classList.add('active');
        customerSelector.classList.remove('active');
        employeeForm.classList.add('active');
        customerForm.classList.remove('active');
    });

    // Password visibility toggle
    const toggleButtons = document.querySelectorAll('.password-toggle');
    toggleButtons.forEach(button => {
        button.addEventListener('click', function() {
            const passwordField = this.previousElementSibling;
            if (passwordField.type === 'password') {
                passwordField.type = 'text';
                this.textContent = 'Hide';
            } else {
                passwordField.type = 'password';
                this.textContent = 'Show';
            }
        });
    });

    // Customer login form submission
    customerForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const username = document.getElementById('customer-username').value;
        const password = document.getElementById('customer-password').value;
        
        // Simple validation
        if (!username || !password) {
            showError('Please enter both username and password');
            return;
        }
        
        // For demo purposes, using mock authentication
        // In a real app, you would make an API call to verify credentials
        if (authenticateCustomer(username, password)) {
            // Store login info in session storage
            sessionStorage.setItem('userType', 'customer');
            sessionStorage.setItem('username', username);
            
            // Redirect to customer dashboard
            window.location.href = 'pages/customer/dashboard.html';
        } else {
            showError('Invalid username or password');
        }
    });

    // Employee login form submission
    employeeForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const username = document.getElementById('employee-username').value;
        const password = document.getElementById('employee-password').value;
        const employeeType = document.querySelector('input[name="employee-type"]:checked').value;
        
        // Simple validation
        if (!username || !password) {
            showError('Please enter both employee ID and password');
            return;
        }
        
        // For demo purposes, using mock authentication
        if (authenticateEmployee(username, password, employeeType)) {
            // Store login info in session storage
            sessionStorage.setItem('userType', employeeType);
            sessionStorage.setItem('username', username);
            
            // Redirect based on employee type
            if (employeeType === 'manager') {
                window.location.href = 'pages/manager/dashboard.html';
            } else {
                window.location.href = 'pages/admin/dashboard.html';
            }
        } else {
            showError('Invalid employee credentials');
        }
    });

    // Mock authentication functions (replace with actual API calls in production)
    function authenticateCustomer(username, password) {
        // Mock customer credentials for demo
        const validCustomers = [
            { username: 'customer1', password: 'password123' },
            { username: 'customer2', password: 'password123' }
        ];
        
        return validCustomers.some(customer => 
            customer.username === username && customer.password === password
        );
    }

    function authenticateEmployee(username, password, type) {
        // Mock employee credentials for demo
        const validEmployees = [
            { username: 'manager1', password: 'manager123', type: 'manager' },
            { username: 'admin1', password: 'admin123', type: 'admin' }
        ];
        
        return validEmployees.some(employee => 
            employee.username === username && 
            employee.password === password && 
            employee.type === type
        );
    }

    // Error display function
    function showError(message) {
        // Create error element if it doesn't exist
        let errorEl = document.querySelector('.error-message');
        if (!errorEl) {
            errorEl = document.createElement('div');
            errorEl.className = 'error-message';
            errorEl.style.color = 'var(--error-color)';
            errorEl.style.marginBottom = '1rem';
            errorEl.style.textAlign = 'center';
            errorEl.style.fontWeight = '500';
        }
        
        // Set message and display
        errorEl.textContent = message;
        
        // Insert before the active form's first child
        const activeForm = document.querySelector('.login-form.active');
        activeForm.insertBefore(errorEl, activeForm.firstChild);
        
        // Auto remove after 3 seconds
        setTimeout(() => {
            errorEl.remove();
        }, 3000);
    }
});