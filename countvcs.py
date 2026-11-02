string=input("enter a string:")
v=c=d=space=special_symbol=0

for ch in string:
    if ch in "aeiouAEIOU":
        v+=1
    elif ('A'<=ch<='Z') or ('a'<=ch<='z'):
        c+=1
    elif ('0'<=ch<='9'):
        d+=1
    elif ch==' ':
        space+=1
    else:
        special_symbol+=1
        
print("vowels are:",v)
print("consonants:",c)
print("digit:",d)
print("space:",space)
print("special symbol:",special_symbol)