import sys
from ft_filter import ft_filter


def main():
    """
    Program that outputs a list of words from S that have a length
    greater than N.
    """      
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        s = sys.argv[1]
        try:
            n = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")
        words = s.split()
        result = ft_filter(lambda word: len(word) > n, words)

        print(result)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
