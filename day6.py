from typing import List, Dict

def count_min_transfers(orbits: Dict, orbits_rev: Dict) -> int:

    n_transfers = 0

    pos = orbits['YOU']
    end = orbits['SAN']

    while True:
        if pos == end:
            break
        try:
            pos = orbits[pos]
        except KeyError:
            pos = orbits_rev[pos]

        n_transfers += 1

    return n_transfers

def count_orbits(orbits: Dict) -> int:

    n_orbits = 0

    for orbiter, orbitee in orbits.items():

        while True:

            n_orbits += 1

            if orbitee == 'COM':
                break

            orbitee = orbits[orbitee]

    return n_orbits


def build_orbits(data: List, reverse = False) -> List:

    orbits = {}

    for orbit in data:
        orbitee, orbiter = orbit.split(')')
        if reverse:
            try:
                orbits[orbitee].append(orbiter)
            except KeyError:
                orbits[orbitee] = [orbiter]
        else:
            orbits[orbiter] = orbitee

    return orbits


def read_data(filename: str) -> List:

    with open(filename,'r') as f:
        data = f.readlines()

    return [line.strip() for line in data]


def tests():

    orbits1 = build_orbits(['COM)B','B)C','C)D','D)E','E)F',
                            'B)G','G)H','D)I','E)J','J)K','K)L'])

    orbits2 = build_orbits(['COM)B','B)C','C)D','D)E','E)F',
                            'B)G','G)H','D)I','E)J','J)K','K)L',
                            'K)YOU','I)SAN'])
    orbits2_rev = build_orbits(['COM)B','B)C','C)D','D)E','E)F',
                            'B)G','G)H','D)I','E)J','J)K','K)L',
                            'K)YOU','I)SAN'],reverse=True)

    assert(count_orbits(orbits1) == 42)
    assert(count_min_transfers(orbits2,orbits2_rev) == 4)


def main():

    tests()

    data = read_data('data/day6.dat')
    orbits = build_orbits(data)
    orbits_rev = build_orbits(data,reverse=True)
    print()

    n_orbits = count_orbits(orbits)
    print(f'Number of orbits: {n_orbits}')
    n_transfers = count_min_transfers(orbits,orbits_rev)
    print(f'Number of transfers: {n_transfers}')


if __name__ == '__main__':
    main()
