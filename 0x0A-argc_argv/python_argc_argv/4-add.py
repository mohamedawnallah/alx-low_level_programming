import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"Expected 2 got {len(sys.argv) - 1}")
        sys.exit(1)
    try:
        num1, num2 = int(sys.argv[1]), int(sys.argv[2])
        if num1 <= 0 or num2 <= 0:
            print("Please Enter positive numbers greater than 0")
            sys.exit(1)
    except ValueError as value_error:
        print(value_error)
        sys.exit(1)
    print(f"{num1} + {num2} = {num1 + num2}")
