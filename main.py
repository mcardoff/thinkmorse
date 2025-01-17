#!/usr/bin/python

from time import sleep

text_string = "HELLOWORLD"  # Text to display in morse
multiplier = 0.15  # Speed multiplier (less is faster)

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

# International Morse code is composed of five elements:
# - short mark, dot or "dit" (.): "dot duration" is one time unit long
# - longer mark, dash or "dah" (-): three time units long
# - inter-element gap between the dots and dashes within a character: one dot duration or one unit long
# - short gap (between letters): three time units long
# - medium gap (between words): seven time units long

DOT_LENGTH = 1
DASH_LENGTH = 3
INNER_ELE_GAP = 1
LETTER_GAP = 3
WORD_GAP = 7
LOOP_GAP = 10


def text_to_morse(txt):
    """Convert text string to morse cipher and return it."""
    cipher = ""
    for letter in txt.upper():
        if letter != " ":
            cipher += MORSE_CODE_DICT[letter] + " "
        else:
            cipher += "/"
    return cipher


def led(state):
    """ Turn the LED on (true) or off (false). """
    led = open("/sys/class/leds/platform::micmute/brightness", "w")
    # led = open("/sys/class/leds/input3::capslock/brightness", "w")
    
    if state:
        led.write("1")  # LED On
    else:
        led.write("0")  # LED Off
        
    led.flush()
    led.close()


if __name__ == "__main__":
    while True:
        led(False)
        morse_string = text_to_morse(text_string)
        for ind,ch in enumerate(morse_string[:-1]):
            if ch == ".":
                led(True)
                sleep(multiplier * DOT_LENGTH)
                led(False)

                if morse_string[ind+1] != " " and morse_string[ind+1] != "/":
                    sleep(multiplier * INNER_ELE_GAP)

            elif ch == "-":
                led(True)
                sleep(multiplier * DASH_LENGTH)
                led(False)

                if morse_string[ind+1] != " " and morse_string[ind+1] != "/":
                    sleep(multiplier * INNER_ELE_GAP)

            elif ch == " ":
                if morse_string[ind+1] != "/" and morse_string[ind-1] != "/":
                    sleep(multiplier * LETTER_GAP)

            elif ch == "/":
                sleep(multiplier * WORD_GAP)

        sleep(multiplier * LOOP_GAP)
