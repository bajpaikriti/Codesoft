#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import string

def generate_password(length=12, complexity="medium"):
    characters = ""

    if complexity == "low":
        characters = string.ascii_letters + string.digits
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "high":
        characters = string.ascii_letters + string.digits + string.punctuation + string.whitespace

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        password_length = int(input("Enter the desired password length: "))
        if password_length < 8:
            print("Password length should be at least 8 characters for security.")
        else:
            complexity = input("Choose complexity (low/medium/high): ").lower()
            if complexity not in ["low", "medium", "high"]:
                print("Invalid complexity level. Using 'medium' complexity.")
                complexity = "medium"

            password = generate_password(password_length, complexity)
            print("Generated password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid number for password length.")

if __name__ == "__main__":
    main()


# In[ ]:




