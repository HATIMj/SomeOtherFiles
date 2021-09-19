z=input()
try:print(a)
except Exception as e:
    if z.isdigit():
        raise ValueError("You can't enter this value")
    print("Exception Handled")
