import sys
import string


def count_characters(text):
    """
    Analyzes the input text and counts upper, lower, punctuation,
    digits, and spaces.
    """
    sums = {
        "upper": 0,
        "lower": 0,
        "punctuation": 0,
        "digits": 0,
        "spaces": 0
    }
    for c in text:
        if c.isupper():
            sums["upper"] += 1
        elif c.islower():
            sums["lower"] += 1
        elif c.isdigit():
            sums["digits"] += 1
        elif c.isspace():
            sums["spaces"] += 1
        elif c in string.punctuation:
            sums["punctuation"] += 1
    return sums


def main():
    """
    Handles command-line arguments and calls the counting function.
    """
    # 1. Handle sys.argv logic
    # 2. Call count_characters()
    # 3. Print the results

    try:
        if len(sys.argv) < 2 or sys.argv[1] == "":
            print("What is the text to count?")
            text = sys.stdin.readline()
        elif len(sys.argv) == 2:
            text = sys.argv[1]
        else:
            raise AssertionError("more than one argument is provided")

        print(f"The text contains {len(text)} characters:")
        results = count_characters(text)
        print(f"{results['upper']} upper letters")
        print(f"{results['lower']} lower letters")
        print(f"{results['punctuation']} punctuation marks")
        print(f"{results['spaces']} spaces")
        print(f"{results['digits']} digits")

    except EOFError:
        pass
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
