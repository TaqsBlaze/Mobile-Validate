![Alt text](https://github.com/TaqsBlaze/Mobile-Validate/blob/main/mobile_validate/image/snip2.png)
Easy and Powerful International Phone Number Validation with Country Detection
============================================================================

mobile-validate 📱📠 is a Python package designed to streamline the process of validating international phone numbers and identifying their corresponding countries. It leverages a comprehensive library of country-specific regular expressions to ensure accurate and reliable results.

Key Features 🔑
------------

- Extensive Country Coverage: Supports phone number validation for numerous countries, including popular regions and niche markets.
- Simplified Country Identification: Effortlessly identifies the country of origin associated with any valid phone number.
- Ease of Use: Integrates seamlessly with existing Python applications and features an intuitive API for convenient phone number validation and country detection.
- Highly Accurate: Utilizes a rigorously tested set of country-specific regular expressions to guarantee reliable validation results.

Supported Countries 🗺️
-------------------

The module currently supports phone number validation for a wide range of countries, including:

- Africa: Zimbabwe, South Africa, Mozambique, Botswana, Malawi, Zambia, Ghana, Nigeria, Egypt
- Middle East: Israel
- Europe: United Kingdom (London), Netherlands
- Asia: China, Korea
- North America: United States of America
- South America: Argentina, Brazil
- Oceania: Australia


12/12/23
--------
```18 more countries been added in version v1.2.2```
- consider updating to v1.2.2 ```pip install -U mobile-validate```


Applications 🤔
------------

This package offers a versatile solution for various applications, including:

- Contact Management Systems: Ensure accurate and consistent contact information for international customers and partners.
- User Registration Forms: Simplify user registration by providing seamless phone number validation and country detection.
- SMS Marketing Campaigns: Target specific regions and ensure successful delivery of SMS messages.
- Mobile Payment Systems: Implement secure and reliable mobile payment solutions with accurate phone number validation.
- International Business Transactions: Streamline international business communication and transactions with efficient phone number validation.

Installation 🔌💻
------------

The package can be easily installed using pip:

:: bash

    pip install mobile-validate

Usage 💡
-----

mobile-validate offers an intuitive API for phone number validation and country detection:

:: python

    from mobile_validate.validator import valid_number

    # Example: Valid Zimbabwe Mobile Number
    phone_number = "+263771234567"
    country = "Zimbabwe"

    if valid_number(phone_number, country):
        print(f"Valid {country} mobile number")
    else:
        print(f"Not a valid {country} number")


Checking Carrier provider for a number 📶
--------------------------------------

:: python

    from mobile_validate.validaro import get_provider
   
    phone_number = "+44778392002"
    provider = get_provider(phone_number)
    print(provider)


Country lookup using mobile number
----------------------------------

::

    from mobile_validate.validator import get_country

    number = +2771700917

    country = get_country(number)

    print(f"Mobile number {number} is from {country}")


Note 📄
----

This package is under active development, and contributions are always welcome.👍


Sponsor Mobile-Validate 💰
------------------------
- You can support me on this journey by sponsoring via these playforms
- Any Trc10/Trc20 token: <div style="background:lightred;border-radius:8pc">TBueWQVP14pHX8n5QBHpmk1YD2WAWc27RE</div>
- Airtm: <div style="background:lightblue;border-radius:8pc;">tanakah30@gmail.com</div>

- Please consider sponsoring as this will highly motivate me to keep adding more cool features 
