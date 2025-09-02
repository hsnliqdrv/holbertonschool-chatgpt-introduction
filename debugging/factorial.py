#!/usr/bin/python
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1   # decrease n
    return result

if __name__ == "__main__":
    f = factorial(int(sys.argv[1]))
    print(f)
