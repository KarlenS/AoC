from collections import Counter

def check_criteria(number: int) -> bool:

    numberlist = [i for i in str(number)]
    #is 6 digit
    is_sixdigit = len(numberlist) == 6

    notwithlargergroup = 2 in Counter(numberlist).values()

    adjacent = False
    nondecreasing = True

    ldig = numberlist[0]
    for rdig in numberlist[1:]:
        if int(ldig) > int(rdig):
            nondecreasing = False
        if ldig == rdig:
            adjacent = True

        ldig = rdig


    #return is_sixdigit and adjacent and nondecreasing
    #return adjacent and nondecreasing #part 1 
    return adjacent and nondecreasing and notwithlargergroup

def find_possible_pw_number(start: int, end: int) -> int:

    passed = 0
    for num in range(start, end+1):
        if check_criteria(num):
            passed += 1

    return passed

def tests():

    #assert(check_criteria(111111) == True) #part1
    assert(check_criteria(223450) == False)
    assert(check_criteria(123789) == False)
    assert(check_criteria(112233) == True)
    assert(check_criteria(111122) == True)


def main():

    tests()

    print(find_possible_pw_number(125730,579381))

if __name__ == '__main__':
    main()
