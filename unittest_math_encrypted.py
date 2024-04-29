import math_encrypted as unit
import unittest


class TestMathEncrypted(unittest.TestCase):

    def test_is_prime(self):

        # 1-3
        self.assertEqual(unit.is_prime(1, accuracy=5), False)
        self.assertEqual(unit.is_prime(2, accuracy=5), True)
        self.assertEqual(unit.is_prime(3, accuracy=5), True)

        # small numbers
        self.assertEqual(unit.is_prime(7, accuracy=5), True)
        self.assertEqual(unit.is_prime(8, accuracy=5), False)
        self.assertEqual(unit.is_prime(13, accuracy=5), True)

        # medium numbers
        self.assertEqual(unit.is_prime(8030974187, accuracy=20), True)
        self.assertEqual(unit.is_prime(8030974185, accuracy=20), False)
        self.assertEqual(unit.is_prime(20511149, accuracy=20), False)

        # large numbers
        self.assertEqual(unit.is_prime(7935136383906738772344751824169668733357252153420519306710214722883965447213032023660151594341119401, accuracy=50), True)
        self.assertEqual(unit.is_prime(13179529148667419313752621434193363370806933128742294644974969657446901001, accuracy=50), False)
        self.assertEqual(unit.is_prime(1116046526345976973244076121086481993689310851521763126311899231751259377733001931971438730236525849, accuracy=50), False)
        self.assertEqual(unit.is_prime(8962940820022532954380979647822843129973348706621205180007201628206439308494875826174674526082748906884765625, accuracy=50), False)


if __name__ == '__main__':
    unittest.main()