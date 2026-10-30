f = open("data.txt", "r")

lines = f.readlines()

for i in range(1, len(lines), 2):
    print(lines[i])

f.close()