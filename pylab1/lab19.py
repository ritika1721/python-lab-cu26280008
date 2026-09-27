

principal = float(input("Enter loan amount: "))
annual_rate = float(input("Enter annual interest rate: "))
years = int(input("Enter loan period in years: "))

monthly_rate = annual_rate / (12 * 100)
months = years * 12

emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)

print("Monthly EMI =", emi)
