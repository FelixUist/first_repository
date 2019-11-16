import unittest

from instrument import Instrument

class TestInstrument(unittest.TestCase):

    def setUp(self):
        self.il = Instrument("Saxophone")
        self.i2 = Instrument("Guitar")

    def tearDown(self):
        pass

    def test_has_type(self):
        self.assertEqual("Guitar", self.i2.type)
        self.assertEqual("Saxophone", self.i1.type)

if __name__ == '__main__':
    unittest.main(verbosity=2)
