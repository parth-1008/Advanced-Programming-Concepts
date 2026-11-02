file = open("student.txt", "r")
data = file.read()
a = 0
d = 0
s = 0
sp = 0
for ch in data:
    if ch.isalpha():
        a = a + 1
    elif ch.isdigit():
        d = d + 1
    elif ch == " ":
        s = s + 1
    else:
        sp = sp + 1
print("Alphabets:", a)
print("Digits:", d)
print("Spaces:", s)
print("Special Characters:", sp)

file.close()