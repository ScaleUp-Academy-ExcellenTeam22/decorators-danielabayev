from functools import wraps


def type_check(correct_type):
    """
    This is a decorator which gets a parameter.
    :param correct_type: The type the function gets.
    """
    def wrap(func):
        """
        Wrapper to get the function.
        :param func: The function the decorator wraps.
        """
        @wraps(func)
        def wrapped_f(*args):
            """
            The function parameters.
            :param args: The function parameters.
            """
            if isinstance(type(correct_type), type(*args)):
                func(*args)
            else:
                raise Exception(f"this is not the right type - please call the function with type {correct_type}.\n"
                                f"for your convenience here is the documentation of the function: {func.__doc__}")

        return wrapped_f

    return wrap


@type_check(int)
def times2(num: int) -> int:
    """
    This function gets a number and return the number*2.
    :param num: number.
    :return: number multiply by 2.
    """
    return num*2


if __name__ == "__main__":
    times2(2)
    times2("2")
