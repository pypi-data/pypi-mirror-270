import unittest
from spongebox.loanbox import *

class MyTestCase(unittest.TestCase):
    def test_something(self):
        # self.assertEqual(True, False)  # add assertion here
        print(get_repay_plan(10000,0.015,12))
        print(get_repay_plan(10000, 0.015, 12, "等额本金"))
        print(get_repay_plan(10000,0.015,12,"等本等息"))

    def test_k_term(self):
        print(get_k_term_equal_loan_payment(10000,0.015,12,1))
        
    def test_duration(self):
        print(get_duration([term[1] for term in get_repay_plan(10000,0.15/12,7)]))


if __name__ == '__main__':
    unittest.main()
