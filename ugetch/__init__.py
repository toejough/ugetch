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
    key = None
    if byte < 128:
        key = chr(byte)
    else:
        _put_byte(byte)
    return key


def utf8_parser(infile):
    '''Parse utf-8 bytes to a string'''
    first_byte = _get_byte(infile)
    key = None
    utf8_bytes = [first_byte]
    # get byte string in py 2 and 3
    try:
        if sys.version_info.major == 3:
            key = chr(first_byte)
        else:
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
            key = byte_string.decode('utf-8')
    except:
        # couldn't parse utf-8 out.  not a failure, just not a success.
        for b in utf8_bytes:
            _put_byte(b)
    return key


def tab_parser(infile):
    '''Parse a tab key out'''
    first_byte = _get_byte(infile)
    key = None
    if first_byte == 9:
        # Tab key
        key = 'TAB'
    else:
        _put_byte(first_byte)
    return key


def arrow_parser(infile):
    '''Parse arrow keys'''
    first_byte = _get_byte(infile)
    key = None
    if first_byte == 27:
        # escape.  Check for bracket
        second_byte = _get_byte(infile)
        if second_byte == 91:
            # final byte
            final_byte = _get_byte(infile)
            if final_byte == 65:
                key = 'UP'
            elif final_byte == 66:
                key = 'DOWN'
            elif final_byte == 67:
                key = 'RIGHT'
            elif final_byte == 68:
                key = 'LEFT'
            else:
                _put_byte(first_byte)
                _put_byte(second_byte)
                _put_byte(final_byte)
        else:
            _put_byte(first_byte)
            _put_byte(second_byte)
    else:
        _put_byte(first_byte)
    return key


# [ Global ]
_DEFAULT=object()  # enable dynamic defaults
# Special key parsers need to go before the ASCII parser, because
#   their first byte is generally in the ASCII range,
#   and would be sucked in raw by the ASCII parser.
_KEY_PARSERS=[tab_parser, arrow_parser, ascii_parser, utf8_parser]  # ways to parse keys from byte lists
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
