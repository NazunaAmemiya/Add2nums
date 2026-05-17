import unittest
from Add2Num import MyBigNumber 

class TestMyBigNumber(unittest.TestCase):
    
    def setUp(self):
        self.big_num = MyBigNumber()

    def test_01(self):
        print("="*50 + " Testcase 01 " + "="*50)
        self.assertEqual(self.big_num.sum("1234", "897"), "2131")

    def test_02(self):
        print("="*50 + " Testcase 02 " + "="*50)
        self.assertEqual(self.big_num.sum("99", "11"), "110")

    def test_03(self):
        print("="*50 + " Testcase 03 " + "="*50)
        self.assertEqual(self.big_num.sum("5", "5"), "10")

    def test_04(self):
        print("="*50 + " Testcase 04 " + "="*50)
        num1 = "99999999999999999999"
        num2 = "1"
        expected = "100000000000000000000"
        self.assertEqual(self.big_num.sum(num1, num2), expected)

    def test_05(self):
        print("="*50 + " Testcase 05 " + "="*50)
        self.assertEqual(self.big_num.sum("12345", "0"), "12345")

    def test_06(self):
        print("="*50 + " Testcase 06 " + "="*50)
        self.assertEqual(self.big_num.sum("0", "0"), "0")

    def test_07(self):
        print("="*50 + " Testcase 07 " + "="*50)
        self.assertEqual(self.big_num.sum("12", "50034"), "50046")

    def test_08(self):
        print("="*50 + " Testcase 08 " + "="*50)
        self.assertEqual(self.big_num.sum("70085", "14"), "70099")

    def test_09(self):
        print("="*50 + " Testcase 09 " + "="*50)
        self.assertEqual(self.big_num.sum("9998", "5"), "10003")

    def test_10(self):
        print("="*50 + " Testcase 10 " + "="*50)
        self.assertEqual(self.big_num.sum("999", "999"), "1998")

if __name__ == '__main__':
    unittest.main()