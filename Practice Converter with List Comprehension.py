def convert_to_snake_cased_string(pascal_or_camel_cased_string):
    snake_cased_string =['_' + char.lower() if char.isupper() #note: 
                         else char 
                         for char in pascal_or_camel_cased_string] #code written inside list for conciseness and smooth operation.

    return ''.join(snake_cased_string).strip('_') #list comprehension also used here

def main():
    print(f'\nConverted to snake cased string: {convert_to_snake_cased_string("ALongAndComplexString")}')

main()