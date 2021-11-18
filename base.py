import sys


# TODO add run with args
def app_runner(argument):
    """
    decorator factory
    wrap decorator
    stuff will need to do pass args into
    :param argument:
    :return:
    """
    def decorator(my_function):
        """
        base entity
        :param my_function:
        :return:
        """
        def wrapper():
            while True:
                try:
                    my_function()
                except KeyboardInterrupt:
                    print("Interrupted")
                    sys.exit(0)
        return wrapper
    return decorator
