# Uncommon Python Error: ZeroDivisionError

This repository demonstrates a common but sometimes overlooked error in Python: the `ZeroDivisionError`.  The example focuses on an edge case that can easily be missed during initial development and testing.

The `bug.py` file contains a function with a potential `ZeroDivisionError`, which is illustrated and addressed in the `bugSolution.py` file.

## Bug Description:

The `function_with_uncommon_error` function in `bug.py` can lead to a `ZeroDivisionError` if the input `a` is 0. The solution needs to handle this case to avoid the exception.

## Solution:

The solution in `bugSolution.py` adds a check to prevent the division by zero.  This demonstrates robust error handling and avoids runtime exceptions.
