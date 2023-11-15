# ChatGPTemail.py
import re

def check_email(email):
    # Define the regular expression pattern for a basic email address
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    # Use the search() function to find a match in the email address
    match = re.search(pattern, email)

    # Check if a match is found
    if match:
        return True
    else:
        return False

# Sample email addresses for testing
sample_emails = [
    'user@example.com',
    'john.doe123@gmail.com',
    'invalid.email@.com',
    'missingatgmail.com',
    '@missingusername.com',
    'user@domainwithspaces .com',
    'user@inva!lidchar.com',
    'user@toolongdomainnamethatisbeyondthelimitofcharacters.com',
    'user@valid-domain.com',
    'user@valid.domain-with-hyphen.com',
]

# Test the sample email addresses
for email in sample_emails:
    result = check_email(email)
    print(f'{email}: {"Valid" if result else "Invalid"}')