import unittest

import labinform.datasafe.datasafe as datasafe


class TestDatasafe(unittest.TestCase):
    def setUp(self):
        self.datasafe = datasafe.Datasafe()

    def test_instantiate_class(self):
        pass

    def test_has_create_method(self):
        self.assertTrue(hasattr(self.datasafe, 'generate'))
        self.assertTrue(callable(self.datasafe.generate))

    def test_call_generate_with_parameters(self):
        self.datasafe.generate("cwepr", "sa42")

    def test_has_push_method(self):
        self.assertTrue(hasattr(self.datasafe, 'push'))
        self.assertTrue(callable(self.datasafe.push))

    def test_has_pull_method(self):
        self.assertTrue(hasattr(self.datasafe, 'pull'))
        self.assertTrue(callable(self.datasafe.pull))

    def test_has_index_method(self):
        self.assertTrue(hasattr(self.datasafe, 'index'))
        self.assertTrue(callable(self.datasafe.index))

    def test_has_checksum_method(self):
        self.assertTrue(hasattr(self.datasafe, 'checksum'))
        self.assertTrue(callable(self.datasafe.checksum))

    def test_has_moveto_method(self):
        self.assertTrue(hasattr(self.datasafe, 'moveto'))
        self.assertTrue(callable(self.datasafe.moveto))

    def test_index_returns_dict(self):
        returnvalue = self.datasafe.index()
        self.assertTrue(type(returnvalue) == dict)

    def test_call_index_with_parameters(self):
        self.datasafe.index("loi")

