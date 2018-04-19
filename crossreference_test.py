from crossreference import *

import unittest
import importlib

class TestCrossReference(unittest.TestCase):

    def test_reference(self):

        #test any common lib could be referenced
        loader = importlib.util.find_spec('codetimer')
        self.assertTrue(loader is not None)