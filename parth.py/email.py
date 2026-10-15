import re

def validate_email(email):
    pattern = r'^[A-Za-z0-9._-]+@[A-Za-z0-9]+\.[A-Za-z]{2,6}$'

    if re.match(pattern, email):
        print("Valid email address")
    else:
        print("Invalid email address")


email = input("Enter your email: ")
validate_email(email)