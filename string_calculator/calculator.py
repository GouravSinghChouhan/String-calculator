import re


def add(numbers: str) -> int:
    if numbers == '':
        return 0
    delimiters = [",", "\n"]

    if numbers.startswith("//"):
        header, numbers = numbers.split("\n", 1)

        if "[" in header:
            delimiters = re.findall(r"\[(.*?)]", header)
        else:
            delimiters = [header[2:]]

    pattern = "|".join(map(re.escape, delimiters))
    parts = re.split(pattern, numbers)

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
