try:
    number_JBGP = int(input("Enter a number: "))
    result_JBGP = 100 / number_JBGP
    print("Result:", result_JBGP)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
