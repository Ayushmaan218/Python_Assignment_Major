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

def salary_bracket(gross_salary):
    if gross_salary < 50000:
        return "Low income"
    elif 50000 <= gross_salary <= 80000:
        return "Middle income"
    else:
        return "High income"

def employee_report():
    employees = []
    
    for i in range(3):
        print(f"\nEnter details for Employee {i+1}:")
        name = input("Name: ")
        hourly_rate = float(input("Hourly Rate (in Rs): "))
        hours_per_week = int(input("Hours Worked per Week: "))
        
        employees.append({
            "name": name,
            "hourly_rate": hourly_rate,
            "hours_per_week": hours_per_week
        })
    
    for emp in employees:
        name = emp["name"]
        hourly_rate = emp["hourly_rate"]
        hours_per_week = emp["hours_per_week"]

        basic = basic_salary(hourly_rate, hours_per_week)
        gross = gross_salary(hourly_rate, hours_per_week)
        tax = tax_amount(basic)
        bracket = salary_bracket(gross)

        print(f"\nEmployee Name: {name}")
        print(f"Basic Salary: Rs. {basic}")
        print(f"Gross Salary: Rs. {gross}")
        print(f"Tax Amount: Rs. {tax}")
        print(f"Salary Bracket: {bracket}")
        print("-" * 30)

employee_report()
