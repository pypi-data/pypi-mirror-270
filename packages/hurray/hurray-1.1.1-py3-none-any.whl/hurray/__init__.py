from __future__ import annotations

from array import array as _array, typecodes
from typing import Generic, Iterable, TypeVar
import sys

__version__ = '1.1.1'
__all__ = ('SByteArray', 'ByteArray',
           'CharArray', 'UCharArray',  # aliases for byte arrays
           'UnicodeArray',
           'ShortArray', 'UShortArray',
           'IntArray', 'UIntArray',
           'LongArray', 'ULongArray',
           'LongLongArray', 'ULongLongArray',
           'FloatArray', 'DoubleArray',
           'typecodes')


T = TypeVar('T')


class ArrayType(Generic[T]):
    def __init__(self, typecode: str):
        self.typecode = typecode

    def __call__(self, initializer: bytes | Iterable[T] = (), /) -> _array:
        return _array(self.typecode, initializer)


SByteArray = ArrayType[int]('b')
"""Stores signed chars (signed bytes). [-128; 127]"""
ByteArray = ArrayType[int]('B')
"""Stores unsigned chars (unsigned bytes). [0; 255]"""
if sys.version_info >= (3, 13):
    UnicodeArray = ArrayType[str]('w')
    """Stores Unicode strings."""
else:
    UnicodeArray = ArrayType[str]('u')
    """Stores Unicode strings."""
ShortArray = ArrayType[int]('h')
"""Stores signed 16-bit integers. [-32768; 32767]"""
UShortArray = ArrayType[int]('H')
"""Stores unsigned 16-bit integers. [0; 65535]"""
IntArray = ArrayType[int]('i')
"""
Stores *at least* signed 16-bit integers. [-32768; 32767]

Note:
    Python documentation states that ``array('i')`` elements *minimal* size is **2 bytes** (**16 bits**).

    However, in most cases you deal with **32-bit** integers. [-2147483648; 2147483647]
"""
UIntArray = ArrayType[int]('I')
"""
    Stores at least unsigned 16-bit integers. [0; 65535]

Note:
    Python documentation states that ``array('I')`` elements *minimal* size is **2 bytes** (**16 bits**).

    However, in most cases you deal with **32-bit** integers. [0; 4294967295]
"""
LongArray = ArrayType[int]('l')
"""Stores signed 32-bit integers. [-2147483648; 2147483647]"""
ULongArray = ArrayType[int]('L')
"""Stores unsigned 32-bit integers. [0; 4294967295]"""
LongLongArray = ArrayType[int]('q')
"""Stores signed 64-bit integers. [−9223372036854775807; 9223372036854775807]"""
ULongLongArray = ArrayType[int]('Q')
"""Stores signed 64-bit integers. [0; 18446744073709551615]"""
FloatArray = ArrayType[float]('f')
"""Stores single-precision floating-point numbers."""
DoubleArray = ArrayType[float]('d')
"""Stores double-precision floating-point numbers."""

CharArray = SByteArray
UCharArray = ByteArray


def demo():
    print(f'{ShortArray([-4, -3, -2, -1, 0, 1, 2, 3, 4]) = }')
    print(f'{UIntArray([100_000, 100_001, 100_002, 100_003, 100_004]) = }')
    print(f'{ULongArray().itemsize = }')


if __name__ == '__main__':
    demo()
