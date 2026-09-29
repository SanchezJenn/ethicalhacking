# 1. Temperature converter
def celsius_to_fahrenheit(c):
    try:
        return (float(c) * 9/5) + 32
    except ValueError:
        return "Invalid input"

# 2. Safe list access
def get_item(lst, index):
    try:
        return lst[index]
    except IndexError:
        return None

# 3. Validated age input
def get_valid_age():
    while True:
        try:
            age = int(input("Enter age: "))
            if 0 <= age <= 120:
                return age
        except ValueError:
            pass

# 4. Mini utils module (utils.py)
def is_valid_email(email):
    return "@" in email
# main.py
# from utils import is_valid_email
# print(is_valid_email("test@example.com"))

# 5. Custom exception
class InvalidGradeError(Exception):
    pass

def set_grade(grade):
    if not (0 <= grade <= 10):
        raise InvalidGradeError("Grade must be between 0 and 10")
    return grade