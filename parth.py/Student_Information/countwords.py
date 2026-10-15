try:
    f = open("sample.txt", "r")
    
    count = 0
    
    for line in f:
        words = line.split()
        count += len(words)
    
    print("Total number of words:", count)
    
    f.close()

except FileNotFoundError:
    print("File not found")

