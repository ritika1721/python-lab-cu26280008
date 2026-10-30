f = open("data.txt", "r")
data = f.read()

word = input("Enter word to search: ")

if word in data.split():
    print("Word found")
else:
    print("Word not found")

f.close()