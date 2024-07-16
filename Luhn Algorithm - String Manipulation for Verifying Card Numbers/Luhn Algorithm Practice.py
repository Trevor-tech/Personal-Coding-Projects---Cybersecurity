def verify_card_number(number):
    odd_digits_total = 0
    reversed_card_number = number[::-1]
    odd_digit_number = reversed_card_number[::2] #Arranges string for ease of calculation.
    for digits in odd_digit_number:
        odd_digits_total += int(digits)
    
    even_digits_total = 0 
    even_digit_number = reversed_card_number[1::2]
    for digits in even_digit_number:
        number = int(digits)*2 #As per luhn algorithm principles.
        if number >= 10:
            number = number//10 + number%10 #Adds digits of products (manual working for clarity)
        even_digits_total += number
    total = even_digits_total + odd_digits_total #totals digits
    return total%10 == 0 #Checks if multiple of 10 for validity

def main():
    card_number = '4111-1111-4555-1142'
    translation_principles = str.maketrans({'-': '', ' ': ''}) #Removes '-' and ' ' to make a string of numbers
    translated_card_number = card_number.translate(translation_principles) #Applies translation to selected variable.

    if verify_card_number(translated_card_number): #Under scenario that returned value is true
        print('VALID!')
    else:
        print('INVALID!')

main()