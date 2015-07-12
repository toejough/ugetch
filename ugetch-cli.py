'''
Test script for ugetch
'''


# [ Imports ]
# [ - Python ]
import sys
# [ - Third Party ]
# [ - Project ]
import ugetch


# [ Test script ]
if __name__ == "__main__":
    print("hit ctrl-c to exit.")
    try:
        while True:
            sys.stdout.write("hit a key to print its representation: ")
            sys.stdout.flush()
            print(ugetch.getkey())
    except KeyboardInterrupt:
        print("\nexiting due to Ctrl-c")
        exit(0)
