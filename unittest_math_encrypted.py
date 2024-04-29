'''
Apr 29, 2024
'''

import math_encrypted as unit
import unittest


class TestMathEncrypted(unittest.TestCase):

    def test_is_prime(self):

        # returns bool
        self.assertIsInstance(unit.is_prime(29, accuracy=5), bool)
        self.assertIsInstance(unit.is_prime(24, accuracy=5), bool)

        # 1-3
        self.assertFalse(unit.is_prime(1, accuracy=5))
        self.assertTrue(unit.is_prime(2, accuracy=5))
        self.assertTrue(unit.is_prime(3, accuracy=5))

        # small numbers
        self.assertTrue(unit.is_prime(7, accuracy=5))
        self.assertFalse(unit.is_prime(8, accuracy=5))
        self.assertTrue(unit.is_prime(13, accuracy=5))

        # medium numbers
        self.assertTrue(unit.is_prime(8030974187, accuracy=20))
        self.assertFalse(unit.is_prime(8030974185, accuracy=20))
        self.assertFalse(unit.is_prime(20511149, accuracy=20))

        # large numbers
        self.assertTrue(unit.is_prime(7935136383906738772344751824169668733357252153420519306710214722883965447213032023660151594341119401, accuracy=50))
        self.assertFalse(unit.is_prime(13179529148667419313752621434193363370806933128742294644974969657446901001, accuracy=50))
        self.assertFalse(unit.is_prime(1116046526345976973244076121086481993689310851521763126311899231751259377733001931971438730236525849, accuracy=50))
        self.assertFalse(unit.is_prime(8962940820022532954380979647822843129973348706621205180007201628206439308494875826174674526082748906884765625, accuracy=50))


    def test_generate_prime(self):

        # returns int
        self.assertIsInstance(unit.generate_prime(10), int)
        
        # correct size
        self.assertLess(unit.generate_prime(10), 2**10)
        self.assertLess(unit.generate_prime(20), 2**20)

        # is prime
        self.assertTrue(unit.is_prime(unit.generate_prime(16), accuracy=5))
        self.assertTrue(unit.is_prime(unit.generate_prime(64), accuracy=20))
        self.assertTrue(unit.is_prime(unit.generate_prime(128), accuracy=100))


    def test_gcd(self):

        # check if int
        self.assertIsInstance(unit.gcd(96, 128), int)
        
        # check values
        self.assertEqual(unit.gcd(96, 128), 32)
        self.assertEqual(unit.gcd(22, 26), 2)


    def test_random_coprime(self):
        
        # check if int
        self.assertIsInstance(unit.random_coprime(50), int)

        # check values
        self.assertEqual(unit.gcd(unit.random_coprime(2**16), 2**16), 1)


    def test_modular_inverse(self):
        
        # check if int
        self.assertIsInstance(unit.modular_inverse(131, 288), int)

        # check if correct
        self.assertEqual(unit.modular_inverse(131, 288), 11)
        self.assertEqual(unit.modular_inverse(11, 12), 11)
        self.assertEqual(unit.modular_inverse(7, 11), 8)
        self.assertEqual(unit.modular_inverse(3, 7), 5)

if __name__ == '__main__':
    unittest.main()