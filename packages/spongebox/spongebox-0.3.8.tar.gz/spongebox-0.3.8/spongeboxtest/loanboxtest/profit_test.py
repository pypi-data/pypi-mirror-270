import unittest
from spongebox.loanbox import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        print(profit(15 / 100, 32.5 / 100, 1.06, 5.3 / 100, 3.19 / 100))
        print(lost(15 / 100, 32.5 / 100, 1.06, 1.06 / 100, 3.19 / 100))
        print(lost(15 / 100, 32.5 / 100, 1.06, 1.5 / 100, 3.19 / 100))


if __name__ == '__main__':
    unittest.main()
