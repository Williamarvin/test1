import calc as c
from calc import calc
import unittest

calcs = c.calc()

class Testing(unittest.TestCase):
    
    def tearDown(self):
        print("Tear Down")
        
    def setUp(self) -> None:
        print("set up")
    
    def test_add(self):
        print("test add")
        self.assertEqual(calcs.add(5,3), 8)
        self.assertEqual(calcs.add(5,3), 8)
        

def func(x) -> int:
    return x
        
if __name__ == '__main__':
    # unittest.main()
    
    print(func(2))