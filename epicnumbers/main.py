#!/usr/bin/env python3

import argparse
from sys import argv, exit
from string import digits, ascii_letters
from struct import unpack, pack

from tabulate import tabulate
from epicnumbers import __version__

BIG_ENDIAN = ">"
LITTLE_ENDIAN = "<"

def convert_to(num, fmt):
    signed_fmt, unsigned_fmt = fmt.lower(), fmt.upper()

    try:
        if num < 0:
            packed = pack(signed_fmt, num)
        else:
            packed = pack(unsigned_fmt, num)
    except:
        return None

    printable_chars = [c for c in digits + ascii_letters]

    signed = unpack(signed_fmt, packed)[0]
    unsigned = unpack(unsigned_fmt, packed)[0]
    printable = "".join([x if x in printable_chars else "\\x{:02x}".format(x) for x in packed])
    return signed, unsigned, printable

def as_8(num, endian):
    """8 bit"""
    return convert_to(num, "{}b".format(endian))

def as_16(num, endian):
    """16 bit"""
    return convert_to(num, "{}h".format(endian))

def as_32(num, endian):
    """32 bit"""
    return convert_to(num, "{}i".format(endian))

def as_64(num, endian):
    """64 bit"""
    return convert_to(num, "{}q".format(endian))

def format_binary(unsigned):
    b = bin(unsigned)[2:][::-1]
    return " ".join([b[x:x + 8] for x in range(0, len(b), 8)])[::-1]

def create_output(signed, unsigned, printable, doc):
    return [doc, signed, unsigned, hex(unsigned), printable, format_binary(unsigned)]

def string_to_int(num):
    # if hex
    if num[:2] in ["0x", "0X"]:
        return int(num, 16)
    if num[-1] in ["h", "H"]:
        return int(num[:-1], 16)

    # if binary
    if num[:2] in ["0b", "0B"]:
        return int(num, 2)
    if num[:1] in ["b", "B"]:
        return int(num[1:], 2)
    if num[-1] in ["b", "B"]:
        return int(num[:-1], 2)

    # if decimal
    return int(num, 10)

def parse_args():
    parser = argparse.ArgumentParser(description="Convert a number into various other formats")
    parser.add_argument("number", type=str,
            help="A number to convert. In decimal, hex, or binary. F.ex -10, 0x10, or 0b1010")
    parser.add_argument("-V", "--version", action="version", version=f"%(prog)s {__version__}")

    return parser.parse_args()

def main():
    funcs = [as_8, as_16, as_32, as_64]

    args = parse_args()


    num = string_to_int(args.number)

    converted = []
    for func in funcs:
        res = func(num, LITTLE_ENDIAN)
        if not res:
            continue

        s, u, p = res
        converted += [create_output(s, u, p, func.__doc__)]

    headers = ["type", "signed", "unsigned", "hex", "printable", "binary"]
    print(tabulate(converted, headers=headers))

if __name__ == "__main__":
    exit(main())
