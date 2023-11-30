from unittest import TestCase
import os
from tools.file_utils import file_exists

class TestFileUtils(TestCase):
    def setUp(self):
        # Prepare a file for testing
        self.existing_file = "test_file.txt"
        with open(self.existing_file, "w") as f:
            f.write("Some content")

    def tearDown(self):
        # Clean after tests
        try:
            os.remove(self.existing_file)
        except OSError:
            pass

    def test_file_exists_true_for_existing_file(self):
        self.assertTrue(file_exists(self.existing_file))

    def test_file_exists_false_for_nonexistent_file(self):
        self.assertFalse(file_exists("nonexistent.txt"))
