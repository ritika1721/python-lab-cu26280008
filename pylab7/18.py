f = open("data.txt", "r")
words = f.read().split()
f.close()

unique = set(words)

f = open("unique.txt", "w")

for word in sorted(unique):
    f.write(word + "\n")

f.close()

print("Unique words saved")