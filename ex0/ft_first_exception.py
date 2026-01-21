#! /bin/python3.10

def check_temperature(temp_str: str) -> int:
    """Check if temperature is within acceptable range for plants.

    Args:
        temp_str (str): Temperature value as a string.

    Returns:
        int: The temperature value as an integer.

    Prints:
        str: A message indicating if temperature is too cold, too hot,
        or perfect for plants.
    """
    temp_str = int(temp_str)
    if (temp_str < 0):
        print(f"Error: {temp_str}°C is too cold for plants (min 0°C)")
        return (temp_str)
    elif (temp_str > 40):
        print(f"Error: {temp_str}°C is too hot for plants (max 40°C)")
        return (temp_str)
    else:
        print(f"Temperature {temp_str}°C is perfect for plants!")
        return (temp_str)


def test_temperature_input() -> None:
    """Test temperature input validation with various test cases.

    Summury:
        Tests the check_temperature function with valid and invalid inputs,
        catching ValueError exceptions for non-numeric strings.
    """
    test_value = ["25", "abc", "100", "-50"]

    for value in test_value:
        print(f"Testing temperature: {value}")
        try:
            int(value)
        except ValueError:
            print(f"Error: {value} is not a valid number")
        else:
            check_temperature(value)
        print("")


if __name__ == "__main__":
    print(" Garden Temperature Checker ".center(50, "=") + "\n")
    test_temperature_input()
    print("All tests completed - program didn't crash!")
