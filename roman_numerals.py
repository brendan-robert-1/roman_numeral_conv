import sys

#This program is designed to convert integers from 1 to 4999 inclusive into
#standard roman numerals. There are two modes, either giving the number as a command line
#argument in which only the roman numeral is printed to stdout. This mode
#is so that other programs may use this one. The other mode is if we did not pass
#a command line arg where we can test as many numbers manually as we want.

def less_than_ten(number):
    if number >= 10:
        raise Exception('Number is not less than 10')
    roman_numeral = ''
    if number < 4:
        for I in range(number):
            roman_numeral = roman_numeral + 'I'
    elif number == 4:
        roman_numeral = 'IV'
    elif number >= 5 and number < 9:
        roman_numeral = 'V'
        for I in range(number - 5):
            roman_numeral = roman_numeral + 'I'
    elif number  == 9:
        roman_numeral = 'IX'
    return roman_numeral          



def less_than_hund(number):
    if number >= 100:
        raise Exception('Number is not less than 100')
    roman_numeral = ''
    if number < 40:
        for X in range(int(number / 10)):
            roman_numeral = roman_numeral + 'X'
    elif number == 40:
        roman_numeral = 'XL'
    elif number >= 50 and number < 90:
        roman_numeral = 'L'
        for X in range(int((number - 50)/10)):
            roman_numeral = roman_numeral + 'X'
    elif number >= 90:
        roman_numeral = 'XC'
    roman_numeral = roman_numeral + less_than_ten(number % 10)
    return roman_numeral




def less_than_thous(number):
    if number >= 1000:
        raise Exception('Number is not less than 1000')
    roman_numeral = ''
    if number < 500:
        for C in range(int(number/100)):
            roman_numeral = roman_numeral +  'C'
    elif number == 400:
        roman_numeral = 'CD'
    elif number >= 500 and number < 900:
        roman_numeral = 'D'
        for C in range(int((number - 500) / 100)):
            roman_numeral = roman_numeral + 'C'
    elif number >= 900:
        roman_numeral = 'CM'
    roman_numeral = roman_numeral + less_than_hund(number % 100)
    return roman_numeral

def less_than_max(number):
    if number >= 5000:
        raise Exception('Number is not less than 5000')
    roman_numeral = ''
    for M in range(int(number / 1000)):
        roman_numeral = roman_numeral + 'M'
    roman_numeral = roman_numeral + less_than_thous(number % 1000)
    return roman_numeral



def get_roman(number):
    if number < 10:
        return less_than_ten(number)
    elif number < 100:
        return less_than_hund(number)
    elif number < 1000:
        return less_than_thous(number)
    elif number <= 4999:
        return less_than_max(number)


userInput = ''
try:
    userInput = sys.argv[1]
    print(get_roman(int(userInput)))
except IndexError:
    while True:
        try:
            userInput = int(input('Enter an integer from 1 to 4999 inclusive: '))
            if userInput <=0 or userInput > 4999:
                print('Number has to be between 1 and 4999 inclusive.')
                continue
            print(get_roman(userInput))
        except ValueError:
            print('Not an integer!')






    

