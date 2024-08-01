def count_characters(input_string):
    letters=0
    digits=0
    special_symbols=0

    for char in input_string:
        if char.isalpha():
            letters+=1
        elif char.isdigit():
            digits+=1
        else:
            special_symbols+=1
            return letters,digits,special_symbols

#get user input
input_string = input("Enput a string :")
letters,digits,specials_symbols = count_characters(input_string)

print(f"letter :{letters}")
print(f"digit :{digits}")
print(f"special_symbol :{specials_symbols}")

