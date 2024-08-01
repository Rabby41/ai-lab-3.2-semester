def arrange_string(s):
    #separate lower and uper charecter
    lowercase_chars =[char for char in s if char.islower()]
    uppercase_chars= [char for char in s if char.isupper()]
    arrange_string=''.join(lowercase_chars+uppercase_chars)
    return arrange_string

input_string=input("enter a string")
#arrange the string
result=arrange_string(input_string)

print("result:",result)