def surprise(func: callable):
    """
    A decorator gets a function and prints surprise instead.
    :param func: A function.
    """
    def wrapper(*args, **kwargs):
        """A wrapper function"""
        print("surprise!")
    return wrapper


# @surprise
def some_function():
    """
    This function is for debugging.
    """
    print("Hi there.")


if __name__ == "__main__":
    some_function()
