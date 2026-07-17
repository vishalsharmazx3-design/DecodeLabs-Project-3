import random
import string

def generate_password(length):
    # Combine all letters (upper + lower) and digits into one pool
    characters = string.ascii_letters + string.digits
    
    # Randomly pick 'length' characters from the pool
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Ask the user how long they want their password
length = int(input("Enter password length: "))

password = generate_password(length)
print("Your generated password is:", password)