str=input("enter a string:")
upper=lower=0
for ch in str:
    if ('A'<=ch<='Z'):
        upper+=1
    elif ('a'<=ch<='z'):
        lower+=1
print("upper:",upper)
print("lower:",lower)