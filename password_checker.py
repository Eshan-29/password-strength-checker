COMMON_PASSWORDS = [
    "password",
    "password123",
    "12345678",
    "qwerty123",
    "letmein",
    "admin123",
    "welcome123"
]
def check_password(password):
    feedback = []




    is_common = password.lower() in COMMON_PASSWORDS
    has_repeated_char = any(password.count(char) >=5 for char in set (password))
    if is_common:
        
        feedback.append("Warning: this is a commonly used password.")
    if has_repeated_char:
        feedback.append("Warning: A character is repeated 5 or more times!")
        

    score = 0
    if len(password) >=12:
        score = score + 1
    else:
        feedback.append("Your password should be at least 12 characters long.")
    if any(char.islower() for char in password):
        score = score + 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if any(char.isupper() for char in password):
        score = score + 1
    else:feedback.append("Add at least one uppercase letter.")

    if any (char.isdigit() for char in password):
        score = score + 1
    else:
        feedback.append("Add at least one digit.")

    if any(not char.isalnum() for char in password ):
        score = score +1
    else:
        feedback.append("Consider adding a special character.")

   


    if is_common:
        rating = "Low"
    elif score <= 1:
        rating = "Low"
    elif score <= 3:
        rating = "Medium"
    else:
        rating = "High"

    return score, rating, feedback

def main():
    print("Password Strength Checker")
    print("-------------------------")
    print("Welcome! Let's check your password.")

    password = input("Enter a password to check: ")

    if password == "":
        print("Error: You must enter a password.")
        return

    score, rating, feedback = check_password(password)

    for warning in feedback:
        print(warning)

    print("Your password score is:", score, "out of 5")
    print("Password variety:", rating)

if __name__ == "__main__":
    main()