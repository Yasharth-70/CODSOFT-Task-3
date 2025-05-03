import random
import string

def generate_password(length):
    # Define the characters to use (lowercase letters + digits)
    char_pool = string.ascii_lowercase + string.digits

    # Generate a random password
    password = ''.join(random.choice(char_pool) for _ in range(length))
    
    return password

# Directly call the functions without checking _name_
print("Simple Password Generator")

# Get user input for password length
length = int(input("Enter the desired length of the password: "))

# Generate password
password = generate_password(length)

# Display the generated password
print("\nGenerated Password: ", password)
        