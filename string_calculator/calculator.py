def add(numbers: str) -> int:
    if numbers == '':
        return 0
    delimiter = ","

    if numbers.startswith("//"):
        header, numbers = numbers.split("\n", 1)
        delimiter = header[2:]

    numbers = numbers.replace("\n", delimiter)
    parts = numbers.split(delimiter)

    total = 0
    negatives = []
    for part in parts:
        value = int(part)
        if value < 0:
            negatives.append(part)
        elif value < 1000:
            total += value

    if negatives:
        raise ValueError(
            f"Negative numbers not allowed {','.join(negatives)}"
        )

    return total
