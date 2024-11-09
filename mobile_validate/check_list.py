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
    "Algeria": {
        r"\+213\d{9}",  # Mobile
        r"\+213\d{8}",  # Fixed-line
    },
    "Angola": {
        r"\+244\d{9}",  # Mobile
        r"\+244\d{7}",  # Fixed-line
    },
    "Benin": {
        r"\+229\d{8}",  # Mobile
        r"\+229\d{7}",  # Fixed-line
    },
    "Burkina Faso": {
        r"\+226\d{8}",  # Mobile
        r"\+226\d{6}",  # Fixed-line
    },
    "Cameroon": {
        r"\+237\d{8}",  # Mobile
        r"\+237\d{7}",  # Fixed-line
    },
    "India": {
        r"\+91\d{10}",  # Mobile
        r"\+91(?:11|22|33|44|80)\d{7}",  # Fixed-line
    },
    "Indonesia": {
        r"\+62\d{10,11}",  # Mobile
        r"\+62\d{8,9}",  # Fixed-line
    },
    "Japan": {
        r"\+81\d{10,11}",  # Mobile
        r"\+81(?:3|570|60|80)\d{7}",  # Fixed-line
    },
    "Kazakhstan": {
        r"\+7\d{10}",  # Mobile
        r"\+7(?:7|70|71|72|73|74|75|76|77|78|79)\d{7}",  # Fixed-line
    },
    "Malaysia": {
        r"\+60\d{10,11}",  # Mobile
        r"\+60(?:3|4|5|6|7|8|9)\d{7}",  # Fixed-line
    },
    "Canada": {
        r"\+\d{1}\s?\d{3}-\d{3}-\d{4}",  # Mobile, similar to USA format
        r"\+\d{1}\s?\d{3}-\d{4}",  # Old format
    },
    "Colombia": {
        r"\+57\d{10}",  # Mobile
        r"\+57(?:1|2|3|4|5|6|7)\d{7}",  # Fixed-line
    },
    "Mexico": {
        r"\+52\d{10}",  # Mobile
        r"\+52(?:22|33|55|81)\d{7}",  # Fixed-line
    },
    "Peru": {
        r"\+51\d{9}",  # Mobile
        r"\+51(?:1|4|5|6|7)\d{6}",  # Fixed-line
    },
    "France": {
        r"\+33\d{9}",  # Mobile
        r"\+33\d{10}",  # Fixed-line
    },
    "Germany": {
        r"\+49\d{11}",  # Mobile
        r"\+49\d{9,10}",  # Fixed-line
    },
    "Italy": {
        r"\+39\d{10}",  # Mobile
        r"\+39\d{11}",  # Fixed-line
    },
    "Poland": {
        r"\+48\d{9}",  # Mobile
        r"\+48\d{8}",  # Fixed-line
    },
    "Spain": {
        r"\+34\d{9}",  # Mobile
        r"\+34\d{8,9}",  # Fixed-line
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

    # Added Countries
    "United States (USA)": {
        r"\+1(?:\s?)\d{10}",  # Mobile
        r"\+1(?:\s?)\d{3}-\d{3}-\d{4}",  # Mobile (with dashes, similar format)
    },
    "United Kingdom (UK)": {
        r"\+44(?:\s?)\d{10}",  # Mobile
        r"\+44(?:\s?)\d{3}\s?\d{7}",  # Fixed-line
    },
    "France": {
        r"\+33\d{9}",  # Mobile
        r"\+33\d{9}",  # Fixed-line
    },
    "Turkey": {
        r"\+90\d{10}",  # Mobile
        r"\+90\d{10}",  # Fixed-line
    },
    "Belgium": {
        r"\+32\d{8}",  # Mobile
        r"\+32\d{8}",  # Fixed-line
    },
    "Sweden": {
        r"\+46\d{9}",  # Mobile
        r"\+46\d{9}",  # Fixed-line
    },
    "Switzerland": {
        r"\+41\d{9}",  # Mobile
        r"\+41\d{9}",  # Fixed-line
    },
    "Austria": {
        r"\+43\d{10}",  # Mobile
        r"\+43\d{10}",  # Fixed-line
    },
    "New Zealand": {
        r"\+64\d{9}",  # Mobile
        r"\+64\d{9}",  # Fixed-line
    },
    "Denmark": {
        r"\+45\d{8}",  # Mobile
        r"\+45\d{8}",  # Fixed-line
    },
    "Norway": {
        r"\+47\d{8}",  # Mobile
        r"\+47\d{8}",  # Fixed-line
    },
    "Finland": {
        r"\+358\d{9}",  # Mobile
        r"\+358\d{9}",  # Fixed-line
    },
    "Iceland": {
        r"\+354\d{7}",  # Mobile
        r"\+354\d{7}",  # Fixed-line
    },
    "Portugal": {
        r"\+351\d{9}",  # Mobile
        r"\+351\d{9}",  # Fixed-line
    },
    "Greece": {
        r"\+30\d{10}",  # Mobile
        r"\+30\d{10}",  # Fixed-line
    },
    "South Korea": {
        r"\+82\d{10,11}",  # Mobile
        r"\+82\d{10}",  # Fixed-line
    },
    "Thailand": {
        r"\+66\d{9}",  # Mobile
        r"\+66\d{8,9}",  # Fixed-line
    },
    "Vietnam": {
        r"\+84\d{9}",  # Mobile
        r"\+84\d{8}",  # Fixed-line
    },
    "Philippines": {
        r"\+63\d{10}",  # Mobile
        r"\+63\d{9}",  # Fixed-line
    },
    "Chile": {
        r"\+56\d{9}",  # Mobile
        r"\+56\d{8}",  # Fixed-line
    },
	 "Afghanistan": {
        r"\+93\d{9}",  # Mobile
        # Add landline format if known (same structure as mobile):
        r"\+93\d{9}", 
    },
    "Bangladesh": {
        r"\+880\d{9}",  # Mobile
        # Landline format:
        r"\+880\d{8}", 
    },
    "Sri Lanka": {
        r"\+94\d{9}",  # Mobile
        # Landline format:
        r"\+94\d{8}", 
    },
    "Pakistan": {
        r"\+92\d{10}",  # Mobile
        # Landline format:
        r"\+92\d{8}", 
    },
    "Kuwait": {
        r"\+965\d{8}",  # Mobile
        # Landline format:
        r"\+965\d{8}", 
    },
    "Qatar": {
        r"\+974\d{8}",  # Mobile
        # Landline format:
        r"\+974\d{8}", 
    },
    "Bahrain": {
        r"\+973\d{8}",  # Mobile
        # Landline format:
        r"\+973\d{8}", 
    },
    "UAE": {
        r"\+971\d{9}",  # Mobile
        # Landline format:
        r"\+971\d{7}", 
    },
    "Saudi Arabia": {
        r"\+966\d{9}",  # Mobile
        # Landline format:
        r"\+966\d{7}", 
    },
    "Oman": {
        r"\+968\d{8}",  # Mobile
        # Landline format:
        r"\+968\d{8}", 
    },
    "Jordan": {
        r"\+962\d{9}",  # Mobile
        # Landline format:
        r"\+962\d{7}", 
    },
    "Lebanon": {
        r"\+961\d{9}",  # Mobile
        # Landline format:
        r"\+961\d{7}", 
    },
    "Cyprus": {
        r"\+357\d{8}",  # Mobile
        # Landline format:
        r"\+357\d{8}", 
    },
    "Malta": {
        r"\+356\d{8}",  # Mobile
        # Landline format:
        r"\+356\d{8}",  # Fixed-line (example, placeholder)
    },
    "Armenia": {
        r"\+374\d{8}",  # Mobile
        # Landline format:
        r"\+374\d{8}", 
    },
    "Georgia": {
        r"\+995\d{9}",  # Mobile
        # Landline format:
        r"\+995\d{8}", 
    },
    "Mongolia": {
        r"\+976\d{8}",  # Mobile
        # Landline format:
        r"\+976\d{8}", 
    },
    "Uzbekistan": {
        r"\+998\d{9}",  # Mobile
        # Landline format:
        r"\+998\d{9}", 
    },
    "Tanzania": {
        r"\+255\d{9}",  # Mobile
        # Landline format:
        r"\+255\d{9}", 
    },
    "Kenya": {
        r"\+254\d{9}",  # Mobile
        # Landline format:
        r"\+254\d{9}", 
    },
    "Uganda": {
        r"\+256\d{9}",  # Mobile
        # Landline format:
        r"\+256\d{9}", 
    },
    "Ethiopia": {
        r"\+251\d{9}",  # Mobile
        # Landline format:
        r"\+251\d{9}", 
    },
}


