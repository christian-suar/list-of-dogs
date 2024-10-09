"""
Module Docstring: main.py
======================

This is the main module of the read/write to file project.
"""

__author__ = "Christian S."
__version__ = "0.1"
__date__ = "Oct. 7th, 2024"
__license__ = "None"

def read_file(file_name) -> None:
    """
    Reads a file and prints it to the console
    """
    with open(file_name, "r") as f:
        for line in f:
            print(line, end="")


def new_file(file_name) -> None:
    """
    Creates a new file and writes data to it, or overwrites an existing file.
    """
    with open(file_name, "w") as f:
        f.write("Maine Coon")

def append_file(file_name, data) -> None:
    """
    Appends data to an existing file.
    """

    with open(file_name, "r") as f:
        lines = f.readlines()

    with open(file_name, "a") as f:
        last_line = lines[-1]
        #print(last_line)
        if not last_line.endswith("\n"):
            f.write("\n")   

        f.write(data)


def main():
    """
    Main entry point of the application
    """
    user_submission=input('Enter Data To Append: ')
    append_file("cats.txt", user_submission)

if __name__ == "__main__":
    """
    Starts the program.
    """
    main()



