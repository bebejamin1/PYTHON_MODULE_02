#! /bin/python3.10

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class ValueError(GardenError):
    pass


class GardenManager:
    """Manage a garden with multiple plants.

    Tracks plant health, water levels, sunlight exposure, and errors.

    Attributes:
        error_save (list): Class attribute to store error messages.
        name (str): The name of the plant.
        water_level (int): The water level (1-10).
        sun_hours (int): Daily sunlight hours (2-12).
    """

    error_save = []

    def __init__(self, name: str, water_level: int, sun_hours: int) -> None:
        """Initialize a new plant in the garden.

        Args:
            name (str): The name of the plant.
            water_level (int): The water level for the plant.
            sun_hours (int): Daily sunlight hours needed.

        Raises:
            PlantError: If the plant name is empty or None.
        """
        try:
            if (name == "" or name is None):
                raise PlantError("Error adding plant: "
                                 "Plant name cannot be empty!")
        except PlantError as e:
            print(e)
        else:
            self.name = name.capitalize()
            self.water_level = water_level
            self.sun_hours = sun_hours
            print(f"Added {name} successfully")

    def check_plant(self) -> None:
        """Check the health of the plant.

        Validates water level and sunlight hours against acceptable ranges
        and stores any errors for later recovery handling.
        """
        if (self.water_level < 1 or self.water_level > 10 or
                self.sun_hours < 2 or self.sun_hours > 12):
            try:
                if (self.water_level < 1):
                    GardenManager.error_save.append(f"{self.name} "
                                                    "not enough water in tank")
                    raise ValueError(f"water level {self.water_level} "
                                     "is too low (min 1)")
                if (self.water_level > 10):
                    GardenManager.error_save.append(f"{self.name} too much "
                                                    "water in the tank")
                    raise ValueError(f"water level {self.water_level} "
                                     "is too high (max 10)")
            except ValueError as e:
                print(f"Error checking {self.name}: {e}")

            try:
                if (self.sun_hours < 2):
                    GardenManager.error_save.append(f"{self.name} "
                                                    "not enough sunlight")
                    raise ValueError(f"sunlight hours {self.sun_hours} "
                                     "is too low (min 2)")
                if (self.sun_hours > 12):
                    GardenManager.error_save.append(f"{self.name} "
                                                    "too much sun")
                    raise ValueError(f"sunlight hours {self.sun_hours} "
                                     "is too high (max 12)")
            except ValueError as e:
                print(f"Error checking {self.name}: {e}")
        else:
            print(f"{self.name}: healthy (water: "
                  f"{self.water_level}, sun: {self.sun_hours})")

    def print_error_and_recovery(self) -> None:
        """Print stored errors and recover plant parameters to safe values.

        Removes and prints all errors from the error_save list and adjusts
        water_level and sun_hours to be within acceptable ranges.
        """
        while len(GardenManager.error_save) > 0:
            error = GardenManager.error_save.pop(0)
            print(f"Caught GardenError: {error}")
        if (self.water_level > 10):
            self.water_level = 10
        elif (self.water_level < 1):
            self.water_level = 1
        if (self.sun_hours > 12):
            self.sun_hours = 12
        elif (self.sun_hours < 2):
            self.sun_hours = 2

    def watering_garden(self) -> None:
        """Water the plant.

        Prints a success message indicating the plant has been watered.
        """
        print(f"Watering {self.name} - success")


def test_garden_management() -> None:
    """Test the complete garden management system.

    Tests plant initialization, watering, health checking, and
    error recovery procedures.
    """
    print("Adding plants to garden...")
    flower1 = GardenManager("tomato", 5, 8)
    flower2 = GardenManager("lettuce", 15, 5)
    _ = GardenManager("", 5, 5)

    print("\n" + "Watering plants...")
    print("Opening watering system")
    flower1.watering_garden()
    flower2.watering_garden()
    print("Closing watering system (cleanup)" + "\n")

    print("Checking plant health...")
    flower1.check_plant()
    flower2.check_plant()

    print("\n" + "Testing error recovery...")
    flower1.print_error_and_recovery()
    flower2.print_error_and_recovery()
    print("System recovered and continuing...")


if __name__ == "__main__":
    print(" Garden Management System ".center(40, "=") + "\n")
    test_garden_management()
    print("\n" + "Garden management system test complete!")
