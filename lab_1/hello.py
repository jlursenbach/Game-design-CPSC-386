"""
Name: Jacob Ursenbach
Date: 20220824
File Purpose: Multiple Hello Functions
"""


def helloworld() -> str:
    """
    @Name: helloworld
    @Description: returns the string "Hello World
    @Param: None
    @return: "Hello World"
    """
    return "Hello World"


def helloname(name: str) -> str:
    """
    @Name: helloname
    @Description: returns a hello world using custom name
    @Parameters:
    @Return: custom str
    """
    return "Hello " + name + "!"


def predefined_list() -> list:
    """
    @Name: helloname
    @Description: returns a hello world using custom name
    @Parameters:
    @Return: custom str
    """
    return [1, 2, 3, 4]


def param_list(*argv) -> list:
    """
    @Name: param_list
    @Description: returns the params as a list
    @Parameters: any amount of items
    @Return: a list
    """
    # defines an empty list
    p_list = []

    # iterates through the parameters and adds them to the list
    for item in argv:
        p_list.append(item)

    return p_list


the_list = [
    "Jacob",
    "Jared",
    "Joshua",
    "Iona",
    "Lyzette",
    "Arlette",
    "Tanner",
    "Octave",
    "Kristina",
    "Vernon",
]


class Calc:

    def __init__(self):
        pass

    def add(self, *addends) -> int:
        """

        :param addends:
        :return:
        """
        sum = 0

        for item in addends:
            sum += item

        return sum

    def sub(self, item1, item2):
        """

        :param item1:
        :param item2:
        :return:
        """
        return item1 - item2

    def mul(self, *mults):
        """

        :param mults:
        :return:
        """
        num = 1

        for item in mults:
            num *= item

        return num

    def div(self, item1, item2):
        """

        :param item1:
        :param item2:
        :return:
        """
        return item1 / item2

    def factorial(self, number: int) -> int:
        """

        :param number:
        :return:
        """
        num = 1
        factorial = 1

        while num <= number:
            num += 1
            factorial = factorial * num

        return factorial

    def recursive_factorial(self, number: int) -> int:
        """

        :param number:
        :return:
        """


    def odd_even(self, number: int) -> str:
        """
        
        :param number:
        :return:
        """
        if number % 2 == 0:
            return "Even"
        else:
            return "Odd"

if __name__ == "__main__":
    print(param_list('a', 'b', 'c', 'd'))
