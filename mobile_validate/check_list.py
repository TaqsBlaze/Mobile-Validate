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
	#------------------------------------------------
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
	#--------------------------—-------------------------
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

