#! /bin/python3.10

def garden_operations(error_type: str) -> None:
    """Perform garden operations based on error type.

    Args:
        error_type (str): Type of error to test.

    Raises:
        ValueError: If error_type is "ValueError".
        ZeroDivisionError: If error_type is "ZeroDivisionError".
        FileNotFoundError: If error_type is "FileNotFoundError".
        KeyError: If error_type is "KeyError".
    """
    if (error_type == "ValueError"):
        int("abc")
    if (error_type == "ZeroDivisionError"):
        42 / 0
    if (error_type == "FileNotFoundError"):
        open("where.txt")
    if (error_type == "KeyError"):
        dic = {"flower": 1}
        dic["where_flower"]
    if (error_type == "all"):
        int("abc")
        42 / 0
        open("where.txt")
        dic = {"flower": "roze"}
        dic["where_flower"]


def test_error_types() -> None:
    """Test different error types in garden operations.

    Tests ValueError, ZeroDivisionError, FileNotFoundError, and KeyError
    by catching them individually and also testing multiple errors together.
    """
    test_value = ["ValueError", "ZeroDivisionError", "FileNotFoundError",
                  "KeyError"]

    for value in test_value:
        print(f"Testing: {value}...")
        try:
            garden_operations(value)
        except ValueError:
            print(f"Caught {value}: invalid literal for int()")
        except ZeroDivisionError:
            print(f"Caught {value}: division by zero")
        except FileNotFoundError:
            print(f"Caught {value}: No such file 'missing.txt'")
        except KeyError:
            print(f"Caught {value}: 'missing\\_plant'")
        print("")
    print("Testing multiple errors together...")
    try:
        garden_operations("all")
    except (ValueError, ZeroDivisionError,
            FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")
    print("\n" + "All error types tested successfully!")


if __name__ == "__main__":
    print(" Garden Error Types Demo ".center(50, "=") + "\n")
    test_error_types()
