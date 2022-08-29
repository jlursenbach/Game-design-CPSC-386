"""
Name: Jacobu Ursenbach
Date: 20220824
File Purpose: Multiple Hello Functions
"""

# imports everything from hello.py
from hello import *


def main():
    """
    :Name: main
    :Description:
    :Param:
    :Return: None
    """

    print("****** TITAN Hello Program ******")

    #
    print(helloworld())

    # provides the name argument
    # helloname is in hello.py
    # imported above
    print(helloname("Jacob"))

    # pulls the_list from hello.py
    # iterates through each item
    # prints each item
    # NOTE: 'item' is not a keyword
    for item in the_list:
        print(item)


if __name__ == "__main__":
    main()
