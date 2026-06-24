import unittest
from PhiBase import PhiBase, transfer_to_int, transfer_int_to_Phi

class TestPhiBase(unittest.TestCase):

    def test_creation(self):

        for i in ["0", "1", "10.01", "101.01", "1000.1001"]:
            self.assertEqual(PhiBase(i).x, i)
        
        for i in ["2", "11", "1.1.1", "abc", "0.11"]:
            with self.assertRaises(TypeError):
                PhiBase(i)

    def test_round_trip_and_normalization(self):

        for i in range(11):
            phi = transfer_int_to_Phi(float(i))

            self.assertAlmostEqual(transfer_to_int(phi), float(i), places=9)
            self.assertNotIn("11", phi.x.replace('.', ''))

if __name__ == "__main__":
    unittest.main()