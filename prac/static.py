from sum import getSum
class Dog:

    num_of_dogs = 0

    def __init__(self, name = "Unknown"):
        self.name = name

        Dog.num_of_dogs += 1

    @staticmethod
    def getNumOfDogs():
        print("There are currenty {} dogs".format(Dog.num_of_dogs))

def main():
    spot = Dog("Spot")
    doug = Dog("Doug")
    spot.getNumOfDogs()
    doug.getNumOfDogs()
main()

print("The sum is:", getSum(1,2, 3, 4, 5))