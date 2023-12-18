class DogNameError(Exception):

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

try:
    dogName = input("What is your dogs name:")
    if any(char.isdigit() for char in dogName):
        raise DogNameError
except DogNameError:
    print("not a char")
    