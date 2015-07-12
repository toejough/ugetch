'''
ugetch
Supports getting ascii characters from the input
'''


# [ Imports ]
# [ -Python ]
import sys
import termios


# [ Parsers ]
def ascii_parser(infile):
    '''Parse ascii bytes to ascii keys'''
    byte = _get_byte(infile)
    if byte < 128:
        return chr(byte)
    else:
        _put_byte(byte)


def utf8_parser(infile):
    '''Parse utf-8 bytes to a string'''
    first_byte = _get_byte(infile)
    # get byte string in py 2 and 3
    if sys.version_info.major == 3:
        string = chr(first_byte)
    else:
        utf8_bytes = [first_byte]
        if 194 <= first_byte <= 223:
            # 2 bytes
            utf8_bytes.append(_get_byte(infile))
        elif 224 <= first_byte <= 239:
            # 3 bytes
            utf8_bytes.append(_get_byte(infile))
            utf8_bytes.append(_get_byte(infile))
        elif 240 <= first_byte <= 244:
            # 4 bytes
            utf8_bytes.append(_get_byte(infile))
            utf8_bytes.append(_get_byte(infile))
            utf8_bytes.append(_get_byte(infile))
        byte_string = ''.join([chr(b) for b in utf8_bytes])
        string = byte_string.decode('utf-8')
    return string


# [ Global ]
_DEFAULT=object()  # enable dynamic defaults
_KEY_PARSERS=[ascii_parser, utf8_parser]  # ways to parse keys from byte lists
_BYTES=[]  # byte buffer from the input file


# [ Helper Functions ]
def _put_byte(byte):
    '''Put a single byte onto the buffer'''
    global _BYTES
    _BYTES.append(byte)


def _get_byte(infile):
    '''Get a single byte from either the buffer (if non-empty), or the input stream'''
    if _BYTES:
        byte = _BYTES[0]
        del _BYTES[0]
    else:
        fd = infile.fileno()
        old_settings = termios.tcgetattr(fd)
        char = None
        try:
            new = termios.tcgetattr(fd)
            new[3] = new[3] & ~termios.ECHO
            new[3] = new[3] & ~termios.ICANON
            termios.tcsetattr(fd, termios.TCSADRAIN, new)
            char = infile.read(1)
        # no catching - don't know what could go wrong, so no good way to handle it right now.
        # let it propagate up and generate a bug report.
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        byte = ord(char)
    return byte


# [ Core Functions ]
def getkey(infile=_DEFAULT):
    '''Get a single key from the input file'''
    # Handle dynamic default
    if infile == _DEFAULT:
        # if not overridden, use the current sys.stdin
        infile = sys.stdin
    # Set some defaults
    key = None
    byte_list = []
    key_type = None
    # Loop through parsers and return the first that matches
    for parser in _KEY_PARSERS:
        key = parser(infile)
        if key is not None:
            break
    # Return the key to the user
    return key
