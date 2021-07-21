def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
        return
    return dividend/divisor

grades = []

print("Welcome to the average grade program.")
try:
    average = divide(sum(grades),len(grades))

except ZeroDivisionError as e:
    print("There are no grades yet in your list")
else:
    print(f"The average grade is {average}.")
finally:
    print("Thank you!")

def calculate(*values, operator):
    return operator(*values)

result = calculate(20, 4, operator = divide)
print(result)
