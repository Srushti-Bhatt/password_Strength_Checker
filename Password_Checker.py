import re

def check_password_strength(password):
    score = 0
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r'[A-Z]', password)
    lower_criteria = re.search(r'[a-z]', password)
    digit_criteria = re.search(r'\d', password)
    special_criteria = re.search(r'[@$!%*?&#]', password)

    if length_criteria:
        score += 1
    if upper_criteria:
        score += 1
    if lower_criteria:
        score += 1
    if digit_criteria:
        score += 1
    if special_criteria:
        score += 1

    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return strength

# --- Run the checker ---
if __name__ == "__main__":
    user_password = input("Enter your password: ")
    strength = check_password_strength(user_password)
    print(f"Password Strength: {strength}")

