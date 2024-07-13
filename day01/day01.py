def get_fuel(mass: int) -> int:
    return int(mass / 3) - 2


def get_fuel_recursive(mass: int) -> int:
    if mass <= 0:
        return 0
    return mass + get_fuel_recursive(get_fuel(mass))


def get_total_fuel(mass: int) -> int:
    return get_fuel_recursive(mass) - mass


if __name__ == "__main__":
    with open("day01/input.txt", "r") as f:
        lines = f.readlines()

    total = 0
    for line in lines:
        total += get_total_fuel(int(line.strip()))

    print(total)
