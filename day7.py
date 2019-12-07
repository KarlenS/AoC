'''
Don't know phase setting (first input) for the amplifiers (0-4).

Your job is to find the largest output signal that
can be sent to the thrusters by trying every possible
combination of phase settings on the amplifiers.
Make sure that memory is not shared or reused between copies of the program.
'''
from typing import List, Callable
from itertools import permutations
from day5 import Intcode_computer

def get_max_signal(data: List, phase_settings: List,
                   func: Callable) -> int:

    phase_options = permutations(phase_settings)

    max_signal = 0
    for phases in phase_options:
        signal = func(data, phases)
        if signal > max_signal:
            max_signal = signal

    return max_signal


def run_amp_chain(data: List, phases: List) -> int:

    input_val = 0
    for phase in phases:
        datacopy = data.copy()
        input_val = Intcode_computer(datacopy,
                                     input_val=input_val,
                                     first_input=phase)

    return input_val

def run_amp_loop(data: List, phases: List) -> int:

    # fuck it, we'll do it manually...

    phA, phB, phC, phD, phE = phases

    # jesus...
    dataA, dataB, dataC, dataD, dataE = data.copy(), data.copy(), data.copy(),\
                                        data.copy(), data.copy()


    first = True

    while True:

        if first:
            input_val = 0
            first = False
        else:
            input_val = outputE

        #probably shoulda used map or something...
        outputA = Intcode_computer(dataA,
                                   input_val=input_val,
                                   first_input=phA,
                                   first=first)
        outputB = Intcode_computer(dataB,
                                   input_val=outputA,
                                   first_input=phB,
                                   first=first)
        outputC = Intcode_computer(dataC,
                                   input_val=outputB,
                                   first_input=phC,
                                   first=first)
        outputD = Intcode_computer(dataD,
                                   input_val=outputC,
                                   first_input=phD,
                                   first=first)
        outputE = Intcode_computer(dataE,
                                   input_val=outputD,
                                   first_input=phE,
                                   first=first)

        print(outputE)

        if outputA == 99 or outputB == 99 or outputC == 99\
           or outputD == 99 or outputE == 99:
            break

    return outputE

def read_data(filename):

    with open(filename) as f:
        data = f.read().strip().split(',')

    return [int(x) for x in data]


def tests():
    assert(run_amp_chain([3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0],
                    phases=[4,3,2,1,0]) == 43210)

    assert(run_amp_chain([3,23,3,24,1002,24,10,24,1002,23,-1,23,
                          101,5,23,23,1,24,23,23,4,23,99,0,0],
                    phases=[0,1,2,3,4]) == 54321)

    assert(run_amp_chain([3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,
                          1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0],
                    phases=[1,0,4,3,2]) == 65210)

    assert(run_amp_loop([3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
                         27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5],
                         phases=[9,8,7,6,5]) == 139629729)

    assert(run_amp_loop([3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,
                         1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,
                         54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,
                         1005,56,6,99,0,0,0,0,10],
                         phases=[9,7,8,5,6]) == 18216)

def main():

    tests()

    filename = 'data/day7.dat'
    data = read_data(filename)
    #part1
    max_signal1 = get_max_signal(data,
                                 phase_settings=[0,1,2,3,4],
                                 func = run_amp_chain)
    print(f'Max signal part1 is {max_signal1}')

    #part2
    max_signal2 = get_max_signal(data,
                                 phase_settings=[5,6,7,8,9],
                                 func = run_amp_loop)

    print(f'Max signal part1 is {max_signal2}')


if __name__ == '__main__':
    main()
