# ===================================================================================
# Created By     : x_4rch4n63l_x
# Created On     : 12/31/2024 - 3:42AM
# Script Purpose : PSN Code Validator coded in Python
# Description    : This script allows users to:
#                  1. Validate PSN codes based on their format.
#                  2. Ensure codes contain a mix of letters and digits.
#                  3. Add a simple login mechanism for security.
# 
# Features       : 
#                  - Simple login mechanism for security.
#                  - Clear console screen post-login for a clean interface.
#                  - User-friendly interaction to input PSN codes and validate them.
#
# Usage Note     : This script does not verify PSN codes against Sony's backend and should be
#                  used responsibly and ethically. Ensure compliance with relevant policies.
# ===================================================================================

import re
import getpass
import os

USER = "root"
PASSWORD = "root"

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else: 
        os.system('clear')

def login():
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    return username == USER and password == PASSWORD

def is_valid_psn_code(code):
    pattern = re.compile(r'^[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}$')
    
    if not pattern.match(code):
        return False

    has_letter = any(c.isalpha() for c in code)
    has_digit = any(c.isdigit() for c in code)

    parts = code.split('-')
    if len(parts) != 3:
        return False

    for part in parts:
        if len(part) != 4:
            return False
        if not any(char.isdigit() for char in part) or not any(char.isalpha() for char in part):
            return False

    return has_letter and has_digit

def main():
    clear_screen()
    print("PSN Code Validator Login")
    
    if not login():
        print("Invalid credentials. Access denied.")
        return

    clear_screen()
    print("Welcome to the PSN Code Validator")
    
    while True:
        code = input("Enter PSN code to validate (or type 'exit' to quit): ")
        
        if code.lower() == 'exit':
            break

        if is_valid_psn_code(code):
            print("Code is valid!")
        else:
            print("Code is invalid.")

if __name__ == "__main__":
    main()
