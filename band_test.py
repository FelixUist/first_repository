import unittest

from band import Band
from musician import Musician
from instrument import Instrument

class TestBand(unittest.TestCase):

    def setup(self):

        self.sax = Instrument("Saxophone")
        self.guitar = Instrument("Guitar")
        self.drums = Instrument("Drums")

        self.m1 = Musician("Evan Parker", self.sax )
        self.m2 = Musician("Derek Bailey", self.guitar )
        self.m3 = Musician("Han Bennink", self.drums )

        self.lungs_band = Band("Lungs Band", [self.m1, self.m2, self.m3])

    def tearDown(self):
        pass

    def test_band_has_musicians(self):
        self.assertEqual(len(self.lungs_band.musicians)), 3))
        print(self.lungs_band.musicians)


if __name__ == '__main__':
    unittest.main(verbosity=2)
