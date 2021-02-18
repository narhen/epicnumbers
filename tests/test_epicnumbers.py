from epicnumbers import __version__
from epicnumbers import main as en

def test_version():
    assert __version__ == '1.0.0'

def test_string_to_int():
    assert en.string_to_int("1") == 1
    assert en.string_to_int("-2") == -2

    assert en.string_to_int("0xa") == 10
    assert en.string_to_int("0XA") == 10
    assert en.string_to_int("0Xa") == 10
    assert en.string_to_int("ah") == 10
    assert en.string_to_int("10h") == 16
    assert en.string_to_int("-10h") == -16

    assert en.string_to_int("1b") == 1
    assert en.string_to_int("0b10") == 2
    assert en.string_to_int("b11") == 3
    assert en.string_to_int("b-11") == -3

def test_as_8():
    assert en.as_8(10, en.LITTLE_ENDIAN) == (10, 10, '\\x0a')
    assert en.as_8(-10, en.LITTLE_ENDIAN) == (-10, 246, '\\xf6')

def test_as_16():
    assert en.as_16(10, en.LITTLE_ENDIAN) == (10, 10, '\\x0a\\x00')
    assert en.as_16(-10, en.LITTLE_ENDIAN) == (-10, 65526, '\\xf6\\xff')

def test_as_32():
    assert en.as_32(10, en.LITTLE_ENDIAN) == (10, 10, '\\x0a\\x00\\x00\\x00')
    assert en.as_32(-10, en.LITTLE_ENDIAN) == (-10, 4294967286, '\\xf6\\xff\\xff\\xff')

def test_as_64():
    assert en.as_64(10, en.LITTLE_ENDIAN) == (10, 10, '\\x0a\\x00\\x00\\x00\\x00\\x00\\x00\\x00')
    assert en.as_64(-10, en.LITTLE_ENDIAN) == (-10, 18446744073709551606, '\\xf6\\xff\\xff\\xff\\xff\\xff\\xff\\xff')


def test_format_binary():
    assert en.format_binary(10) == "1010"
    assert en.format_binary(128) == "10000000"
    assert en.format_binary(256) == "1 00000000"
