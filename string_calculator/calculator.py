
def add(numbers: str) -> int:
    if numbers == '':
        return 0
    numbers = numbers.replace("\n", ",")
    parts = numbers.split(",")

    return sum(int(part) for part in parts)
