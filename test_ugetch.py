'''
Test suite for ugetch
'''


# [ Imports ]
# [ - Python ]
import tempfile
import os
# [ - Third Party ]
import pytest
import pexpect
# [ - Project ]
import ugetch


# [ Helpers ]
def in_vs_out(input_values):
    '''supply ascii chars, use getch, and validate ascii returned'''
    p = pexpect.spawn("python ugetch-cli.py", timeout=0.5)
    p.expect_exact("hit ctrl-c to exit.")
    for value in input_values:
        p.expect_exact("hit a key to print its representation: ")
        p.sendline(value)
        index = p.expect_exact([value, pexpect.EOF, pexpect.TIMEOUT])
        assert index == 0, "did not find expected ({}) in output ({})".format(
            value, p.before
        )


# [ Unit tests ]
def test_getch_ascii():
    '''supply ascii chars, use getch, and validate ascii returned'''
    in_vs_out(" \n\t")
    all_printable_acii = [chr(n) for n in range(32, 127)]  # not including 127
    in_vs_out(all_printable_acii)
