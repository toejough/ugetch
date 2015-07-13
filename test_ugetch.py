# -*- coding: utf-8 -*-


'''
Test suite for ugetch
'''


# [ Imports ]
# [ - Python ]
import tempfile
import os
import sys
# [ - Third Party ]
import pytest
import pexpect
# [ - Project ]
import ugetch


# [ Helpers ]
def start_cli_shim():
    # choose the correct spawn
    spawn = pexpect.spawn
    if sys.version_info.major == 3:
        spawn = pexpect.spawnu
    # spawn the subproc
    p = spawn("python ugetch-cli.py", timeout=0.5)
    p.expect_exact("hit ctrl-c to exit.")
    return p


def assert_expected(p, expected):
    '''Assert that we get the expected value'''
    index = p.expect_exact([expected, pexpect.EOF, pexpect.TIMEOUT])
    assert index == 0, "did not find expected ({}) in output ({})".format(
        value, p.before
    )


def in_vs_out(input_values):
    '''supply ascii chars, use getch, and validate ascii returned'''
    # get shim
    p = start_cli_shim()
    # test each char
    for value in input_values:
        p.expect_exact("hit a key to print its representation: ")
        p.send(value)
        assert_expected(p, value)


# [ Unit tests ]
def test_getch_ascii():
    '''supply ascii chars, use getch, and validate ascii returned'''
    all_printable_acii = [chr(n) for n in range(32, 127)]  # not including 127
    in_vs_out(all_printable_acii)


def test_getch_utf8():
    '''supply utf-8 glyphs, use getch, and validate the keys returned'''
    in_vs_out(['☢'])
    in_vs_out(['ά','έ','ή','ί','ΰ','α','β','γ','δ','ε','ζ','η','θ','ι','κ','λ','μ','ν','ξ','ο','π'])  # greek
    in_vs_out(['༰','༱','༲','༳','༴',' ༵','༶','༸',' ༹','༺',' ','༻',' ','༼','༽',' ༾',' ༿',' ','ཀ','ཁ','ག','གྷ','ང','ཅ','ཆ'])  # tibetan


def test_getch_tab():
    # get shim
    p = start_cli_shim()
    # test each char
    p.expect_exact("hit a key to print its representation: ")
    p.send('\t')
    assert_expected(p, 'TAB')
    p.sendcontrol('i')
    assert_expected(p, 'TAB')


if __name__ == '__main__':
    import cProfile
    cProfile.run("test_getch_ascii()")
