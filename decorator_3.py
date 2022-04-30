import decorator


# I didn't find any useful decorator in search of decorator.decorator.
def double_function(func):
    """
    This decorator gets a function and run it twice.
    :param func: The function to run.
    """
    def wraps(*args, **kwargs):
        return_val = func(*args, **kwargs)
        return_val += func(*args, **kwargs)
    return wraps


@double_function
def squared(number: int) -> int:
    return number * number


if __name__ == "__main__":
    print(squared(3))
