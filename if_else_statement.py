# Step 1: Get user input
user_input = input("Enter a number: ")

# Step 2: Convert the input to an integer
try:
    number = int(user_input)

    # Step 3: Check if the number is even or odd
    if number % 2 == 0:
        print(f"The number {number} is Even.")
    else:
        print(f"The number {number} is Odd.")

except ValueError:
    print("Invalid input. Please enter an integer.")
