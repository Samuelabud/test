def text_backward(text):
    return text[::-1]

def morse(text):
    dictionary = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
        'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', 
        '7': '--...', '8': '---..', '9': '----.', '0': '-----',
        ' ': '//'}

    morse_code = []
    for character in text.upper():
        if character in dictionary:
            morse_code.append(dictionary[character])
    return ' '.join(morse_code)

def numerito(text):
    numbers = []
    for character in text.upper():
        if character.isalpha():
            numbers.append(str(ord(character) - ord('A') + 1))
    return ' '.join(numbers)

def oso_polar(text):
    dictionary2 = {'P': 'C', 'C': 'P', 'O': 'E', 'E': 'O', 'A': 'I', 'I': 'A','L': 'N', 'N': 'L', 'R': 'T', 'T': 'R'}
    polarcenit = []
    for character in text.upper():
        if character in dictionary2:
            polarcenit.append(dictionary2[character])
        else:
            polarcenit.append(character)
    return ''.join(polarcenit)

def decryption_polarcenit(text):
    return oso_polar(text)

def options():
    print("encryption methods are polarcenit, morse code and letters to numbers, which want do you want?")
    print("morse code = 1, polarcent = 2, numbers = 3")
    user_choice  = int(input("which want to do you choose?:  "))
    return user_choice

def code():
    sentence = input("what is your sentence? :  ")
    user_choice  = options()

    if user_choice == 1:
        text2 = morse(sentence)
    elif user_choice == 2:
        text2 = oso_polar(sentence)
    elif user_choice == 3:
        text2 = numerito(sentence)

    print("Your text encrypted is: ", text2)

    

code()


    