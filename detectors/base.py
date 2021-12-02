import sys


# TODO add run with args
def app_runner(my_function):
    def wrapper():
        while True:
            try:
                my_function()
            except KeyboardInterrupt:
                print("Interrupted")
                sys.exit(0)
    return wrapper
