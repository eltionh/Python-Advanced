from typing import Optional, Any, List, Union


def get_name(name: Optional[str] = None) -> str:
    if name:
        return name
    return "Anonymous"

print(get_name())


def get_value(value: Union[int, str]) -> str:
    if isinstance(value, int):
        return f"Number: {value}"
    return f"String: {value}"


print(get_value(1))


def any_value(value: Any):
    return value

print(any_value(10))



def show_numbers(numbers: List[int]):
    return sum(numbers)

print(show_numbers([1, 2, 3]))



















