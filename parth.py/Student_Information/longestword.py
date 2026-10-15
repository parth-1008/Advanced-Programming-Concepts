try:
    f = open("sample.txt", "r")

    words = f.read().split()
    longest_word = max(words, key=len)

    print("Longest word:", longest_word)
    print("Length:", len(longest_word))

    f.close()

except FileNotFoundError:
    print("File not found")