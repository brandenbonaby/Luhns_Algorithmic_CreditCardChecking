# Luhns_Algorithmic_CreditCardChecking
Simple Python3 program to run on the shell using Luhn's ALgorithm to confirm whether card number provided is either a VISA, American Express or a Mastercard Luhns Algorthm is a simple checksum formula used to validate a variety of identification numbers, such as credit card numbers you can read about it and the more complex ones at https://en.wikipedia.org/wiki/Luhn_algorithm

<h2> Usage:</h2>

you can run the program by entering **python Credit_Card_Check.py** to execute on the cmdline shell.  

<h2>Sample Output:</h2>

**$ python Credit_Card_Check.py**

**Please provide a sample card# and we will validate if its possibly a AMEX, VISA or MASTERCARD number**

**Card Number: 4111111111111111**

**The card provided is a VISA card**

<h2> Limitations: </h2>

This program will only check for VISA, MASTERCARD and AMEX card numbers, right now VISA card numbers are of length 13 or 16 and they usually start with the number 4. AMEX cards start with 34 or 37 and are usually 15 numbers in length. Lastly MASTERCARD's start with 51, 52, 53, 54, or 55 and are usually 16 numbers in length.
