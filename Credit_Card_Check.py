#Simple Python3 program to run on the shell using Luhn's ALgorithm to confirm whether card number provided is either a
#VISA, American Express or a Mastercard
#Luhns Algorthm is a simple checksum formula used to validate a variety of identification numbers, such as credit card numbers
#you can read about it and the more complex ones at https://en.wikipedia.org/wiki/Luhn_algorithm

def main():
    #promt user for card number
    print("Please provide a sample card# and we will validate if its possibly a AMEX, VISA or MASTERCARD number\n");
    credit = str(input("Card Number: "));

    for letter in credit:
        if(not letter.isdigit()):  #error checking should any non-number be entered
            exit("invalid Input");
            return 1;
    if (12 > len(credit) or 17 <= len(credit) or len(credit) ==14): #error if incorrect card# length
        exit("invalid ---Input");
        return 1;


    first2 = int(credit[:2]); # distinguish between AMEX & mastercards using first 2 digits
    first1 = int(credit[0]);  # distinguish VISA by first digit

    #initilzing variables for Luhn algorthim
    k= 0;
    i=0;
    if (first2 == 34 or first2 == 37 or first2 == 51 or first2 == 52 or first2 == 53 or first2 == 54 or first2 == 55 or first1 == 4):
        for c in (credit[::-1]):

            if (i%2 != 0):
                k += int(((int(c)*2) %10)) + int(((int(c)*2)/10));
                i +=1;
            else:
                k += int(c);
                i +=1;

        #if card length is valid mod10 should return zero
        if (k%10 == 0):
            if( first2 == 34 or first2 == 37):
                print("\nThe card provided is a AMEX card \n");
            elif (first2 == 51 or first2 == 52 or first2 == 53 or first2 == 54 or first2 == 55 ):
                print("\nThe card provided is a MASTERCARD\n");
            elif (first1 == 4):
                print("\nThe card provided is a VISA card\n");
        else:
            print("\ncard is not a valid AMEX, VISA, or MASTERCARD\n");
    else:
        print("\ncard is not a valid AMEX, VISA, or MASTERCARD\n");

if __name__ == "__main__":
    main()