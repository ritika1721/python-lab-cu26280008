f = open("data.txt", "r")
data = f.read()

numbers = data.split()

total = 0

for n in numbers:
    total = total + int(n)

avg = total / len(numbers)

print("Sum:", total)
print("Average:", avg)

f.close()