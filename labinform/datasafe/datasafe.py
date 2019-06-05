import os


class Error(Exception):
    """
    Base class for exceptions in this module.
    """
    pass


class NoSuchDirectoryError(Error):
    """
    Raised when an invalid path is set.
    """
    pass


class IncorrectLoiError(Error):
    """
    Raised when an incorrect loi is provided.
    """
    pass


class Datasafe:
    """Data handler for moving data in the context of a
    datasafe.

    The operations performed include generation of a directory structure,
    storing data in and retrieving data from these directories as well
    verifying the integrity of and providing general information about the
    data stored.
    """
    def __init__(self):
        self.path = ""

    def setPath(self, path=""):
        """Sets the path of the datasafe's toplevel directory.

        :param path: The path that should be set as the instance attribute.
        """
        print(path)
        if not self.verifyPath(path):
            raise NoSuchDirectoryError
        self.path = path

    def verifyPath(self, path=""):
        """Verifies if a path is correct.

        :param path: path that should be checked
        :return: result of the path check
        """
        return os.path.isdir(path)

    def verifyOwnPath(self):
        """Verifies if the path set as instance attribute is a correct path.

        :return: result of the path check
        """
        return self.verifyPath(self.path)

    def loiToPath(self, loi=""):
        """Retrieves the a file's datasafe directory path from the
        corresponding loi.

        :param loi: loi for which the path should be retrieved
        :return: path of the file
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

    def addDirectory(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def generate(self, experiment="", sample_id=""):
        """Generate directory structure and return identifier.

        This method will verify to what extent the relevant directory structure
        is present and create directories as required. In this context the
        measurement number for a given sample is - in case of consecutive
        measurements - automatically increased.

        Finally the method will return a unique identifier for the respective
        measurement and sample, including the directory path.

        :param experiment: type of experiment performed, e.g. cwepr
        :param sample_id: unique identifier for the sample measured
        :return: unique loi including the information provided
        """
        loi_basic = "42.1001/ds/"

        return "42.1001/ds/cwepr/sa42/01/data/raw"

    def push(self, data="", loi=""):
        """Move data inside the datasafe.

        Before moving the existence of the target directory (as specified in
        the loi) as well as its emptiness are verified.

        :param data: data (file) to be moved
        :param loi: unique identifier providing the target directory
        """
        pass

    def pull(self, loi=""):
        """Retrieve data from the datasafe.

        Retrieves data from the datasafe if present at the target directory
        (as specified in the loi), raises an exception otherwise.

        :param loi: identifier for the data (file) to be retrieved
        :return: retrieved data
        """
        return str()

    def index(self, loi=""):
        """Retrieve background information from the datasafe.

        Retrieves background information (manifest.yaml file) from the datasafe
        if present at the target directory (as specified in the loi), raises
        an exception otherwise.

        :param loi: identifier for the data (file) for which the background
         information should be retrieved
        :return: background information (manifest.yaml) as dict
        """
        return dict()

    def checksum(self, loi=""):
        """Create a checksum (MD5) for a file in the datasafe.

        Creates a checksum for a file in the datasafe if present at the target
        directory (as specified in the loi), raises an exception otherwise.

        :param loi: identifier for the data (file) for which the checksum
        should be created
        :return: checksum (MD5)
        """
        return str()

    def moveto(self, data="", experiment="", sample=""):
        """Wrapper function including all operations necessary for moving data
        to the datasafe.

        Calls :method:`generate` to generate a directory structure if
        necessary and creates a local checksum of the file to be moved.
        Then moves the file to the datasafe, creates another checksum.
        The two checksums are compared and the result of the comparation is
        returned.

        :return: result of the checksum comparation
        """
        return True

