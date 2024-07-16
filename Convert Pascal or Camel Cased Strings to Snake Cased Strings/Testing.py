def convert_to_snake_case(pascal_or_camel_cased_string):

    snake_cased_char_list = ['_' + char.lower() for char in pascal_or_camel_cased_string if char.isupper()]

    return ''.join(snake_cased_char_list).strip('_')

def main():
    print(convert_to_snake_case('aLongAndComplexString'))

main()