# Ayushmaan Mohanty
# Reg No: 2241013230
# Section: 2241028

def salary_bracket(gross_salary):
    if gross_salary < 50000:
        return "Low income"
    elif 50000 <= gross_salary <= 80000:
        return "Middle income"
    else:
        return "High income"

# Example usage
gross_salary_value = float(input("Enter your Gross Salary"))
print("Salary Bracket:", salary_bracket(gross_salary_value))
