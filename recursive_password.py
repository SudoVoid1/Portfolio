import string
import random as ran

def passwordgen(text,maxlength):
    #length of text will also be 0 as it hold no data yet
    # will recurise picking new charcter until >maxlength
    if len(text) < maxlength:
        randomChar = get_random_char()
        return passwordgen(text+randomChar,maxlength)
    else:
        return text

def get_random_char():
    chars = string.printable
    #chooses a random printable character (digits,ascii,puncuation, and whitespace)
    randomChar = chars[ran.randint(0,len(chars)-1)]
    return randomChar

while True:
    maxlen = input(' [?] Enter a password length (type e to exit): ')
    try:
        #try and make length an int
        maxlength = int(maxlen)
        print("'",passwordgen('',maxlength),"'\n")
    except:
        if maxlen == 'e':
            break
        print('Please Enter an integer')