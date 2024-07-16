def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0

def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

main()

#Luhn Algorithm Fundamentals: Starting from the right of the string of numbers to the left, multiply every even positioned digit by 2. 
# If the product is more than 9 then add the digits of the product. Add doubled values, values where digits of product was added and 
# add odd positioned digits. If it is a multiple of 10, the number is valid, if not it is invalid. e.g.,  '4' where 4 is an even positioned 
# digit of a card number, *2 = 8 and '7' where 7 is a even positioned digit of the card number, *2 = 14 , add digits of 14, 1+4 = 5 (add 5 in the sum of
#  all digits). 