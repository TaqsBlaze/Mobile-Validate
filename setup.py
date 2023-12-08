#!/usr/bin/env python
from setuptools import setup

setup(
    name="mobile_validate",
    version="1.0.0",
    author="Tanaka Chinengundu",
    author_email="tanakah30@gmail.com",
    description="""

Easy and Powerful International Phone Number Validation with Country Detection
============================================================================

easy-phone-numbers is a Python package designed to streamline the process of validating international phone numbers and identifying their corresponding countries. It leverages a comprehensive library of country-specific regular expressions to ensure accurate and reliable results.

Key Features
------------

- Extensive Country Coverage: Supports phone number validation for numerous countries, including popular regions and niche markets.
- Simplified Country Identification: Effortlessly identifies the country of origin associated with any valid phone number.
- Ease of Use: Integrates seamlessly with existing Python applications and features an intuitive API for convenient phone number validation and country detection.
- Highly Accurate: Utilizes a rigorously tested set of country-specific regular expressions to guarantee reliable validation results.

Supported Countries
-------------------

The module currently supports phone number validation for a wide range of countries, including:

- Africa: Zimbabwe, South Africa, Mozambique, Botswana, Malawi, Zambia, Ghana, Nigeria, Egypt
- Middle East: Israel
- Europe: United Kingdom (London), Netherlands
- Asia: China, Korea
- North America: United States of America
- South America: Argentina, Brazil
- Oceania: Australia

Applications
------------

This package offers a versatile solution for various applications, including:

- Contact Management Systems: Ensure accurate and consistent contact information for international customers and partners.
- User Registration Forms: Simplify user registration by providing seamless phone number validation and country detection.
- SMS Marketing Campaigns: Target specific regions and ensure successful delivery of SMS messages.
- Mobile Payment Systems: Implement secure and reliable mobile payment solutions with accurate phone number validation.
- International Business Transactions: Streamline international business communication and transactions with efficient phone number validation.

Installation
------------

The package can be easily installed using pip:

.. code-block:: bash

    pip install mobile-validate

Usage
-----

mobile-validate offers an intuitive API for phone number validation and country detection:

.. code-block:: python

    from mobile_validate.validator import valid_mobile

    # Example: Valid Zimbabwe Mobile Number
    phone_number = "+263771234567"
    country = "Zimbabwe"

    if valid_mobile(phone_number, country):
        print(f"Valid {country} mobile number")
    else:
        print(f"Not a valid {country} number")

Note
----

This package is under active development, and contributions are always welcome.

""",
    license="MIT",
    url="https://github.com/taqsblaze/mobile-validate",
    install_requires=["pip"],
    classifiers=[
    	"Development Status :: 3 - Alpha",
		"Intended Audience :: 2 - Developers",
		"Topic :: 7 - Communications",
		"Topic :: 16 - Software Development",
		"License :: OSI Approved :: MIT License",
		"Programming Language :: 7 - Python :: 3",
		"Operating System :: 1 - OS Independent",
		"Classifier :: 11 - Phone Number Validation",
		"Classifier :: 12 - Country Detection",
		"Classifier :: 13 - International",
		"Classifier :: 14 - Regular Expressions"
		],
	python_requires=">=3.8",
    entry_points={"cli":["snipet=mobile_validate.validator:Example.show"]}
)