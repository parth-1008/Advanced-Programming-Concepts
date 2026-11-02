import re
text = "My phone number is 9699551596"
result = re.search("[0-9]+", text)
if result:
    print("Number found:", result.group())
else:
    print("Number not found")