import unittest
import caesar
import block
import polyalphabetic as poly
import transposition as trans
import onetimepad as otp

class CipherTestCase(unittest.TestCase):
    def test_caesar_cipher(self):
        enc = caesar.create_cipher(12, 'test cipher')
        self.assertEqual(caesar.unlock_cipher(12, enc), 'test cipher')

    def test_polyalphabetic_cipher(self):
        enc = poly.create_cipher('treefrog', 'test polyalpha cipher')
        self.assertEqual(poly.unlock_cipher('treefrog', enc), 
        'test polyalpha cipher') 

    def test_onetimepad_cipher(self):
        key, enc = otp.create_cipher('legend of zelda, pizza party, mario bros.')
        self.assertEqual(otp.unlock_cipher(key, enc),
        'legend of zelda, pizza party, mario bros.')

    def test_block_cipher(self):
        key, enc = block.create_cipher('hunter2', 'Super Secret Message')
        self.assertEqual(block.unlock_cipher(key, enc), 'Super Secret Message')

    def test_transposition_columnar_cipher(self):
        enc = trans.create_cipher(5, 'The Germans are Coming!')
        self.assertEqual(trans.unlock_cipher(5, enc), 'thegermansarecoming!')


if __name__ == '__main__':
    unittest.main()
