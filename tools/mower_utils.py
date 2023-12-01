import re
from typing import Optional, Tuple
from entities.mower_entity import Mower
from entities.lawn_entity import Lawn
from tools.file_utils import file_exists, count_lines


def valid_mower_position(pos, lawn_x_max, lawn_y_max) -> Tuple[bool, Optional[str]]:
    # Construction of the regex fot the orientation
    orientations = "|".join(["N", "S", "E", "W"])
    regex = r"^\d+ \d+ ({})$".format(orientations)
    if bool(re.match(regex, pos)):
        coordinates = pos.split()
        x = int(coordinates[0])
        y = int(coordinates[1])
        if x > lawn_x_max or y > lawn_y_max:
            return False, (f"Invalid position {pos}: The initial position ({x},{y}) of the mower should be inside "
                           f"the lawn ({lawn_x_max},{lawn_y_max}).")
        else:
            return True, "Valid position."
    else:
        return False, (f"Invalid position {pos}: The initial position and orientation of the mower must be in "
                       f"the form of 2 numbers and one of these letters [N, S, E, W], separated by a space.")


def valid_instructions(inst):
    # Construction of the regex fot the instructions
    instructions = "|".join(["A", "G", "D"])
    regex = r"^({})+$".format(instructions)
    if bool(re.match(regex, inst)):
        return True, "Valid instructions."
    else:
        return False, (f"Invalid instructions {inst}: It must be a string consisting of only 'A', 'G', and 'D' "
                       f"letters.")


def valid_lawn_coordinates(coordinates) -> Tuple[bool, Optional[str]]:
    if coordinates == "0 0":
        return False, "Invalid lawn coordinates 0 0: The lawn should be a valid rectangle and not a point."
    else:
        if bool(re.match(r"^\d+ \d+$", coordinates)):
            return True, "Valid coordinates."
        else:
            return False, f"Invalid lawn coordinates {coordinates}: It must be in the form of 2 numbers."

def process_instructions_file(file_path):
    with open(file_path, 'r') as file:
        first_line = file.readline().strip()  # Read first line
        valid_lawn, message_lawn = valid_lawn_coordinates(first_line)
        if valid_lawn:
            first_line_split = first_line.split()
            lawn = Lawn(int(first_line_split[0]), int(first_line_split[1]))
        else:
            raise Exception(message_lawn)

        # Read the rest of the file
        while True:
            # Read first line
            line1 = file.readline().strip()
            # if line 1 is empty then break, end of file
            if not line1:
                break
            valid_mower, message_mower = valid_mower_position(line1, lawn.x_max, lawn.y_max)
            if valid_mower:
                line1_split = line1.split()
                mower = Mower(int(line1_split[0]), int(line1_split[1]), line1_split[2], lawn)
            else:
                raise Exception(message_mower)

            # Read second line
            line2 = file.readline().strip()
            # if line 1 is not empty and line2 is empty, raise exception
            if not line2:
                raise Exception(f"There is no instructions for Mower in position {line1}.")
            valid_inst, message_inst = valid_instructions(line2)
            if valid_inst:
                mower.move(line2)
                print(str(mower))
            else:
                raise Exception(message_inst)

def process_mowing(file_path):
    if file_exists(file_path):
        if count_lines(file_path) >= 3:
            process_instructions_file(file_path)
        else:
            raise Exception(f"Invalid file. The file must contain at least 3 lines.")
    else:
        raise Exception(f"File not found: {file_path}.")


