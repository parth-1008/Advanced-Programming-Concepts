password = input("Enter password: ")

upper = lower = special = False

for ch in password:
    if ch.isupper():
        upper = True
    elif ch.islower():
        lower = True
    elif not ch.isalnum():
        special = True

if len(password) >= 8 and upper and lower and special:
    print("Valid Password")
else:
    print("Invalid Password")