import random
import itertools
from typing import List

def Intcode_computer(code: List) -> List:

    for i in range(0,len(code),4):

        opcode = code[i]

        if opcode == 99:
            #print(f"hit 99 @ {i}")
            return code
        elif opcode == 1:
            code[code[i+3]] = code[code[i+1]] + code[code[i+2]]
        elif opcode == 2:
            code[code[i+3]] = code[code[i+1]] * code[code[i+2]]
        else:
            raise ValueError('Computer failed!')

    return code


def run_computer(instr: List, noun: int, verb: int) -> int:

    instr[1],instr[2] = noun, verb

    return Intcode_computer(instr)[0]


def tests():

    assert(Intcode_computer([1,0,0,0,99]) == [2,0,0,0,99])
    assert(Intcode_computer([2,3,0,3,99]) == [2,3,0,6,99])
    assert(Intcode_computer([2,4,4,5,99,0]) == [2,4,4,5,99,9801])
    assert(Intcode_computer([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99])


def main():

    tests()

    filename = 'day2.dat'

    with open(filename) as f:
        data = f.read().strip().split(',')
        data = [int(x) for x in data]


    pars = list(range(0,100))
    nv_pairs = list(itertools.product(pars,pars))

    n_combos = len(nv_pairs)

    tried = []
    output = 0

    #while output != 19690720 or len(tried) < n_combos:

    found = False

    for noun, verb in nv_pairs:
        #ind = random.randint(0,n_combos - 1)

        #if len(tried)%20 == 0:
        #    print(f'{len(tried)}/{n_combos}')

        #if ind not in tried:

        #noun, verb = nv_pairs[ind]
        instr = data.copy()

        output = run_computer(instr,noun,verb)

        if output == 19690720:
            found = True
            break

        #tried.append(ind)


    if found:

        print(f'Found value of {output} with noun={noun} and verb={verb}')
        print(f'answer is : {100 * noun + verb}')

    else:
        print('Did not find input combination to give 19690720.')


if __name__ == '__main__':
    main()
