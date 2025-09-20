import re 
import bcrypt
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
DB_NAME = "user_db"
COLLECTION_NAME = "users"
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
            print(f"Error: {e}. Please try again.\n")


def hash_password(password):

    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed 

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode("utf-8"), hashed)

def login(users_collection):
    username = input("\nEnter your username: ").strip()
    password = input("Enter your password: ").strip()

    user = users_collection.find_one({"username": username})
    if not user:
        print("Username not found.")
        return
    
    stored_hashed = user["hashed_password"].encode("utf-8")
    if check_password(password, stored_hashed):
        print("\nLogin successful!")
    else:
        print("\nLogin Failed")
    


if __name__ == "__main__":
    try:
        client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=5000)
        client.server_info()
    except Exception as e:
        print(print(f"Error: could not connect to MongoDB. {e}"))
        exit()

    db = client[DB_NAME]
    users = db[COLLECTION_NAME]

    users.create_index("username", unique=True)

    username, password = get_user_info()
    hashed_password = hash_password(password)
        
    try:
        users.insert_one({
            "username": username,
            "hashed_password": hashed_password.decode("utf-8")
        })
        print(f"\n User '{username}' saved to MongoDB!")
    except DuplicateKeyError:
        print(f"Error: Username '{username}' already exists. Please choose a different one.")
        exit()

    login(users)
    
