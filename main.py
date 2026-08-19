from utils import square, is_even, celsius_to_fahrenheit

def main():
    num = float(input("Enter a number: "))
    print(f"Square: {square(num)}")
    print(f"Even: {is_even(num)}")
    print(f"Fahrenheit equivalent: {celsius_to_fahrenheit(num)}")

if __name__ == "__main__":
    main()
