import random
import string

def generate_password(length):
    """Generate and return a random password of given length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ""
    for i in range(length):
        password += random.choice(characters)
    
    return password


def main():
    print("Password Generator")

    length = int(input("Enter the desired password length: "))

    password = generate_password(length)

    print(f"Generated password: {password}")


# Start the program
main()