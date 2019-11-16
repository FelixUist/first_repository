import unittest

from musician import Musician

class TestMusician(unittest.TestCase):

    def setUp(self):
        self.m1 = Musician("Evan Parker", "Saxophone")
        self.m2 = Musician("Derek Bailey", "Guitar")

    def tearDown(self):
        pass

    def test_musician_has_name(self):
        self.assertEqual(self.m1.name, "Evan Parker")

    def test_musician_has_instrument(self):
        self.assertEqual(self.m1.instrument, "Saxophone")
        self.assertEqual(self.m2.instrument, "Guitar")

    def test_can_play_saxophone(self):
        self.assertEqual("I'm playing squeek, multiphonic pattern", self.m1.play_song("squeek, multiphonic pattern"))


if __name__ == '__main__':
    unittest.main(verbosity=2)
