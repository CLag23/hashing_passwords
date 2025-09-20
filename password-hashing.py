import re 
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
                raise ValueError("Password must contain at least one lowercase letter.")
            if not re.search(r"[0-9]", password):
                raise ValueError("Password must contain at least one digit.")
            if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
                raise ValueError("Password must contain at least one special character")
            
            return username, password
        except ValueError as e:
            print(f"Error: {e}. Please try again.")


def hash_password(password):

    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed 

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode("utf-8"), hashed)

def login(hashed):
    password = input("\nEnter password to login: ").strip()
    if check_password(password, hashed):
        print("\nLogin Sucessful!")
    else:
        print("\nLogin Failed!")


if __name__ == "__main__":
    username, password = get_user_info()
    hashed_password = hash_password(password)
    login_attempt = login(hashed_password)

    print(f"\nUsername: {username}")
    print(f"hashed password: {hashed_password.decode('utf-8')}")
