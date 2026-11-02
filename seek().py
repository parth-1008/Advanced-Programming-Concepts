with open("demo2.txt", "r") as f:
    print(f.read(7))
    f.seek(0)
    print(f.read(7))