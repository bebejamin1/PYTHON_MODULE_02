#! /bin/python3.10

def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> str:
    if (plant_name == "" or plant_name is None):
        raise ValueError("Error: Plant name cannot be empty!")
    if (sunlight_hours < 2):
        raise ValueError(f"Error: sunlight hours {sunlight_hours} "
                         "is too low (min 2)")
    if (sunlight_hours > 12):
        raise ValueError(f"Error: sunlight hours {sunlight_hours} "
                         "is too high (max 12)")
    if (water_level < 1):
        raise ValueError(f"Error: sunlight hours {water_level} "
                         "is too low (min 1)")
    if (water_level > 10):
        raise ValueError(f"Error: sunlight hours {water_level} "
                         "is too high (max 10)")
    return (print(f"Plant '{plant_name}' is healthy!"))


def test_plant_checks():
    print("Testing good values...")
    try:
        check_plant_health("tomato", 5, 5)
    except ValueError as e:
        print(e)

    print("\n" + "Testing empty plant name...")
    try:
        check_plant_health("", 5, 5)
    except ValueError as e:
        print(e)

    print("\n" + "Testing bad water level...")
    try:
        check_plant_health("tomato", 15, 5)
    except ValueError as e:
        print(e)

    print("\n" + "Testing bad sunlight hours...")
    try:
        check_plant_health("tomato", 5, 0)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    print(" Garden Plant Health Checker ".center(40, "=") + "\n")
    test_plant_checks()
    print("\n" + "All error raising tests completed!")
