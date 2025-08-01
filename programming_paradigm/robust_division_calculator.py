def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator / denominator
        print(f"The result of the division is {result}")
        return
    except(ZeroDivisionError):
        print("Error: Cannot divide by zero.")
        return
    except(ValueError):
        print("Error: Please enter numeric values only.")
        return