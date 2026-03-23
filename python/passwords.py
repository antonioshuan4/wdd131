"""
W02 Project: Password Strength Checker
Author: Gustavo Antonio Shuan Barreto
Description: This program evaluates the strength of a password based on length,
dictionary matches, and character complexity.

Exceeding Requirements:
- Added error handling for missing files.
- Improved loop structure for better readability.
"""

LOWER = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
UPPER = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
DIGITS = ["0","1","2","3","4","5","6","7","8","9"]
SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"]


def word_in_file(word, filename, case_sensitive=False):
    """Checks if a word exists in a given file."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                clean_line = line.strip()
                if case_sensitive:
                    if word == clean_line:
                        return True
                else:
                    if word.lower() == clean_line.lower():
                        return True
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
    return False


def word_has_character(word, character_list):
    """Checks if the word contains any character from the provided list."""
    for char in word:
        if char in character_list:
            return True
    return False


def word_complexity(word):
    """Calculates complexity (0-4) based on types of characters used."""
    complexity = 0

    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1

    return complexity


def password_strength(password, min_length=10, strong_length=16):
    """Calculates password strength (0-5) based on requirements."""

    # 1. Dictionary check (case insensitive)
    if word_in_file(password, "wordlist.txt"):
        print("Password is a dictionary word and is not secure.")
        return 0

    # 2. Top passwords (case sensitive)
    if word_in_file(password, "toppasswords.txt", True):
        print("Password is a commonly used password and is not secure.")
        return 0

    # 3. Too short
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1

    # 4. Strong by length (>15)
    if len(password) > 15:
        print("Password is long, length trumps complexity, this is a good password.")
        return 5

    # 5. Complexity
    complexity_score = word_complexity(password)
    strength = 1 + complexity_score

    return strength


def main():
    """Main input loop."""
    print("--- Password Strength Checker ---")

    while True:
        user_password = input("\nEnter a password to test (or 'q' to quit): ")

        if user_password.lower() == "q":
            break

        strength = password_strength(user_password)
        print(f"Password Strength: {strength}")


# Start program
if __name__ == "__main__":
    main()