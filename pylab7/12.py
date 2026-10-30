f = open("data.txt", "r")
data = f.read()

word = input("Enter word: ")

count = data.split().count(word)

print("Occurrence:", count)

f.close()