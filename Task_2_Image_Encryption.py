
TODAY
Messages are end-to-end encrypted. No one outside of this chat, not even WhatsApp, can read or listen to them. Click to learn more
TUESDAY
bsnl-teevra-v2.5.2.apk
APK•16 MB
2:50 pm
TODAY
import re

def assess_password_strength(password):
    # Initialize strength levels
    strength = 0
    feedback = []

    # Criteria for evaluation
    length_criteria = len(password) >= 8
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[\W_]', password))

    # Check each criterion
    if length_criteria:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if lowercase_criteria:
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    if uppercase_criteria:
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    if number_criteria:
        strength += 1
    else:
        feedback.append("Password should contain at least one number.")

    if special_char_criteria:
        strength += 1
    else:
        feedback.append("Password should contain at least one special character (e.g., @, #, $, etc.).")

    # Provide strength feedback
    if strength == 5:
        feedback_message = "Strong password!"
    elif strength >= 3:
        feedback_message = "Moderate password. Consider improving it."
    else:
        feedback_message = "Weak password. You need to improve it."

    return {"strength": strength, "feedback": feedback, "overall_message": feedback_message}

# Example usage
password = "P@ssw0rd"
result = assess_password_strength(password)
print(result['overall_message'])
for f in result['feedback']:
    print(f)
11:16 pm


