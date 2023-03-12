import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit("Expected 2 arguments got 0")
    num1, num2 = int(sys.argv[1]), int(sys.argv[2])
    print(f"{num1} x {num2} = {num1 * num2}")

