
import unittest

class NothingTest(unittest.TestCase):
    """
    Dummy test just to get unit test count above 0 to prevent
    django-jenkins failing due to no test results
    """
    
    def test_nothing(self):
        pass