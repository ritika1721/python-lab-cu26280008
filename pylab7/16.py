f = open("data.txt", "r")
lines = f.readlines()

print("First line:", lines[0])
print("Last line:", lines[-1])

f.close()