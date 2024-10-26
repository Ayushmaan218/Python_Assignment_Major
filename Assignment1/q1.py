# Ayushmaan Mohanty
# Reg No: 2241013230
# Section: 2241028

def basic_salary(hourly_rate, hours_per_week):
    basic_monthly_salary = hourly_rate * hours_per_week * 4
    return basic_monthly_salary

def overtime_salary(hourly_rate, hours_per_week):
    if hours_per_week > 40:
        overtime_hours = hours_per_week - 40
        overtime_payment = overtime_hours * hourly_rate * 1.5 * 4
        return overtime_payment
    return 0

def total_salary(hourly_rate, hours_per_week):
    basic = basic_salary(hourly_rate, hours_per_week)
    overtime = overtime_salary(hourly_rate, hours_per_week)
    return basic + overtime


hourly_rate = float(input("Enter the rate for an hour:"))
hours_per_week = float(input("Hours Worked per Week:"))
print("Basic Salary:", basic_salary(hourly_rate, hours_per_week))
print("Overtime Salary:", overtime_salary(hourly_rate, hours_per_week))
print("Total Salary:", total_salary(hourly_rate, hours_per_week))