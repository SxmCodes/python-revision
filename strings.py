# a = '''Saksa
# am
# Shar
# ma'''
# print(a[-1]) #last character.
# print(a.replace('a', 'A'))
 
# String slicing.

# name = "saksham1029"

# print(name[0:10:2]) #Saksha -> This will skip n-1 (1) character. 
# print(name[:4]) # Replace first number with 0.
# print(name[1:]) # Replace last number with length.

# print(name.upper()) # Convert to upper case.
# print(name.lower()) # Convert to lower case.
# print(name.title()) # Convert to title case.
# print(name.capitalize()) # Convert to capital case.
# print(name.isupper()) # Check if string is in upper case.
# print(name.islower()) # Check if string is in lower case.
# print(name.isalpha()) # Check if string contains only alphabets.
# print(name.isalnum()) # Check if string contains only alphanumeric characters.
# print(name.isdigit()) # Check if string contains only digits.
# print(name.isnumeric()) # Check if string contains only numeric characters.
# print(name.isidentifier()) # Check if string is a valid identifier.
# print(name.startswith("Sak")) # Check if string starts with "Sak".
# print(name.endswith("29")) # Check if string ends with "29".
# print(name.find("sh")) # Find the index of "sh" in the string.
# print(name.index("sh")) # Find the index of "sh" in the string (raises ValueError if not found).
# print(name.count("a")) # Count the number of occurrences of "a" in the string.
# print(name.replace("Sak", "Sam")) # Replace "Sak" with "Sam" in the string.
# print(name.split("k")) # Split the string by "k".
# print(name.split()) # Split the string by whitespace.


new = "Apple, Banana, Cherry, Date"
print(new)
print(new.split(", "))  # Split the string by ", " and return a list of substrings.
# print(new.split("a"))  # Split the string by "a"
print(",".join(new.split(", "))) # WhiteSpace will not be included.

# Strings formatting and f-strings. 
name = "Yoo! You are osm!"
a1 = "Richard"
print(name.format()) 
print(f"{a1} will go to the moon!")
print(f"{name} {a1} will go to the moon!") 
