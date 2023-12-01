import os
from unittest import TestCase

from tools.mower_utils import valid_lawn_coordinates, valid_instructions, valid_mower_position, process_mowing, process_instructions_file


class TestMowerUtils(TestCase):

    def setUp(self):
        # Prepare files for testing
        self.empty_file = "empty_file.txt"
        self.invalid_file = "invalid_file.txt"
        open(self.empty_file, 'w').close()
        data = ["5 5", "1 2 N", "GAGAGAGAA", "3 3 E"]
        with open(self.invalid_file, 'w') as file:
            for line in data:
                file.write(line + '\n')

    def tearDown(self):
        # Clean after tests
        try:
            os.remove(self.empty_file)
            os.remove(self.invalid_file)
        except OSError:
            pass

    def test_lawn_coordinates_returns_false_when_empty_value(self):
        valid, message = valid_lawn_coordinates("")
        self.assertFalse(valid)
        self.assertEqual(message, "Invalid lawn coordinates : It must be in the form of 2 numbers.")

    def test_lawn_coordinates_returns_false_when_blanc_value(self):
        valid, message = valid_lawn_coordinates("  ")
        self.assertFalse(valid)
        self.assertEqual(message, "Invalid lawn coordinates   : It must be in the form of 2 numbers.")

    def test_lawn_coordinates_returns_false_when_two_zeros(self):
        valid, message = valid_lawn_coordinates("0 0")
        self.assertFalse(valid)
        self.assertEqual(message, "Invalid lawn coordinates 0 0: The lawn should be a valid rectangle and not a point.")

    def test_lawn_coordinates_returns_false_when_invalid_number_value(self):
        valid, message = valid_lawn_coordinates("5 5 5")
        self.assertFalse(valid)
        self.assertEqual(message, "Invalid lawn coordinates 5 5 5: It must be in the form of 2 numbers.")

    def test_lawn_coordinates_returns_false_when_invalid_alphanum_value(self):
        valid, message = valid_lawn_coordinates("5 N")
        self.assertFalse(valid)
        self.assertEqual(message, "Invalid lawn coordinates 5 N: It must be in the form of 2 numbers.")

    def test_lawn_coordinates_returns_true_when_valid_value(self):
        valid = valid_lawn_coordinates("5 5")
        self.assertTrue(valid)

    def test_valid_position_returns_false_when_empty_value(self):
        valid, message = valid_mower_position("", 5, 5)
        self.assertFalse(valid)
        self.assertEqual(message, f"Invalid position : The initial position and orientation of the mower must be in "
                                  f"the form of 2 numbers and one of these letters [N, S, E, W], separated by a space.")

    def test_valid_position_returns_false_when_blanc_value(self):
        valid, message = valid_mower_position("  ", 5, 5)
        self.assertFalse(valid)
        self.assertEqual(message, f"Invalid position   : The initial position and orientation of the mower must be in "
                                  f"the form of 2 numbers and one of these letters [N, S, E, W], separated by a space.")

    def test_valid_position_returns_false_when_no_orientation(self):
        valid, message = valid_mower_position("1 2 3", 5, 5)
        self.assertFalse(valid)
        self.assertEqual(message, f"Invalid position 1 2 3: The initial position and orientation of the mower must be "
                                  f"in the form of 2 numbers and one of these letters [N, S, E, W], separated by a "
                                  f"space.")

    def test_valid_position_returns_false_when_invalid_orientation_pos(self):
        valid, message = valid_mower_position("1 N 2", 5, 5)
        self.assertFalse(valid)
        self.assertEqual(message, f"Invalid position 1 N 2: The initial position and orientation of the mower must be "
                                  f"in the form of 2 numbers and one of these letters [N, S, E, W], separated by a "
                                  f"space.")

    def test_valid_position_returns_false_when_too_long_value(self):
        valid, message = valid_mower_position("1 2 N 3", 5, 5)
        self.assertFalse(valid)
        self.assertEqual(message,
                         f"Invalid position 1 2 N 3: The initial position and orientation of the mower must be "
                         f"in the form of 2 numbers and one of these letters [N, S, E, W], separated by a "
                         f"space.")

    def test_valid_position_returns_false_when_invalid_orientation(self):
        valid, message = valid_mower_position("1 2 K", 5, 5)
        self.assertFalse(valid)
        self.assertEqual(message, f"Invalid position 1 2 K: The initial position and orientation of the mower must be "
                                  f"in the form of 2 numbers and one of these letters [N, S, E, W], separated by a "
                                  f"space.")

    def test_valid_position_returns_false_when_invalid_position(self):
        valid, message = valid_mower_position("8 2 N", 5, 5)
        self.assertFalse(valid)
        self.assertEqual(message, f"Invalid position 8 2 N: The initial position (8,2) of the mower should be inside "
                                  f"the lawn (5,5).")

    def test_valid_position_returns_true_when_valid_value(self):
        valid = valid_mower_position("1 2 N", 5, 5)
        self.assertTrue(valid)

    def test_valid_instructions_returns_false_when_empty_value(self):
        valid, message = valid_instructions("")
        self.assertFalse(valid)
        self.assertEqual(message, "Invalid instructions : It must be a string consisting of only 'A', 'G', "
                                  "and 'D' letters.")

    def test_valid_instructions_returns_false_when_blanc_value(self):
        valid, message = valid_instructions("  ")
        self.assertFalse(valid)
        self.assertEqual(message, "Invalid instructions   : It must be a string consisting of only 'A', 'G', "
                                  "and 'D' letters.")

    def test_valid_instructions_returns_false_when_invalid_value(self):
        valid, message = valid_instructions("GAGAGAGAAL")
        self.assertFalse(valid)
        self.assertEqual(message, "Invalid instructions GAGAGAGAAL: It must be a string consisting of only 'A', 'G', "
                                  "and 'D' letters.")

    def test_valid_instructions_returns_true_when_valid_value1(self):
        valid = valid_instructions("AADAADADDA")
        self.assertTrue(valid)

    def test_valid_instructions_returns_true_when_valid_value2(self):
        valid = valid_instructions("GAGAGAGAA")
        self.assertTrue(valid)

    def test_process_mowing_throws_exception_when_no_file(self):
        with self.assertRaisesRegex(Exception, "File not found: test_file.txt."):
            process_mowing("test_file.txt")

    def test_process_mowing_throws_exception_when_empty_file(self):
        with self.assertRaisesRegex(Exception, "Invalid file. The file must contain at least 3 lines."):
            process_mowing("empty_file.txt")

    def test_process_mowing_throws_exception_when_mower_without_instructions(self):
        with self.assertRaisesRegex(Exception, "There is no instructions for Mower in position 3 3 E."):
            process_instructions_file("invalid_file.txt")
