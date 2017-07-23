import sys
import webbrowser

#This program is designed to convert integers from 1 to 4999 inclusive into
#is so that other programs may use this one. The other mode is if we did not pass
#standard roman numerals as well as convert roman numerals into the respective number.
#There are two modes, either giving the input as a command line
#argument in which only the roman numeral/number is printed to stdout.
#The other mode is if we did not pass a command line arg where we can test as many values manually as we want.
#Roman -> number is case insensitive

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
    elif number >= 40 and number < 50:
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
    if number < 400:
        for C in range(int(number/100)):
            roman_numeral = roman_numeral +  'C'
    elif number >= 400 and number < 500:
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

def check_quads(roman):
    invalid = ['IIII', 'VV','XXXX','LL','CCCC','DD']
    for n in invalid:
        if n in roman:
            raise Exception('Invalid roman numeral entered')

def get_num(roman):
    roman = roman.upper()
    val_map = {'':0, 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    value = 0
    last_char = ''
    check_quads(roman)
    for char in roman:
        if char not in val_map:
            raise Exception('Invalid roman numeral entered')
        if val_map.get(last_char) < val_map.get(char):
            value += val_map.get(char) - (val_map.get(last_char) + val_map.get(last_char))
        else:
            value += val_map.get(char)
        last_char = char
    return value

def print_all():
    with open('roman.txt', 'wb') as output:
        for i in range(5000):
            roman = get_roman(i)
            line = (str(get_num(roman)) + ', ' + roman + '\n').encode()
            output.write(line)
        webbrowser.open('roman.txt')



def main(args):  
    userInput = ''
    try:
        userInput = sys.argv[1]
        try:
            i = int(userInput)
            print(get_roman(i))
        except ValueError:
            i = str(userInput)
            print(get_num(i))
    except IndexError:
        while True:
            userInput = input('Enter an integer from 1 to 4999 inclusive or a roman numeral: ')
            try:
                userInput = int(userInput)
                if userInput <=0 or userInput > 4999:
                    print('Number has to be between 1 and 4999 inclusive.')
                    continue
                print(get_roman(userInput))
            except ValueError:
                print(get_num(userInput))

main(sys.argv)
#print_all()







    

