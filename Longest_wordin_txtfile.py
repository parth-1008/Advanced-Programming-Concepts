file = open("student.txt", "r")
data = file.read()
words = data.split()
longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word
print("Longest word:", longest)
file.close()