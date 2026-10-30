f = open("data.txt", "r")
data = f.read()
f.close()

data = data.replace("Python", "Java")

f = open("data.txt", "w")
f.write(data)
f.close()

print("Word replaced successfully")