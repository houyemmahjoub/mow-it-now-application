# mow-it-now-application

## Introduction
MowItNow application is an automated lawn mower application designed for rectangular surfaces. The application allows programming the mower to traverse the entire surface based on a set of instructions provided in a file.

## Setup
To set up the MowItNow application, ensure you have Python installed on your system. This application is compatible with Python 3.x.

## Running the Application
To run the MowItNow application, use the following command:

```bash
python execute.py inputs/instructions.txt
```
This command will execute the application using the instructions provided in the instructions.txt file located in the inputs directory.

## Instructions Format
The instructions.txt file should be formatted as follows:

* The first line should contain the coordinates of the top-right corner of the lawn, assuming the bottom-left corner is at (0,0).
* The following lines should contain instructions for each mower deployed. Each mower has two lines associated with it:
1. The first line provides the mower's initial position and orientation (format: X Y O, where X and Y are integers, and O a letter indicating the orientation according to English cardinal notation (N,E,W,S).
2. The second line contains a series of instructions telling the mower how to explore the lawn (A for move forward, D for turn right, and G for turn left).
## Testing
To test the application with your input data, you can modify the instructions.txt file or create a new file with the desired instructions. Run the application with the command mentioned above.
