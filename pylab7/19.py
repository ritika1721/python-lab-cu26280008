f = open("data.txt", "r")
words = f.read().split()
f.close()

words.sort()

f = open("sorted.txt", "w")

for word in words:
    f.write(word + "\n")

f.close()

print("Words sorted successfully")