p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

ci = p * (1 + r/100) ** t - p

print("Compound Interest =", ci)
