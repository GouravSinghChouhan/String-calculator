
def add(numbers: str) -> int:
    if numbers == '':
        return 0

    parts = numbers.split(',')
    total = 0
    for part in parts:
        total+=int(part)
    return total