"""
	A library for converting integer numbers to twos complement values
	
"""


def twos_8(num):
    """Converts 8 bit number to twos complement"""
    if num > 0x7F:
        num ^= 0xFF
        return -(num + 1)
    return num


def twos_16(num):
    """Converts 16 bit number to twos complement"""
    if num > 0x7FFF:
        num ^= 0xFFFF
        return -(num + 1)
    return num


def twos_32(num):
    """Converts 32 bit number to twos complement"""
    if num > 0x7FFFFFFF:
        num ^= 0xFFFFFFFF
        return -(num + 1)
    return num


def twos_64(num):
    """Converts 64 bit number to twos complement"""
    if num > 0x7FFFFFFFFFFFFFFF:
        num ^= 0xFFFFFFFFFFFFFFFF
        return -(num + 1)
    return num
