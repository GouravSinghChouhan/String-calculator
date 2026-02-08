
def add(numbers: str) -> int:
    if numbers == '':
        return 0
    delimiter = ","

    if numbers.startswith("//"):
        header, numbers = numbers.split("\n", 1)
        delimiter = header[2:]

    numbers = numbers.replace("\n", delimiter)
    parts = numbers.split(delimiter)

    negatives =  [part for part in parts if int(part) < 0]
    if negatives:
        raise ValueError(
            f"Negative numbers not allowed {','.join(negatives)}"
        )

    return sum(int(part) for part in parts)
