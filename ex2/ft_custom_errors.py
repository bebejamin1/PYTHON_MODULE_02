#! /bin/python3.10

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class Plant:
    """Represent a plant in the garden.

    Attributes:
        name (str): The capitalized name of the plant.
        __age (int): Private attribute storing the age of the plant.
        __watering (int): Private attribute storing watering status.
    """

    def __init__(self, name: str) -> None:
        """Initialize a new plant.

        Args:
            name (str): The name of the plant.
        """
        self.name = name.capitalize()
        self.__age = 0
        self.__watering = 0

    def get_age(self) -> str:
        """Get the age of the plant.

        Returns:
            str: The age of the plant.
        """
        return (self.__age)

    def set_age(self, value: str) -> None:
        """Set the age of the plant.

        Args:
            value (str): The age value to set.

        Raises:
            PlantError: If the value is "wilting".
        """
        if (value == "wilting"):
            raise PlantError(f"The {self.name} plant is wilting!")
        else:
            self.__age = value

    def get_watering(self) -> str:
        """Get the watering level of the plant.

        Returns:
            str: The watering level of the plant.
        """
        return (self.__watering)

    def set_watering(self, value: str) -> None:
        """Set the watering level of the plant.

        Args:
            value (str): The watering value to set.

        Raises:
            WaterError: If the value is "empty".
        """
        if (value == "empty"):
            raise WaterError("Not enough water in the tank!")
        else:
            self.__watering = value


def test_error() -> None:
    """Test custom error handling for plants.

    Tests PlantError, WaterError, and catching all GardenErrors.
    """
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
