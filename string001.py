def create_new_string(input_string):
    if not input_string:    #check string is empty
        return ""
    first_char = input_string[0]
    last_char = input_string[-1]
    middle_char=input_string[len(input_string)//2]
    new_string=first_char + middle_char +last_char
    return new_string

#get user input
user_input =input("enter a string :")
result = create_new_string(user_input)
print(result)