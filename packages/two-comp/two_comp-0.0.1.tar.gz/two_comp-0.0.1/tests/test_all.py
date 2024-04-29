""" pytest """
import ctypes
import random

# pylint: disable=W0611
import pytest

import two_comp


def test_8():
    """test twos_8"""
    for x in range(0xFF):
        value = two_comp.twos_8(x)
        assert value == ctypes.c_int8(x).value


def test_16():
    """test twos_16"""
    for x in range(0xFFFF):
        value = two_comp.twos_16(x)
        assert value == ctypes.c_int16(x).value


def test_32():
    """test twos_32"""
    for _ in range(0xFFFFFF):
        test_value = random.randint(0xFFFF, 0xFFFFFFFF)
        value = two_comp.twos_32(test_value)
        assert value == ctypes.c_int32(test_value).value


def test_64():
    """test twos_64"""
    for _ in range(0xFFFFFF):
        test_value = random.randint(0xFFFFFFFF, 0xFFFFFFFFFFFFFFFF)
        value = two_comp.twos_64(test_value)
        assert value == ctypes.c_int64(test_value).value
