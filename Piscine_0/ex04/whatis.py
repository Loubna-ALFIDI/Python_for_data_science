import sys

if (len(sys.argv) == 1):
    sys.exit(1)

try:
    assert len(sys.argv) == 2
    number = int(sys.argv[1])
except ValueError:
    print("AssertionError: argument is not an integer")
    sys.exit(1)
except AssertionError:
    print("AssertionError: more than one argument is provided")
    sys.exit(1)

if number % 2 == 0:
    print("I'm Even")
else:
    print("I'm Odd")
