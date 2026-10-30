f = open("data.txt", "r")
lines = f.readlines()

longest = max(lines, key=len)

print("Longest line:", longest)

f.close()