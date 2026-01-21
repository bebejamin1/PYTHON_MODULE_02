#! /bin/python3.10

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class Plant:
    def __init__(self, name: str) -> None:

        self.name = name.capitalize()
        self.__age = 0
        self.__watering = 0

    def get_age(self) -> str:
        return (self.__age)

    def set_age(self, value: str) -> None:
        if (value == "wilting"):
            raise PlantError(f"The {self.name} plant is wilting!")
        else:
            self.__age = value

    def get_watering(self) -> str:
        return (self.__watering)

    def set_watering(self, value: str) -> None:
        if (value == "empty"):
            raise WaterError("Not enough water in the tank!")
        else:
            self.__watering = value


def test_error():
    plant = Plant("tomato")
    try:
        print("Testing PlantError...")
        plant.set_age("wilting")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print("")
    try:
        print("Testing WaterError...")
        plant.set_watering("empty")
    except WaterError as e:
        print(f"Caught PlantError: {e}")
    print("")

    print("Testing catching all garden errors...")
    try:
        plant.set_age("wilting")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        plant.set_watering("empty")
    except GardenError as e:
        print(f"Caught a garden error: {e}")


if __name__ == "__main__":
    print(" Custom Garden Errors Demo ".center(50, "=") + "\n")
    test_error()
    print("\n" + "All custom error types work correctly!")
