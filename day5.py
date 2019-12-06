import itertools
from typing import List

def Intcode_computer(code: List, input_val = 1) -> List:

    i = 0
    while i < len(code):
    #for i in range(0,len(code),4):

        opcode_str = str(code[i])

        opcode = int(opcode_str[-2:])

        par_modes = opcode_str[0:-2]

        if opcode == 99:
            #print(f"hit 99 @ {i}")
            return code

        elif opcode == 1:

            try:
                par1 = code[i+1] if int(par_modes[-1]) else code[code[i+1]]
            except IndexError:
                par1 = code[code[i+1]]
            try:
                par2 = code[i+2] if int(par_modes[-2]) else code[code[i+2]]
            except IndexError:
                par2 = code[code[i+2]]

            try:
                if int(par_modes[-3]):
                    code[i+3] = par1 + par2
                else:
                    code[code[i+3]] = par1 + par2
            except IndexError:
                code[code[i+3]] = par1 + par2

            i += 4

        elif opcode == 2:

            try:
                par1 = code[i+1] if int(par_modes[-1]) else code[code[i+1]]
            except IndexError:
                par1 = code[code[i+1]]
            try:
                par2 = code[i+2] if int(par_modes[-2]) else code[code[i+2]]
            except IndexError:
                par2 = code[code[i+2]]

            try:
                if int(par_modes[-3]):
                    code[i+3] = par1 * par2
                else:
                    code[code[i+3]] = par1 * par2
            except IndexError:
                code[code[i+3]] = par1 * par2

            i += 4

        elif opcode == 3:

            try:
                if int(par_modes[-1]):
                    code[i+1] = input_val
                else:
                    code[code[i+1]] = input_val
            except IndexError:
                code[code[i+1]] = input_val

            i += 2

        elif opcode == 4:
            try:
                par1 = code[i+1] if int(par_modes[-1]) else code[code[i+1]]
            except IndexError:
                par1 = code[code[i+1]]
            print(par1)
            i += 2

        elif opcode == 5:
            try:
                par1 = code[i+1] if int(par_modes[-1]) else code[code[i+1]]
            except IndexError:
                par1 = code[code[i+1]]
            try:
                par2 = code[i+2] if int(par_modes[-2]) else code[code[i+2]]
            except IndexError:
                par2 = code[code[i+2]]

            if par1:
                i = par2
            else:
                i += 3

        elif opcode == 6:
            try:
                par1 = code[i+1] if int(par_modes[-1]) else code[code[i+1]]
            except IndexError:
                par1 = code[code[i+1]]
            try:
                par2 = code[i+2] if int(par_modes[-2]) else code[code[i+2]]
            except IndexError:
                par2 = code[code[i+2]]

            if not par1:
                i = par2
            else:
                i += 3

        elif opcode == 7:

            try:
                par1 = code[i+1] if int(par_modes[-1]) else code[code[i+1]]
            except IndexError:
                par1 = code[code[i+1]]
            try:
                par2 = code[i+2] if int(par_modes[-2]) else code[code[i+2]]
            except IndexError:
                par2 = code[code[i+2]]

            val = 1 if par1 < par2 else 0

            try:
                if int(par_modes[-3]):
                    code[i+3] = val
                else:
                    code[code[i+3]] = val
            except IndexError:
                code[code[i+3]] = val

            i += 4

        elif opcode == 8:

            try:
                par1 = code[i+1] if int(par_modes[-1]) else code[code[i+1]]
            except IndexError:
                par1 = code[code[i+1]]
            try:
                par2 = code[i+2] if int(par_modes[-2]) else code[code[i+2]]
            except IndexError:
                par2 = code[code[i+2]]

            val = 1 if par1 == par2 else 0

            try:
                if int(par_modes[-3]):
                    code[i+3] = val
                else:
                    code[code[i+3]] = val
            except IndexError:
                code[code[i+3]] = val

            i += 4

        else:
            raise ValueError(f'Computer failed! What is opcode {opcode_str}?!')


    return code

def tests():

    print('---Running tests---')
    print('All outputs should be 1 (except for last - 1000):')
    Intcode_computer([3,9,8,9,10,9,4,9,99,-1,8],input_val=8)
    Intcode_computer([3,9,7,9,10,9,4,9,99,-1,8],input_val=7)
    Intcode_computer([3,3,1108,-1,8,3,4,3,99],input_val=8)
    Intcode_computer([3,3,1107,-1,8,3,4,3,99],input_val=7)
    Intcode_computer([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9],input_val=7)
    Intcode_computer([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
                      1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
                      999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99],
                     input_val=8)
    print('---Done with tests---')


def main():

    filename = 'day5.dat'
    with open(filename) as f:
        data = f.read().strip().split(',')
        data = [int(x) for x in data]

    tests()
    Intcode_computer(data,input_val=5)

if __name__ == '__main__':
    main()
