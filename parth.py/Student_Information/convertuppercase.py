try:
    f1 = open("sample.txt", "r")
    f2 = open("uppercase.txt", "w")

    text = f1.read()
    f2.write(text.upper())

    f1.close()
    f2.close()

    print("Text copied in uppercase successfully.")

except FileNotFoundError:
    print("File not found")