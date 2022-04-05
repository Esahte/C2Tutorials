# Function that adds the individual digits in a given number

def sumDigits(n):
    # Base case
    if n == 0:
        return 0
    # Adds the last digit in the number to the previous digit
    return n % 10 + sumDigits(n // 10)


# Test Code
n = 502
result = sumDigits(n)
print("Sum of digits in ", n, " is: ", result)





