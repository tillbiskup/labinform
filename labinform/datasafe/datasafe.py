"""Datasafe module for the labinform package.

The datasafe is a key feature of labinform which serves to safely store data.
Functionality includes directory generation and checksum creation.
"""

import os


class Error(Exception):
    """Base class for exceptions in this module."""

    pass


class NoSuchDirectoryError(Error):
    """Raised when an invalid path is set."""

    pass


class IncorrectLoiError(Error):
    """Raised when an incorrect loi is provided."""

    pass


class DirNamesAreNotIntsError(Error):
    """Raised when it is tried to increment non numeric dir names."""


class Datasafe:
    """Data handler for moving data in the context of a datasafe.

    The operations performed include generation of a directory structure,
    storing data in and retrieving data from these directories as well
    verifying the integrity of and providing general information about the
    data stored.
    """

    def __init__(self):
        self.path = ""

    def set_path(self, path=""):
        """Set the path of the datasafe's top level directory.

        The directory is set as path if it exists.

        Parameters
        ----------
        path: :class: `str`
            The path that should be set as the instance attribute.

        """
        if not self.verify_path(path):
            raise NoSuchDirectoryError
        self.path = path

    @staticmethod
    def verify_path(path=""):
        """Verify if a path is correct.

        Static method which works for any path not just the datasafe root
        path.

        Parameters
        ----------
        path: :class: `str`
            path that should be checked

        Returns
        -------
        path_okay: :class: `bool`
            result opf the path check

        """
        path_okay = os.path.isdir(path)
        return path_okay

    def verify_own_path(self):
        """Verify if the path set as instance attribute is a correct path.

        Wrapper around :method: `verify_path` specifically for checking the
        root path of the datasafe.

        Returns
        -------
        path_okay: :class: `bool`
            result opf the path check

        """
        path_okay = self.verify_path(self.path)
        return path_okay

    def loi_to_path(self, loi=""):
        """Retrieve the a file's datasafe directory path from the data's loi.

        Retrieves the data's path (relative to the datasafe's root path) which
        is included in the loi. If the loi is not correctly formatted, an
        exception is raised.

        Parameters
        ----------
        loi: :class: `str`
            loi from which the path should be retrieved

        Returns
        -------
        path: :class: `str`
            path retrieved from the loi

        """
        path = self.path
        loi_parts = loi.split("/")
        if len(loi_parts) != 7:
            raise IncorrectLoiError
        loi_parts_useful = loi_parts[2:]
        for part in loi_parts_useful:
            path += "/"
            path += part
        return path

    def add_directory(self, path):
        """Create a directory at a specified path

        Parameters
        ----------
        path: :class: `str`
            path of the directory that should be created

        """
        if not os.path.exists(path):
            os.makedirs(path)

    @staticmethod
    def dir_empty(path=""):
        """Check whether a directory is empty.

        Parameters
        ----------
        path: :class: `str`
            path of the directory which should be checked

        """
        try:
            dir_content = os.listdir(path)
        except FileNotFoundError:
            raise NoSuchDirectoryError
        return dir_content == list()

    @staticmethod
    def has_dir(path=""):
        has_dir = os.path.isdir(path)
        return has_dir

    @staticmethod
    def increment(number=0):
        """Increment an integer by one.

        Parameters
        ----------
        number: :class: `int`
            integer that should be incremented

        """
        incremented = number + 1
        return incremented

    @staticmethod
    def find_highest(path=""):
        """Find a numbered directory with the highest number.

        For a given path, find the numbered directory (i.e. directory with an
        integer as name) with the highest number. If the directory that the
        path leads to doesn't exist, if it is empty or if the subdirectories
        are not 'numbered' an error is raised.

        ..Todo: What happens, when there are 'numbered' _files_ in the dir?

        Parameters
        ----------
        path: :class: `str`
            path of the directory that should be searched

        """
        try:
            dir_content = os.listdir(path)
        except FileNotFoundError:
            raise NoSuchDirectoryError
        dir_names = list()
        for entry in dir_content:
            try:
                dir_name = int(entry)
                dir_names.append(dir_name)
            except ValueError:
                pass
        if dir_names == list():
            return 0
            #raise DirNamesAreNotIntsError
        else:
            highest = max(dir_names)
            return highest

    def generate(self, experiment="", sample_id=""):
        """Generate directory structure and return identifier.

        This method will verify to what extent the relevant directory structure
        is present and create directories as required. In this context the
        measurement number for a given sample is - in case of consecutive
        measurements - automatically increased.

        Finally the method will return a unique identifier for the respective
        measurement and sample, including the directory path.


        Parameters
        ----------
        experiment: :class: `str`
            type of experiment performed, e.g. 'cwepr'
        sample_id: :class: `str`
            unique identifier for the sample measured

        Returns
        -------
        loi: :class: `str`
            unique loi including the information provided

        """
        loi_basic = "42.1001/ds/"
        path_for_loi = str()
        path_for_loi = os.path.join(path_for_loi, experiment)
        dir_path = os.path.join(self.path, path_for_loi)
        if not self.has_dir(dir_path):
            self.add_directory(dir_path)
        path_for_loi = os.path.join(path_for_loi, sample_id)
        dir_path = os.path.join(self.path, path_for_loi)
        if not self.has_dir(dir_path):
            self.add_directory(dir_path)
        if self.dir_empty(dir_path):
            path_for_loi = os.path.join(path_for_loi, "1")
            dir_path = os.path.join(self.path, path_for_loi)
        else:
            number = str(self.increment(self.find_highest(dir_path)))
            path_for_loi = os.path.join(path_for_loi, number)
            dir_path = os.path.join(self.path, path_for_loi)
        if not self.has_dir(dir_path):
            self.add_directory(dir_path)
        path_for_loi = os.path.join(path_for_loi, "data")
        dir_path = os.path.join(self.path, path_for_loi)
        if not self.has_dir(dir_path):
            self.add_directory(dir_path)
        path_for_loi = os.path.join(path_for_loi, "raw")
        dir_path = os.path.join(self.path, path_for_loi)
        if not self.has_dir(dir_path):
            self.add_directory(dir_path)
        #print(dir_path)
        loi_complete = loi_basic + path_for_loi
        return loi_complete

    def push(self, data="", loi=""):
        """Move data inside the datasafe.

        Before moving the existence of the target directory (as specified in
        the loi) as well as its emptiness are verified.

        Parameters
        ----------
        data: :class: `str`
            data (file) to be moved
        loi: :class: `str`
            unique identifier providing a directory path

        """
        pass

    def pull(self, loi=""):
        """Retrieve data from the datasafe.

        Retrieves data from the datasafe if present at the target directory
        (as specified in the loi), raises an exception otherwise.

        Parameters
        ----------
        loi: :class: `str`
            unique identifier for the data to be retrieved

        Returns
        -------
        xxxxxx: :class: `str`
            retrieved data

        """
        return str()

    def index(self, loi=""):
        """Retrieve background information from the datasafe.

        Retrieves background information (manifest.yaml file) from the datasafe
        if present at the target directory (as specified in the loi), raises
        an exception otherwise.

        Parameters
        ----------
        loi: :class: `str`
            unique identifier for the data for which the background information
            should be retrieved.

        Returns
        -------
        xxxxxx: :class: `str`
            retrieved background information (manifest.yaml) as dict

        """
        return dict()

    def checksum(self, loi=""):
        """Create a cryptographic hash (MD5) for a file in the datasafe.

        Creates a checksum for a file in the datasafe if present at the target
        directory (as specified in the loi), raises an exception otherwise.

        Parameters
        ----------
        loi: :class: `str`
            unique identifier for the data (file) for which a checksum should
            be created

        Returns
        -------
        xxxxxx: :class: `str`
            checksum (MD5)

        """
        return str()

    def moveto(self, data="", experiment="", sample_id=""):
        """Prepare directory and move data there.

        This is a wrapper function which calls :method:`generate` to generate
        a directory structure if necessary and creates a local checksum of
        the file to be moved. Then moves the file to the datasafe, creates
        another checksum.
        The two checksums are compared and the result of the comparison is
        returned.

        Parameters
        ----------
        data: :class: `str`
            data (file) that should be moved inside the datasafe.
        experiment: :class: `str`
            type of experiment performed, e.g. 'cwepr'
        sample_id: :class: `str`
            unique identifier for the sample measured

        Returns
        -------
        xxxxx: :class: `bool`
            result of the checksum comparison

        """
        return True
