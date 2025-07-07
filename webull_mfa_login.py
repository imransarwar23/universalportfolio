from webull import webull
import json
import os
from dotenv import load_dotenv

# Load credentials from .env
load_dotenv(dotenv_path="confidential.env")
email = os.getenv("WEBULL_EMAIL")
password = os.getenv("WEBULL_PASSWORD")

# Safety check
if not email or not password:
    raise ValueError("Email or password not loaded from confidential.env")

# Create Webull instance
wb = webull()

# Step 1: Request MFA and security question
wb.get_mfa(email)
sec_questions = wb.get_security(email)

# Check response before continuing
if not sec_questions or "questionId" not in sec_questions[0]:
    raise RuntimeError("Failed to get security questions. Check response or try again later.")

print("Security Question:", sec_questions[0]["questionName"])

# Optional: Test raw request (already handled above)
# You don't need this unless debugging:
response = wb._session.post(
     'https://userapi.webull.com/api/passport/val/secureVerify/do/getSecurityQuestion',
     json={"account": email, "accountType": 2}
 )
print("Status Code:", response.status_code)
print("Raw Response Text:", response.text)

# Step 2: Manual input
mfa_code = input("Enter 6-digit MFA code (from SMS/email): ")
question_id = sec_questions[0]["questionId"]
question_answer = input("Enter answer to security question: ")
device_name = "MyScript"

# Step 3: Full login
login_response = wb.login(
    email,
    password,
    device_name,
    mfa_code,
    question_id,
    question_answer
)

# Check if login succeeded
if login_response.get("success") is False:
    raise RuntimeError(f"Login failed: {login_response.get('msg', 'Unknown error')}")

print("\n✅ Login Success\n")

# Step 4: Save tokens
tokens = {
    "access_token": wb.get_access_token(),
    "refresh_token": wb.get_refresh_token(),
    "token_expiry": str(wb.token_exp),
}

with open("tokens.json", "w") as f:
    json.dump(tokens, f, indent=2)

print("✅ Saved tokens to tokens.json")
