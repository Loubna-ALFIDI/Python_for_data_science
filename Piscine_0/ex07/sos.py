import sys


def main():
    """
    Encodes a string into Morse Code.
    Exactly one string argument is required.
    """
    NESTED_CODE = {
        'A': '.-',    'B': '-...',  'C': '-.-.',
        'D': '-..',   'E': '.',     'F': '..-.',
        'G': '--.',   'H': '....',  'I': '..',
        'J': '.---',  'K': '-.-',   'L': '.-..',
        'M': '--',    'N': '-.',
        'O': '---',   'P': '.--.',  'Q': '--.-',
        'R': '.-.',   'S': '...',
        'T': '-',     'U': '..-',   'V': '...-',
        'W': '.--',   'X': '-..-',
        'Y': '-.--',  'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-',
        '5': '.....', '6': '-....',
        '7': '--...', '8': '---..',
        '9': '----.'
    }

    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
        morse = []
        text = sys.argv[1].upper()
        for char in text:
            if char == " ":
                morse.append("/")
            elif char in NESTED_CODE:
                morse.append(NESTED_CODE[char])
            else:
                raise AssertionError("the arguments are bad")
        print(" ".join(morse))
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
