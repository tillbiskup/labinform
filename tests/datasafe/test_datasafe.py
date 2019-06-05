import unittest
import tempfile
import os

import labinform.datasafe.datasafe as datasafe


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

    def test_call_moveto_with_parameters(self):
        self.datasafe.moveto("", "cwepr", "sa42")

    def test_moveto_returns_bool(self):
        worked = self.datasafe.moveto("", "cwepr", "sa42")
        self.assertEqual(bool, type(worked))

    def test_has_set_path_method(self):
        self.assertTrue(hasattr(self.datasafe, 'setPath'))
        self.assertTrue(callable(self.datasafe.setPath))

    def test_call_set_path_with_parameters(self):
        try:
            self.datasafe.setPath("")
        except datasafe.NoSuchDirectoryError:
            pass

    def test_has_verify_path_method(self):
        self.assertTrue(hasattr(self.datasafe, 'verifyPath'))
        self.assertTrue(callable(self.datasafe.verifyPath))

    def test_call_verify_path_with_parameters(self):
        self.datasafe.verifyPath("")

    def test_verify_path_returns_bool(self):
        pathOkay = self.datasafe.verifyPath("")
        self.assertEqual(bool, type(pathOkay))

    def test_has_verify_own_path(self):
        self.assertTrue(hasattr(self.datasafe, 'verifyOwnPath'))
        self.assertTrue(callable(self.datasafe.verifyOwnPath))

    def test_verify_own_path_returns_bool(self):
        pathOkay = self.datasafe.verifyOwnPath()
        self.assertEqual(bool, type(pathOkay))

    def test_has_loi_to_path_method(self):
        self.assertTrue(hasattr(self.datasafe, 'loiToPath'))
        self.assertTrue(callable(self.datasafe.loiToPath))

    def test_call_loi_to_path_with_parameters(self):
        self.datasafe.loiToPath("42.1001/ds/cwepr/sa42/01/data/raw")

    def test_has_add_directory_method(self):
        self.assertTrue(hasattr(self.datasafe, 'addDirectory'))
        self.assertTrue(callable(self.datasafe.addDirectory))

    def test_call_add_directory_with_parameters(self):
        target_directory = "/home/kirchner/nas/Praktikum/datasafe-test"
        temp_dir = tempfile.TemporaryDirectory(dir=target_directory)
        datasafe_path = temp_dir.name
        self.datasafe.setPath(datasafe_path)
        self.datasafe.addDirectory(self.datasafe.path + "cwepr")

    #def test_has_dir_empty_method(self):


class TestGenerate(unittest.TestCase):
    def setUp(self):
        self.datasafe = datasafe.Datasafe()
        #self.path =


class TestSetPath(unittest.TestCase):
    def setUp(self):
        self.datasafe = datasafe.Datasafe()

    def tearDown(self):
        pass

    def test_set_path(self):
        target_directory = "/home/kirchner/nas/Praktikum/datasafe-test"
        temp_dir = tempfile.TemporaryDirectory(dir=target_directory)
        datasafe_path = temp_dir.name
        self.datasafe.setPath(datasafe_path)
        self.assertEqual(True, hasattr(self.datasafe, 'path'))
        self.assertEqual(str, type(self.datasafe.path))

    def test_set_path_raises_error_for_incorrect_path(self):
        with self.assertRaises(datasafe.NoSuchDirectoryError):
            self.datasafe.setPath("")


class TestVerifyPath(unittest.TestCase):
    def setUp(self):
        self.datasafe = datasafe.Datasafe()

    def tearDown(self):
        pass

    def test_verify_path_returns_false_for_incorrect_path(self):
        pathOkay = self.datasafe.verifyPath("")
        self.assertEqual(False, pathOkay)

    def test_verify_path_returns_true_for_correct_path(self):
        target_directory = "/home/kirchner/nas/Praktikum/datasafe-test"
        temp_dir = tempfile.TemporaryDirectory(dir=target_directory)
        datasafe_path = temp_dir.name
        pathOkay = self.datasafe.verifyPath(datasafe_path)
        self.assertEqual(True, pathOkay)

    def test_verify_own_path_returns_false_when_path_not_set(self):
        pathOkay = self.datasafe.verifyOwnPath()
        self.assertEqual(False, pathOkay)

    def test_verify_own_path_returns_true_when_path_is_set(self):
        target_directory = "/home/kirchner/nas/Praktikum/datasafe-test"
        temp_dir = tempfile.TemporaryDirectory(dir=target_directory)
        datasafe_path = temp_dir.name
        self.datasafe.setPath(datasafe_path)
        pathOkay = self.datasafe.verifyOwnPath()
        self.assertEqual(True, pathOkay)


class TestLoiToPath(unittest.TestCase):
    def setUp(self):
        self.datasafe = datasafe.Datasafe()
        target_directory = "/home/kirchner/nas/Praktikum/datasafe-test"
        temp_dir = tempfile.TemporaryDirectory(dir=target_directory)
        self.datasafe_path = temp_dir.name
        self.datasafe.setPath(self.datasafe_path)

    def tearDown(self):
        pass

    def test_correct_path_from_loi(self):
        path_correct = self.datasafe_path + "/cwepr/sa42/01/data/raw"
        path_experimental = self.datasafe.loiToPath("42.1001/ds/cwepr/sa42/01/data/raw")
        self.assertEqual(path_correct, path_experimental)

    def test_loi_to_path_raises_error_for_incorrect_loi(self):
        with self.assertRaises(datasafe.IncorrectLoiError):
            self.datasafe.loiToPath("42.1001//raw")


class TestAddDirectory(unittest.TestCase):
    def setUp(self):
        self.datasafe = datasafe.Datasafe()
        target_directory = "/home/kirchner/nas/Praktikum/datasafe-test"
        temp_dir = tempfile.TemporaryDirectory(dir=target_directory)
        self.datasafe_path = temp_dir.name
        self.datasafe.setPath(self.datasafe_path)

    def tearDown(self):
        pass

    def test_directory_is_added(self):
        path_complete = self.datasafe.path + "cwepr"
        self.datasafe.addDirectory(path_complete)
        self.assertTrue(os.path.isdir(path_complete))








