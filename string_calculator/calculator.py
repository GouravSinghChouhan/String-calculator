
def add(numbers: str) -> int:
    if numbers == '':
        return 0

    delimiter = ","

    if numbers.startswith("//"):
        header, numbers = numbers.split("\n", 1)
        delimiter = header[2:]

    numbers = numbers.replace("\n", delimiter)
    parts = numbers.split(delimiter)

    return sum(int(part) for part in parts)