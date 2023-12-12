import re
import phonenumbers
from mobile_validate.check_list import phone_regex
from phonenumbers.carrier import name_for_number


def valid_number(number, country):

	 try:
	    regex = phone_regex.get(country)
	    if isinstance(regex, set): #This checks is country has mobile and fixed line formats:'#	'
	      for pattern in regex:
	        if re.match(pattern, number):
	          return True
	    else:
	      if re.match(regex, number):
	        return True
	 except KeyError:
	    # Country not found in the regex list
	    return False
	
def get_country(phone_number):
	
	for country in phone_regex:
		if isinstance(phone_regex.get(country), set):
			for pattern in phone_regex.get(country):
				if re.match(pattern, phone_number):
					return country

		else:
			
			if re.match(phone_regex.get(country), phone_number):
				return country


def get_provider(number):

	ro_num = phonenumbers.parse(number, "RO")
	provider = str(name_for_number(ro_num, "en"))


	return provider



def is_number_active(number):

	#This function will be for checking if a number is active
	#Will utilize cloud APIs for verificatiin calls

	print("This is a future function which is currently under development")

	pass



class Example: 

	
	def show():
			
		eg = """
			 from mobile_validate.validator import valid_mobile

		    # Example: Valid Zimbabwe Mobile Number
		    phone_number = "+263771234567"
		    country = "Zimbabwe"
		
		    if valid_mobile(phone_number, country):
		        print(f"Valid {country} mobile number")
		    else:
		        print(f"Not a valid {country} mobile number")
		        
		        """
		print(eg)
		
		
