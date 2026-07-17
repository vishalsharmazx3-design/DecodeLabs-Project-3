# Random Password Generator

A simple Python command-line tool that generates a random password of a user-specified length using letters and numbers.

Built as Project 3 of the DecodeLabs Industrial Training Kit (Python Programming track) — focused on library integration (`random`/`secrets` and `string` modules) and string manipulation.

## Features

- Prompts the user for a desired password length
- Generates a random password using uppercase letters, lowercase letters, and digits
- Uses Python's built-in `string` module for clean character set definitions
- Uses `''.join()` for efficient string building (avoids slow repeated concatenation)

## Requirements

- Python 3.6+ (no external libraries needed)

## Usage

1. Save the script as `password_generator.py`
2. Run it from your terminal:
   ```bash
   python password_generator.py
   ```
3. Enter the desired password length when prompted:
   ```
   Enter password length: 12
   Your generated password is: aB3xT9pQ1zLk
   ```

## How It Works

1. **Input** – The program asks the user for the number of characters they want in their password.
2. **Process** – It builds a character pool from `string.ascii_letters` (a–z, A–Z) and `string.digits` (0–9), then randomly selects characters from that pool one at a time.
3. **Output** – The selected characters are joined into a single string and printed as the final password.

## Code

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Enter password length: "))
password = generate_password(length)
print("Your generated password is:", password)
```

## Possible Extensions

- Add symbols (`@`, `#`, `$`, etc.) to the character pool for extra complexity
- Guarantee at least one digit and one symbol appear in every password
- Add input validation (reject negative numbers or non-numeric input)
- Swap `random.choice()` for `secrets.choice()` if the password will be used for real accounts — `secrets` draws from a cryptographically secure source, whereas `random` is predictable and not meant for security purposes

## Learning Goals

- Importing and using Python's standard library modules (`random`, `string`, `secrets`)
- String immutability and efficient string building with `.join()`
- Understanding why length matters more than complexity for password strength (per current NIST guidelines)

## License

Free to use for learning and educational purposes.
