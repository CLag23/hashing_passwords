# 🔐 Python Password Manager with MongoDB

This project is a simple **Python-based user authentication system** that uses **bcrypt for password hashing** and **MongoDB for user storage**.

demonstrates:
-  Enforcing strong password rules (length + uppercase + lowercase + digit + special character)  
-  Hashing passwords securely with bcrypt (no plain-text storage)  
-  Storing and retrieving user credentials in MongoDB  
-  Preventing duplicate usernames with a unique index  
-  Login verification against the stored hash  

---

## 🚀 Requirements
- Python 3.10+  
- MongoDB (running locally via Docker or installed natively)  
- Dependencies:
  ```bash
   pip install pymongo bcrypt
  ```
---
🐳 Running MongoDB with Docker

Start MongoDB in a Docker container:
  ```bash
  docker run --name hashing -d -p 27017:27017 mongo
  ```
---
▶️ How to Run
- Enter a username and password (must meet password strength requirements).

- The password will be hashed and stored in MongoDB.

- Try logging in with the same credentials to verify authentication.
```txt
Password requirements:
- At least 8 characters long
- Must include: uppercase, lowercase, number, special character (!@#$%^&* etc.)

Enter username: alice
Enter password: StrongPass!123

User 'alice' saved to MongoDB!

Enter your username: alice
Enter your password: StrongPass!123

Login successful!
```
---
🐳 MongoDB Shell

<img width="831" height="136" alt="image" src="https://github.com/user-attachments/assets/945a28b7-12da-4166-8a56-ba52bf7a7f48" />
