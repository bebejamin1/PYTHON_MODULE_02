#! /bin/python3.10

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class SunError(GardenError):
    pass


class Plant:
    def __init__(self, name: str, water_level: int, sun_hours: int) -> None:
        try:
            if name == "" or name is None:
                raise PlantError("Error adding plant: "
                                 "Plant name cannot be empty!")
        except PlantError as e:
            print(e)
        else:
            self.name = name
            self.water_level = water_level
            self.sun_hours = sun_hours
            print(f"Added {self.name} successfully")


class GardenManager:
    error_save = []

    def __init__(self) -> None:
        self.plants = []

    def add_plant(self, plant: Plant) -> None:
        try:
            if plant is None or plant.name is None:
                raise PlantError("Cannot add a None plant!")
            self.plants.append(plant)
        except PlantError as e:
            print(f"Error: {e}")
            GardenManager.error_save.append(str(e))
        finally:
            pass

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant.name} - success")
        finally:
            print("Closing watering system (cleanup)" + "\n")

    def check_plant_health(self) -> None:
        try:
            for plant in self.plants:
                try:
                    if plant.water_level < 1:
                        msg = "Water level is too low (min 1)"
                        raise WaterError(msg)
                    if plant.water_level > 10:
                        msg = "Water level is too high (max 10)"
                        raise WaterError(msg)
                    if plant.sun_hours < 2:
                        msg = "Sunlight hours is too low (min 2)"
                        raise SunError(msg)
                    if plant.sun_hours > 12:
                        msg = "Sunlight hours is too high (max 12)"
                        raise SunError(msg)
                    water = plant.water_level
                    sun = plant.sun_hours
                    print(f"{plant.name}: healthy (water: {water}, "
                          f"sun: {sun})")
                except WaterError as e:
                    print(f"Error checking {plant.name}: {e}")
                    GardenManager.error_save.append(str(e))
                except SunError as e:
                    print(f"Error checking {plant.name}: {e}")
                    GardenManager.error_save.append(str(e))
        finally:
            print()

    def show_errors(self) -> None:
        for error in GardenManager.error_save:
            print(f"Caught GardenError: {error}")


def test_garden_management() -> None:
    try:
        print(" Garden Management System ".center(79, "=") + "\n")

        print("Adding plants to garden...")
        # Create a garden manager
        garden = GardenManager()

        plant1 = Plant("tomato", 5, 8)
        if plant1.name:
            garden.add_plant(plant1)

        plant2 = Plant("lettuce", 15, 5)
        if plant2.name:
            garden.add_plant(plant2)

        Plant("", 5, 5)

        print("\n" + "Watering plants...")
        garden.water_plants()

        print("Checking plant health...")
        garden.check_plant_health()

        print("Testing error recovery...")
        try:
            raise GardenError("Not enough water in tank")
        except GardenError as e:
            print(f"Caught GardenError: {e}")
        finally:
            pass

        print("System recovered and continuing...")
    finally:
        print("\n" + "Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
