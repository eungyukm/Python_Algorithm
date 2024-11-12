try:
    print("test_before")
    open('test.txt')
except ZeroDivisionError:
    print("Divide by zero")

except FileNotFoundError:
    print("File not found")