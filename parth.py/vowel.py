letter = input("Enter one letter: ").strip().lower()

if len(letter) == 1 and letter.isalpha():
    if letter in "aeiou":
        print("It is a vowel.")
    else:
        print("It is not a vowel,it is a consonant")
else:
    print("Please enter exactly one letter.")