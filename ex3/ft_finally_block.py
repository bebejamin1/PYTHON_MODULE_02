#! /bin/python3.10

def water_plants(plant_list: list) -> None:
    """Water plants from the given list.

    Opens the watering system, waters each plant in the list, and ensures
    the watering system is closed in the finally block, even if an error occurs

    Args:
        plant_list (list): A list of plant names to water.

    Raises:
        ValueError: If a plant in the list is None.
    """
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError(f"Error: Cannot water {plant} "
                                 "- invalid plant!")
            else:
                print(f"Watering {plant}")
    except ValueError as e:
        print(e)
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """Test the watering system with valid and invalid plant lists.

    Tests normal watering flow and error handling when encountering
    invalid plant entries.
    """
    good_list = ["tomato", "lettuce", "carrots"]
    bad_list = ["tomato", None, "carrots"]

    print("Testing normal watering...")
    water_plants(good_list)
    print("Watering completed successfully!")

    print("\n" + "Testing with error...")
    water_plants(bad_list)


if __name__ == "__main__":
    print(" Garden Watering System ".center(50, "=") + "\n")
    test_watering_system()
    print("\n" + "Cleanup always happens, even with errors!")
