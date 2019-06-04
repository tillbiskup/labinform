import unittest

import labinform.datasafe.datasafe as datasafe
#import aspecd
#from cwepr import dataset


class TestDatasafe(unittest.TestCase):
    def setUp(self):
        self.datasafe = datasafe.Datasafe()

    def test_instantiate_class(self):
        pass

    def test_has_generate_method(self):
        self.assertTrue(hasattr(self.datasafe, 'generate'))
        self.assertTrue(callable(self.datasafe.generate))

    def test_call_generate_with_parameters(self):
        self.datasafe.generate("cwepr", "sa42")

    def test_generate_returns_loi(self):
        loi = self.datasafe.generate("cwepr", "sa42")
        self.assertEqual("42.1001/ds/cwepr/sa42/01/data/raw", loi)

    def test_has_push_method(self):
        self.assertTrue(hasattr(self.datasafe, 'push'))
        self.assertTrue(callable(self.datasafe.push))

    def test_call_push_with_parameters(self):
        self.datasafe.push("", "42.1001/ds/cwepr/sa42/01/data/raw")

    def test_has_pull_method(self):
        self.assertTrue(hasattr(self.datasafe, 'pull'))
        self.assertTrue(callable(self.datasafe.pull))

    def test_call_pull_with_parameters(self):
        self.datasafe.pull("42.1001/ds/cwepr/sa42/01/data/raw")

    def test_pull_returns_data(self):
        data = self.datasafe.pull("42.1001/ds/cwepr/sa42/01/data/raw")
        self.assertEqual(str, type(data))

    def test_has_index_method(self):
        self.assertTrue(hasattr(self.datasafe, 'index'))
        self.assertTrue(callable(self.datasafe.index))

    def test_call_index_with_parameters(self):
        self.datasafe.index("42.1001/ds/cwepr/sa42/01/data/raw")

    def test_index_returns_dict(self):
        returnvalue = self.datasafe.index()
        self.assertTrue(type(returnvalue) == dict)

    def test_has_checksum_method(self):
        self.assertTrue(hasattr(self.datasafe, 'checksum'))
        self.assertTrue(callable(self.datasafe.checksum))

    def test_call_checksum_with_parameters(self):
        self.datasafe.checksum("42.1001/ds/cwepr/sa42/01/data/raw")

    def test_checksum_returns_str(self):
        checksum = self.datasafe.checksum("42.1001/ds/cwepr/sa42/01/data/raw")
        self.assertEqual(str, type(checksum))

    def test_has_moveto_method(self):
        self.assertTrue(hasattr(self.datasafe, 'moveto'))
        self.assertTrue(callable(self.datasafe.moveto))


class TestGenerate(unittest.TestCase):
    def setUp(self):
        self.datasafe = datasafe.Datasafe()
        #self.path =




