'''
ugetch
Supports getting ascii characters from the input
'''


# [ Imports ]
# [ -Python ]
import sys
import termios


# [ Global ]
_DEFAULT=object()  # enable dynamic defaults


# [ Helper Functions ]
def _get_byte(infile):
    fd = infile.fileno()
    old_settings = termios.tcgetattr(fd)
    byte = None
    try:
        new = termios.tcgetattr(fd)
        new[3] = new[3] & ~termios.ECHO
        new[3] = new[3] & ~termios.ICANON
        termios.tcsetattr(fd, termios.TCSADRAIN, new)
        byte = infile.read(1)
    # no catching - don't know what could go wrong, so no good way to handle it right now.
    # let it propagate up and generate a bug report.
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return byte


# [ Core Functions ]
def getkey(infile=_DEFAULT):
    '''Get a single key from the input file'''
    # Handle dynamic default
    if infile == _DEFAULT:
        # if not overridden, use the current sys.stdin
        infile = sys.stdin
    # Do the standard getch
    return _get_byte(infile)
