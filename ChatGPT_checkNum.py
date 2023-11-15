# ChatGPT_checkNum.py
import re

def check_resident_number(resident_number):
    # Define the regular expression pattern for Korea's resident registration number
    pattern = r'^(\d{2})(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])-(1|2)\d{6}$'

    # Use the search() function to find a match in the resident registration number
    match = re.search(pattern, resident_number)

    # Check if a match is found
    if match:
        return True
    else:
        return False

# Sample resident registration numbers for testing
sample_resident_numbers = [
    '920101-1234567',
    '990214-2345678',
    '880312-1122334',
    '760525-2123456',
    '051122-1122334',
    '030512-2123456',
    '201301-1122334',  # Invalid month (13)
    '890232-2123456',  # Invalid day (32)
    '980215-3456789',  # Invalid first digit of the last 7 digits (3)
    '070701-0123456',  # Valid resident number
]

# Test the sample resident registration numbers
for resident_number in sample_resident_numbers:
    result = check_resident_number(resident_number)
    print(f'{resident_number}: {"Valid" if result else "Invalid"}')