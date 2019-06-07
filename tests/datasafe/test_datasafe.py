import unittest
import os
from pathlib import Path
import shutil

import labinform.datasafe.datasafe as datasafe


class TestDatasafe(unittest.TestCase):
    def setUp(self):
        self.datasafe = datasafe.Datasafe()

    def test_instantiate_class(self):
        pass

    def test_has_generate_method(self):
        self.assertTrue(hasattr(self.datasafe, 'generate'))
        self.assertTrue(callable(self.datasafe.generate))

    @unittest.skip
    def test_call_generate_with_parameters(self):
        self.datasafe.generate("cwepr", "sa42")

    @unittest.skip
    def test_generate_returns_loi(self):
        loi = self.datasafe.generate("cwepr", "sa42")
        self.assertEqual("42.1001/ds/cwepr/sa42/2/data/raw", loi)

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
        self.assertTrue(hasattr(self.datasafe, 'set_path'))
        self.assertTrue(callable(self.datasafe.set_path))

    def test_call_set_path_with_parameters(self):
        try:
            self.datasafe.set_path("")
        except datasafe.NoSuchDirectoryError:
            pass

    def test_has_verify_path_method(self):
        self.assertTrue(hasattr(self.datasafe, 'verify_path'))
        self.assertTrue(callable(self.datasafe.verify_path))

    def test_call_verify_path_with_parameters(self):
        self.datasafe.verify_path("")

    def test_verify_path_returns_bool(self):
        path_okay = self.datasafe.verify_path("")
        self.assertEqual(bool, type(path_okay))

    def test_has_verify_own_path(self):
        self.assertTrue(hasattr(self.datasafe, 'verify_own_path'))
        self.assertTrue(callable(self.datasafe.verify_own_path))

    def test_verify_own_path_returns_bool(self):
        path_okay = self.datasafe.verify_own_path()
        self.assertEqual(bool, type(path_okay))

    def test_has_loi_to_path_method(self):
        self.assertTrue(hasattr(self.datasafe, 'loi_to_path'))
        self.assertTrue(callable(self.datasafe.loi_to_path))

    def test_call_loi_to_path_with_parameters(self):
        self.datasafe.loi_to_path("42.1001/ds/cwepr/sa42/01/data/raw")

    def test_has_add_directory_method(self):
        self.assertTrue(hasattr(self.datasafe, 'add_directory'))
        self.assertTrue(callable(self.datasafe.add_directory))

    @unittest.skip
    def test_call_add_directory_with_parameters(self):
        top_level_directory = os.path.dirname(os.path.dirname(os.path.dirname(
            os.path.dirname(__file__))))
        self.target_directory = top_level_directory + "/datasafe-test/ds"
        if not os.path.exists(self.target_directory):
            os.makedirs(self.target_directory)
        self.datasafe.set_path(self.target_directory)
        self.datasafe.add_directory(self.datasafe.path + "cwepr")

    def test_has_dir_empty_method(self):
        self.assertTrue(hasattr(self.datasafe, 'dir_empty'))
        self.assertTrue(callable(self.datasafe.dir_empty))

    def test_call_dir_empty_with_parameters(self):
        self.datasafe.dir_empty(os.path.dirname(__file__))

    def test_dir_empty_returns_bool(self):
        dir_empty = self.datasafe.dir_empty(os.path.dirname(__file__))
        self.assertEqual(bool, type(dir_empty))

    def test_has_increment_method(self):
        self.assertTrue(hasattr(self.datasafe, 'increment'))
        self.assertTrue(callable(self.datasafe.increment))

    def test_call_increment_with_parameters(self):
        self.datasafe.increment(1)

    def test_increment_returns_int(self):
        incremented = self.datasafe.increment(1)
        self.assertEqual(int, type(incremented))

    def test_has_find_highest_method(self):
        self.assertTrue(hasattr(self.datasafe, 'find_highest'))
        self.assertTrue(callable(self.datasafe.find_highest))

    def test_call_find_highest_with_parameters(self):
        try:
            self.datasafe.find_highest("")
        except datasafe.NoSuchDirectoryError:
            pass

    #def test_find_highest_returns_int(self):
    #    highest = self.datasafe.find_highest("")
    #    self.assertEqual(int, type(highest))

    def test_has_has_dir_method(self):
        self.assertTrue(hasattr(self.datasafe, 'has_dir'))
        self.assertTrue(callable(self.datasafe.has_dir))

    def test_call_has_dir_with_parameters(self):
        self.datasafe.has_dir("")

    def test_has_dir_returns_bool(self):
        hasdir = self.datasafe.has_dir("")
        self.assertEqual(bool, type(hasdir))


class TestEmptyDir(unittest.TestCase):
    def setUp(self):
        self.datasafe = datasafe.Datasafe()

    def tearDown(self):
        pass

    def test_dir_empty_on_non_empty_dir(self):
        path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        dir_empty = self.datasafe.dir_empty(path)
        self.assertEqual(False, dir_empty)

    def test_has_dir_on_real_dir(self):
        path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        hasdir = self.datasafe.has_dir(path)
        self.assertEqual(True, hasdir)

    def test_has_dir_fail(self):
        hasdir = self.datasafe.has_dir("")
        self.assertEqual(False, hasdir)


class TestGenerate(unittest.TestCase):
    def setUp(self):
        self.datasafe = datasafe.Datasafe()
        top_level_directory = os.path.dirname(os.path.dirname(os.path.dirname(
            os.path.dirname(__file__))))
        self.target_directory = top_level_directory + "/datasafe-test/ds"
        if not os.path.exists(self.target_directory):
            os.makedirs(self.target_directory)
        self.datasafe.set_path(self.target_directory)

    def tearDown(self):
        shutil.rmtree(self.target_directory)

    def test_increment(self):
        incremented = self.datasafe.increment(1)
        self.assertEqual(2, incremented)

    def test_generate(self):
        expected_loi = "42.1001/ds/cwepr/sa42/1/data/raw"
        real_loi = self.datasafe.generate(experiment="cwepr", sample_id="sa42")
        self.assertEqual(expected_loi, real_loi)
        path_complete = os.path.join(self.datasafe.path, "cwepr/sa42/1/data/raw")
        self.assertTrue(os.path.isdir(path_complete))


class TestSetPath(unittest.TestCase):
    def setUp(self):
        self.datasafe = datasafe.Datasafe()
        top_level_directory = os.path.dirname(os.path.dirname(os.path.dirname(
            os.path.dirname(__file__))))
        self.target_directory = top_level_directory + "/datasafe-test/ds"
        if not os.path.exists(self.target_directory):
            os.makedirs(self.target_directory)

    def tearDown(self):
        shutil.rmtree(self.target_directory)

    def test_set_path(self):
        self.datasafe.set_path(self.target_directory)
        self.assertEqual(True, hasattr(self.datasafe, 'path'))
        self.assertEqual(str, type(self.datasafe.path))

    def test_set_path_raises_error_for_incorrect_path(self):
        with self.assertRaises(datasafe.NoSuchDirectoryError):
            self.datasafe.set_path("")


class TestPathManipulation(unittest.TestCase):
    def setUp(self):
        self.datasafe = datasafe.Datasafe()
        top_level_directory = os.path.dirname(os.path.dirname(os.path.dirname(
            os.path.dirname(__file__))))
        self.target_directory = top_level_directory + "/datasafe-test/ds"
        if not os.path.exists(self.target_directory):
            os.makedirs(self.target_directory)

    def tearDown(self):
        shutil.rmtree(self.target_directory)

    def test_verify_path_returns_false_for_incorrect_path(self):
        path_okay = self.datasafe.verify_path("")
        self.assertEqual(False, path_okay)

    def test_verify_path_returns_true_for_correct_path(self):
        datasafe_path = self.target_directory
        path_okay = self.datasafe.verify_path(datasafe_path)
        self.assertEqual(True, path_okay)

    def test_verify_own_path_returns_false_when_path_not_set(self):
        path_okay = self.datasafe.verify_own_path()
        self.assertEqual(False, path_okay)

    def test_verify_own_path_returns_true_when_path_is_set(self):
        self.datasafe.set_path(self.target_directory)
        path_okay = self.datasafe.verify_own_path()
        self.assertEqual(True, path_okay)


class TestLoiToPath(unittest.TestCase):
    def setUp(self):
        self.datasafe = datasafe.Datasafe()
        top_level_directory = os.path.dirname(os.path.dirname(os.path.dirname(
            os.path.dirname(__file__))))
        self.target_directory = top_level_directory + "/datasafe-test/ds"
        if not os.path.exists(self.target_directory):
            os.makedirs(self.target_directory)
        self.datasafe.set_path(self.target_directory)

    def tearDown(self):
        shutil.rmtree(self.target_directory)

    def test_correct_path_from_loi(self):
        path_correct = self.target_directory + "/cwepr/sa42/01/data/raw"
        path_experimental = self.datasafe.loi_to_path(
            "42.1001/ds/cwepr/sa42/01/data/raw")
        self.assertEqual(path_correct, path_experimental)

    def test_loi_to_path_raises_error_for_incorrect_loi(self):
        with self.assertRaises(datasafe.IncorrectLoiError):
            self.datasafe.loi_to_path("42.1001//raw")


class TestAddDirectory(unittest.TestCase):
    def setUp(self):
        self.datasafe = datasafe.Datasafe()
        top_level_directory = os.path.dirname(os.path.dirname(os.path.dirname(
            os.path.dirname(__file__))))
        self.target_directory = top_level_directory + "/datasafe-test/ds"
        if not os.path.exists(self.target_directory):
            os.makedirs(self.target_directory)
        self.datasafe.set_path(self.target_directory)

    def tearDown(self):
        shutil.rmtree(self.target_directory)

    def test_directory_is_added(self):
        path_complete = self.datasafe.path + "/cwepr"
        self.datasafe.add_directory(path_complete)
        self.assertTrue(os.path.isdir(path_complete))


class TestFindHighest(unittest.TestCase):
    def setUp(self):
        self.datasafe = datasafe.Datasafe()
        top_level_directory = os.path.dirname(os.path.dirname(os.path.dirname(
            os.path.dirname(__file__))))
        self.target_directory = top_level_directory + "/datasafe-test/ds/1"
        if not os.path.exists(self.target_directory):
            os.makedirs(self.target_directory)
        self.datasafe.set_path(self.target_directory)

    def tearDown(self):
        shutil.rmtree(self.target_directory[:-1])

    def test_find_highest(self):
        highest = self.datasafe.find_highest(self.target_directory[:-1])
        self.assertEqual(1, highest)

