import random
import string

def check_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    score = sum([has_upper, has_lower, has_digit, has_special])

    if length < 6 or score <= 1:
        return "Weak"
    elif length >= 6 and score == 2:
        return "Medium"
    else:
        return "Strong"

def generate_password():
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(10))

while True:
    print("\n1. Check Password Strength")
    print("2. Generate Strong Password")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        pwd = input("Enter password: ")
        strength = check_strength(pwd)
        print(f"Password Strength: {strength}")
    elif choice == "2":
        print("Generated Password:", generate_password())
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")
