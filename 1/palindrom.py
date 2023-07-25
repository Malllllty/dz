def is_palindrome(the):
    the = the.lower().replace(' ', '')
    # Сравнение строки с ее перевернутой версией
    if the == the[::-1]:
        return "True"
    else:
        return "False"
    
print(is_palindrome('А роза упала на лапу Азора'))