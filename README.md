# epicnumbers

A small tool I often used to convert a number into various other formats

# Usage

`pip install -r requirements.txt`

`python epicnumbers.py <number>`

# Examples

Convert -100 into signed, unsigned, hex, printable and binary in different sized integers
```
$ python ./epicnumbers.py -100
type      signed              unsigned  hex                  printable                         binary
------  --------  --------------------  -------------------  --------------------------------  -----------------------------------------------------------------------
8 bit       -100                   156  0x9c                 \x9c                              10011100
16 bit      -100                 65436  0xff9c               \x9c\xff                          11111111 10011100
32 bit      -100            4294967196  0xffffff9c           \x9c\xff\xff\xff                  11111111 11111111 11111111 10011100
64 bit      -100  18446744073709551516  0xffffffffffffff9cL  \x9c\xff\xff\xff\xff\xff\xff\xff  11111111 11111111 11111111 11111111 11111111 11111111 11111111 10011100
```

Convert 0x100 into signed, unsigned, hex, printable and binary in different sized integers
```
$ python ./epicnumbers.py 100h
type      signed    unsigned  hex    printable                         binary
------  --------  ----------  -----  --------------------------------  ----------
16 bit       256         256  0x100  \x00\x01                          1 00000000
32 bit       256         256  0x100  \x00\x01\x00\x00                  1 00000000
64 bit       256         256  0x100  \x00\x01\x00\x00\x00\x00\x00\x00  1 00000000
```

Convert 100b (binary) into signed, unsigned, hex, printable and binary in different sized integers
```
$ python ./epicnumbers.py 100b
type      signed    unsigned  hex    printable                           binary
------  --------  ----------  -----  --------------------------------  --------
8 bit          4           4  0x4    \x04                                   100
16 bit         4           4  0x4    \x04\x00                               100
32 bit         4           4  0x4    \x04\x00\x00\x00                       100
64 bit         4           4  0x4    \x04\x00\x00\x00\x00\x00\x00\x00       100
```

