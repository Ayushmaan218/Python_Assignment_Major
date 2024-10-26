# Ayushmaan Mohanty
# Reg No: 2241013230
# Section: 2241028

def basic_salary(hourly_rate, hours_per_week):
    return hourly_rate * hours_per_week * 4

def tax_amount(basic_salary):
    if basic_salary < 60000:
        return basic_salary * 0.10
    elif 60000 <= basic_salary <= 85000:
        return basic_salary * 0.15
    else:
        return basic_salary * 0.20

def gross_salary(hourly_rate, hours_per_week):
    basic = basic_salary(hourly_rate, hours_per_week)
    allowances = basic * 0.20
    tax = tax_amount(basic)
    return basic + allowances - tax


hourly_rate = float(input("Enter the Salary for an hour:"))
hours_per_week = float(input("Hours Worked per Week:"))
print("Gross Salary:", gross_salary(hourly_rate, hours_per_week))
