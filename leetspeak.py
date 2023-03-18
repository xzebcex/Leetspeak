# LeetSpeak

import random
import pyperclip  # pyperclip copies text to the clipboard.


def main():
    english = input('Enter your leet message: ')
    leetspeak = english_to_leet_speak(english)
    print(leetspeak)

    try:
        # Trying to use pyperclip will raise a NameError exception if
        # it wasn't imported:
        pyperclip.copy(leetspeak)
        print('(Copied leetspeak to clipboard.)')
    except NameError:
        pass  # Do nothing if pyperclip wasn't installed.


def english_to_leet_speak(message):
    # Convert the English string in message and return leetspeak.
    # Make sure all the keys in `charMapping` are lowercase.
    char_mapping = {'a': ['4', '@', '/-\\'], 'c': ['('], 'd': ['|)'], 'e': ['3'],
                    'f': ['ph'], 'h': [']-[', '|-|'], 'i': ['1', '!', '|'], 'k': [']<'],
                    'o': ['0'], 's': ['$', '5'], 't': ['7', '+'], 'u': ['|_|'],
                    'v': ['\\/']}

    leetspeak = ''
    for char in message:  # Check each character:
        # There is a 70% chance we change the character to leetspeak.
        if char.lower() in char_mapping and random.random() <= 0.70:
            possible_leet_replacements = char_mapping[char.lower()]
            leet_replacement = random.choice(possible_leet_replacements)
            leetspeak = leetspeak + leet_replacement
        else:
            # Don't translate this character:
            leetspeak = leetspeak + char
    return leetspeak


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    main()
