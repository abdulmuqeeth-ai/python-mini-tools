import random
import string

def generate_password(length=12):
    """Generate strong random password"""
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

print(f"Your password: {generate_password(16)}")
