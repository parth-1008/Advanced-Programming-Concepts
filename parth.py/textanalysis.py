text = input("Enter text: ")

words = text.lower().split()

print("Total words:", len(words))

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Frequency:", frequency)

print("Top 3 words:", sorted(frequency, key=frequency.get, reverse=True)[:3])

vowels = 0
for ch in text.lower():
    if ch in "aeiou":
        vowels += 1

print("Vowels:", vowels)