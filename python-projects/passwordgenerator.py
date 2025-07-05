import random 
import string

def getuserdetails():
    """Get user details for password generation."""
    print("Welcome to the Password Generator!")

    length = int(input("Enter the desired length of the password (minimum 8 characters): "))
    use_upper = input("Do you want to include uppercase letters? (y/n): ").lower() == "y"
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    return use_upper, use_digits, use_symbols, length

# Get user preferences
use_upper, use_digits, use_symbols, length = getuserdetails()

# Character sets for password generation
charsets = list(string.ascii_lowercase) # Add lowercase letters.

if use_upper:
    charsets += list(string.ascii_uppercase) # Add uppercase letters.

if use_digits:
    charsets += list(string.digits) # 0 to 9

if use_symbols:
    charsets += list(string.punctuation) # !@#$#$^%

if not charsets:
    print("No character sets selected. Exiting.")
    exit()
# Note:- charsets.extend() is used to add elements to the list, it is not like append() function. Append will add entire thing as a single element. extend() iterates through the given thing and add it to another list.

# join everything!
mainpassword = ''.join(random.choice(charsets) for _ in range(length))
print(f"Generated password: {mainpassword}")

if __name__ == "__main__":
    # This allows the script to be run directly.
    print("Password generation complete.")