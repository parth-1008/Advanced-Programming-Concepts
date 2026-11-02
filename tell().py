with open("demo2.txt", "r") as f:
    print(f.tell())
    print(f.read(10))
    print(f.tell())