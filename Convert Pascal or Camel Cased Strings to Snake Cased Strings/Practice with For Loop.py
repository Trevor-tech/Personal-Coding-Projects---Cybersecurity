def convert_to_snake_cased_string(camel_or_pascal_cased_string): #parameter is any string that has a capital letter at the start of each word e.g., ILoveSalmon
    snake_cased_string_char = [] #Where converted characters are appended into.
    for char in camel_or_pascal_cased_string:
        if char.isupper(): #check for uppercase
            converted_char = '_' + char.lower() #puts _ followed by capital character converted to lower case.
            snake_cased_string_char.append(converted_char) #appends into list
        else:
            snake_cased_string_char.append(char) #appends into list for all lowercase characters
    
    snake_cased_string_joined = ''.join(snake_cased_string_char) #joins all converted to characters to from snake cased string.
    cleaned_snake_cased_string = snake_cased_string_joined.strip('_') #removes starting and ending characters that was stated as .strip's argument

    return cleaned_snake_cased_string

def main():
    print(f'\nConverted to snake cased string: {convert_to_snake_cased_string("A Long And Complex String")}')

main()