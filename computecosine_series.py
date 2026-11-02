#cos(x) = 1 - x²/2! + x⁴/4! - x⁶/6! + ...
import math

x = float(input("Enter x: "))
n = int(input("Enter n: "))

sum = 0

for i in range(n):
    term = (x ** (2 * i)) / math.factorial(2 * i)

    if i % 2 == 0:
        sum = sum + term
    else:
        sum = sum - term

print("Cos(x) =", sum)