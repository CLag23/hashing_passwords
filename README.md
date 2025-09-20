User authentication system that uses bcrypt for password hashing and MongoDB for user storage.

- Enforcing strong password rules (length + uppercase + lowercase + digit + special character).

- Hashing passwords securely with bcrypt (no plain-text storage).

- Storing and retrieving user credentials in MongoDB.

- Preventing duplicate usernames with a unique index.

- Login verification against the stored hash.
