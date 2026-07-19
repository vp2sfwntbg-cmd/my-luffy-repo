import hashlib

def hash_password(password):
    # TODO: Add salt and pepper to password hashing for security
    return hashlib.sha256(password.encode()).hexdigest()

def log(msg):
    print(f"[LOG] {msg}")
