f = open("demo.txt", "r+")
print(f.read())
f.write("\nit's new line added")
f.close()