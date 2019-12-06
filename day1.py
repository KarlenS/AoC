def module_fuel_requirement(mass: int) -> int:
    return mass//3 - 2


def total_fuel_requirement(mass: int) -> int:

    mass_req = module_fuel_requirement(mass)

    if mass_req <= 0:
        return mass
    else:
        return mass + total_fuel_requirement(mass_req)


def run_tests() -> None:

    ####Part1####
    assert module_fuel_requirement(12) == 2
    assert module_fuel_requirement(14) == 2
    assert module_fuel_requirement(1969) == 654
    assert module_fuel_requirement(100756) == 33583

    ####Part2####
    assert total_fuel_requirement(module_fuel_requirement(14)) == 2
    assert total_fuel_requirement(module_fuel_requirement(1969)) == 966
    assert total_fuel_requirement(module_fuel_requirement(100756)) == 50346


def main():

    ####Tests####
    run_tests()

    #############
    # Main code #
    #############

    filename = 'data/day1.dat'

    module_total = 0
    total = 0

    with open(filename) as f:
        for count, mass in enumerate(f):
            ####Part1####
            module_fuel = module_fuel_requirement(int(mass))
            module_total += module_fuel
            ####Part2####
            total += total_fuel_requirement(module_fuel)

    print(f'Fuel required for all modules: {module_total}')
    print(f'Fuel required for all modules (with fuel mass): {total}')


if __name__ == '__main__':
    main()
