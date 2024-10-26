# Ayushmaan Mohanty
# Reg No: 2241013230
# Section: 2241028

def tax_amount(basic_salary):
    if basic_salary < 60000:
        tax = basic_salary * 0.10
    elif 60000 <= basic_salary <= 85000:
        tax = basic_salary * 0.15
    else:
        tax = basic_salary * 0.20
    return tax

basic_salary_value = float(input("Enter the basic Salary:"))
print("Tax Amount:", tax_amount(basic_salary_value))
