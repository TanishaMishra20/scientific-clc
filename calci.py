import math  # Using only basic math functions

def scientific_calculator():
    print("\nScientific Calculator")
    print("---------------------")
    print("Operations available:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exponentiation (^)")
    print("6. Square Root (√)")
    print("7. Logarithm (log)")
    print("8. Sine (sin)")
    print("9. Cosine (cos)")
    print("10. Tangent (tan)")
    print("11. Exit")
    
    while True:
        try:
            choice = input("\nEnter operation number (1-11): ")
            
            if choice == '11':
                print("Exiting calculator...")
                break
                
            if choice in ('6', '7', '8', '9', '10'):
                # Single input operations
                num = float(input("Enter number: "))
            else:
                # Two input operations
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            
            if choice == '1':
                print(f"Result: {num1 + num2}")
            elif choice == '2':
                print(f"Result: {num1 - num2}")
            elif choice == '3':
                print(f"Result: {num1 * num2}")
            elif choice == '4':
                if num2 == 0:
                    print("Error: Division by zero!")
                else:
                    print(f"Result: {num1 / num2}")
            elif choice == '5':
                print(f"Result: {num1 ** num2}")
            elif choice == '6':
                if num < 0:
                    print("Error: Square root of negative number!")
                else:
                    # Using Babylonian method without math.sqrt
                    guess = num / 2.0
                    for _ in range(10):
                        guess = (guess + num/guess) / 2.0
                    print(f"Result: {guess}")
            elif choice == '7':
                if num <= 0:
                    print("Error: Logarithm of non-positive number!")
                else:
                    # Simple log approximation
                    result = 0
                    x = (num - 1) / (num + 1)
                    for n in range(1, 100, 2):
                        result += (x ** n) / n
                    result *= 2
                    print(f"Result: {result}")
            elif choice == '8':
                print(f"Result: {math.sin(math.radians(num))}")
            elif choice == '9':
                print(f"Result: {math.cos(math.radians(num))}")
            elif choice == '10':
                print(f"Result: {math.tan(math.radians(num))}")
            else:
                print("Invalid input! Please try again.")
                
        except ValueError:
            print("Invalid input! Please enter numbers only.")

if __name__ == "__main__":
    scientific_calculator()