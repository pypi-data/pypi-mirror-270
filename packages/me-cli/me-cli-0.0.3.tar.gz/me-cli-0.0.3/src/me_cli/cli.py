import fire


class Calculator:
    """
    This is a calculator, can be used to solve complex math problems
    """

    def __init__(self, offset: int = 1, other: int = 0) -> None:
        self._offset = offset

    def sum(self, number_1: int, number_2: int) -> int:
        """
        Get the sum of the 2 defined numbers
        :param number_1: Number 1
        :param number_2: Number 2
        :return: int
        """
        return number_1 + number_2 + self._offset


def hello(name: str) -> str:
    """
    Return 'Hello, {name}!'
    :param name: Name of the person
    :return: str
    """
    return f"Hello, {name}!"


def main() -> None:
    fire.Fire({
        "calc": Calculator,
        "hello": hello
    }, name="me")


main()
