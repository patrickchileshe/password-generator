import random
import string

def generate_password(length, include_uppercase, include_numbers, include_special_chars):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if include_uppercase else ''
    numbers = string.digits if include_numbers else ''
    special_chars = string.punctuation if include_special_chars else ''
    
    all_chars = lower + upper + numbers + special_chars

    if not all_chars:
        return "Error: At least one character set must be selected!"

    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def password_generator():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Password length must be greater than 0.")
            return

        include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
        include_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
        include_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

        password = generate_password(length, include_uppercase, include_numbers, include_special_chars)
        print(f"\nYour generated password is: {password}")
    except ValueError:
        print("Invalid input. Please enter a numeric value for length.")

if __name__ == "__main__":
    password_generator()
