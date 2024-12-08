def function_with_uncommon_error(a, b):
    if a == 0:
        return float('inf') # Or handle it based on your specific requirements
        #raise ZeroDivisionError("Division by zero") #Another option if you want to explicitly raise the error 
    else:
        return a / b