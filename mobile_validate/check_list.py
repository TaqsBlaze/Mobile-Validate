'''
============================================================================

READ ME PLEASE!

IF YOU WANT TO ADD MORE COUNTRIES REGEX MAKE SURE TO FOLLOW SET STANDARD
AND STRUCTOR

COUNTRY NAME ALWAYS STARTS WITH CAPITALS
REGEX EXPRESSION FORMAT MUST BE CONSISTANT
============================================================================
'''

phone_regex = {
    "Zimbabwe": {
        r"\+263(?:\s?)?\d{9}$",  # Mobile
        r"\+263(?:\s?)\d{8}",  # Fixed-line
    },
    "South Africa": {
        r"\+27(?:\s?)\d{9}",  # Mobile
        r"\+27(?:\s?)\d{8}",  # Fixed-line
    },
    "Mozambique": {
        r"\+258(?:\s?)\d{9}",  # Mobile
    },
    "Botswana": r"\+267(?:\s?)\d{8}",  # Mobile
    "Malawi": r"\+265(?:\s?)\d{9}",  # Mobile
    "Zambia": r"\+260(?:\s?)\d{9}",  # Mobile
    "Ghana": r"\+233(?:\s?)\d{9}",  # Mobile
    "Nigeria": {
        r"\+234(?:\s?)\d{11}",  # Mobile
        r"\+234(?:\s?)\d{10}",  # Fixed-line
    },
    "Egypt": {
        r"\+20(?:\s?)\d{10}",  # Mobile
        r"\+20(?:\s?)\d{9}",  # Fixed-line
    },
    "Israeli": r"\+972(?:\s?)\d{9}",  # Mobile
    "United Kingdom London": r"\+44(?:\s?)\d{10}",  # Mobile
    "China": r"\+86(?:\s?)\d{11}",  # Mobile
    "Korea": r"\+82(?:\s?)\d{10,11}",  # Mobile
    "Russia": r"\+7(?:\s?)\d{10}",  # Mobile
    "United States of America": r"\+\d{1}\s?\d{3}-\d{3}-\d{4}",  # Mobile
    "Argentina": r"\+54(?:\s?)\d{13}",  # Mobile
    "Brazil": r"\+55(?:\s?)\d{11}",  # Mobile
    "Australia": r"\+61(?:\s?)\d{9}",  # Mobile
    "Netherlands": r"\+31(?:\s?)\d{9}",  # Mobile
}
