import random
import string

def generate_email(first_name, last_name, cohort, domain="yandex.ru"):
    digits = ''.join(random.choices(string.digits, k=3))
    email = f"{first_name}{last_name}{cohort}{digits}@{domain}"
    return email

def generate_password(length=10):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choices(chars, k=length))