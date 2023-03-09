# :::::::::::DESCRIPTION:::::::::::::::::::::
# This function serves as a test for the cipher function

from cipher_kmh2259 import cipher_kmh2259

def test_cipher_single():
    example = 'apple'
    expected = 'dssoh'
    actual = cipher_kmh2259.cipher(example, 3)
    assert actual == expected, "Encrypted word should be 'dssoh'"
test_cipher_single()
