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
def in_vs_out(input_values):
    '''supply ascii chars, use getch, and validate ascii returned'''
    # choose the correct spawn
    spawn = pexpect.spawn
    if sys.version_info.major == 3:
        spawn = pexpect.spawnu
    # spawn the subproc
    p = spawn("python ugetch-cli.py", timeout=0.5)
    p.expect_exact("hit ctrl-c to exit.")
    # test each char
    for value in input_values:
        p.expect_exact("hit a key to print its representation: ")
        p.send(value)
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

def test_getch_utf8():
    '''supply utf-8 glyphs, use getch, and validate the keys returned'''
    in_vs_out(['☢'])
    in_vs_out(['ά','έ','ή','ί','ΰ','α','β','γ','δ','ε','ζ','η','θ','ι','κ','λ','μ','ν','ξ','ο','π'])  # greek
    in_vs_out(['༰','༱','༲','༳','༴',' ༵','༶','༸',' ༹','༺',' ','༻',' ','༼','༽',' ༾',' ༿',' ','ཀ','ཁ','ག','གྷ','ང','ཅ','ཆ'])  # tibetan


if __name__ == '__main__':
    import cProfile
    cProfile.run("test_getch_ascii()")
