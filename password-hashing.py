import re # regex checks patterns
import bcrypt

def get_user_info():
    print("Password requirements:")
    print("- At least 8 characters long")
    print("- Must include: uppercase, lowercase, number, special character (!@#$%^&* etc.)\n")
    while True:
        try:
            username = input("Enter username: ").strip()
            password = input("Enter password: " ).strip()

            if not username:
                raise ValueError("Username cannot be empty.")
            
            if len(password) < 8: 
                raise ValueError("Password must be at least 8 characters long.")
            if not re.search(r"[A-Z]", password):
                raise ValueError("Password must contain at least one uppercase letter.")
            if not re.search(r"[a-z]", password):
                raise ValueError("Password must contain at least one lowercse letter.")
            if not re.search(r"[0-9]", password):
                raise ValueError("Password must contain at least one digit.")
            if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
                raise ValueError("Pssword must contain at least one special charcter")
            
            return username, password
        except ValueError as e:
            print(f"Error: {e}. Please try again.")


