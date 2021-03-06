import pytest

from .. import *

def test_bytes_base32():
    expr = Bytes("base32", "7Z5PWO2C6LFNQFGHWKSK5H47IQP5OJW2M3HA2QPXTY3WTNP5NU2MHBW27M")
    assert expr.type_of() == TealType.bytes
    expected = TealSimpleBlock([
        TealOp(Op.byte, "base32(7Z5PWO2C6LFNQFGHWKSK5H47IQP5OJW2M3HA2QPXTY3WTNP5NU2MHBW27M)")
    ])
    actual, _ = expr.__teal__()
    assert actual == expected

def test_bytes_base32_empty():
    expr = Bytes("base32", "")
    assert expr.type_of() == TealType.bytes
    expected = TealSimpleBlock([
        TealOp(Op.byte, "base32()")
    ])
    actual, _ = expr.__teal__()
    assert actual == expected

def test_bytes_base64():
    expr = Bytes("base64", "Zm9vYmE=")
    assert expr.type_of() == TealType.bytes
    expected = TealSimpleBlock([
        TealOp(Op.byte, "base64(Zm9vYmE=)")
    ])
    actual, _ = expr.__teal__()
    assert actual == expected

def test_bytes_base64_empty():
    expr = Bytes("base64", "")
    assert expr.type_of() == TealType.bytes
    expected = TealSimpleBlock([
        TealOp(Op.byte, "base64()")
    ])
    actual, _ = expr.__teal__()
    assert actual == expected

def test_bytes_base16():
    expr = Bytes("base16", "A21212EF")
    assert expr.type_of() == TealType.bytes
    expected = TealSimpleBlock([
        TealOp(Op.byte, "0xA21212EF")
    ])
    actual, _ = expr.__teal__()
    assert actual == expected

def test_bytes_base16_prefix():
    expr = Bytes("base16", "0xA21212EF")
    assert expr.type_of() == TealType.bytes
    expected = TealSimpleBlock([
        TealOp(Op.byte, "0xA21212EF")
    ])
    actual, _ = expr.__teal__()
    assert actual == expected

def test_bytes_base16_empty():
    expr = Bytes("base16", "")
    assert expr.type_of() == TealType.bytes
    expected = TealSimpleBlock([
        TealOp(Op.byte, "0x")
    ])
    actual, _ = expr.__teal__()
    assert actual == expected

def test_bytes_utf8():
    expr = Bytes("hello world")
    assert expr.type_of() == TealType.bytes
    expected = TealSimpleBlock([
        TealOp(Op.byte, "\"hello world\"")
    ])
    actual, _ = expr.__teal__()
    assert actual == expected

def test_bytes_utf8_special_chars():
    expr = Bytes("\t \n \r\n \\ \" \' 😀")
    assert expr.type_of() == TealType.bytes
    expected = TealSimpleBlock([
        TealOp(Op.byte, "\"\\t \\n \\r\\n \\\\ \\\" \' \\xf0\\x9f\\x98\\x80\"")
    ])
    actual, _ = expr.__teal__()
    assert actual == expected

def test_bytes_utf8_empty():
    expr = Bytes("")
    assert expr.type_of() == TealType.bytes
    expected = TealSimpleBlock([
        TealOp(Op.byte, "\"\"")
    ])
    actual, _ = expr.__teal__()
    assert actual == expected

def test_bytes_invalid():
    with pytest.raises(TealInputError):
        Bytes("base23", "")

    with pytest.raises(TealInputError):
        Bytes("base32", "Zm9vYmE=")

    with pytest.raises(TealInputError):
        Bytes("base64", "?????")

    with pytest.raises(TealInputError):
        Bytes("base16", "7Z5PWO2C6LFNQFGHWKSK5H47IQP5OJW2M3HA2QPXTY3WTNP5NU2MHBW27M")
