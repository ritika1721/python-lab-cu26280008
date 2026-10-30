f = open("data.txt", "r")
data = f.read()

print("Lines:", len(data.splitlines()))
print("Characters:", len(data))

f.close()