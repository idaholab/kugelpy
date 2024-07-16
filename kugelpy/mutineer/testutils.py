'''Utility module for testing modules.

Created on 2023-05-11 16:13:01

@authors: balep, stewryan

Copyright 2024, Battelle Energy Alliance, LLC, ALL RIGHTS RESERVED
'''
#===============================================================================
# Import
#===============================================================================
from _ctypes import ArgumentError
from os import path, mkdir,getenv
from errno import EEXIST

#===============================================================================
# Definitions
#===============================================================================
def gen_tmp_folder(main_tests_dir):
    if not path.isdir(main_tests_dir):
        try:
            mkdir(main_tests_dir)
        except OSError as exc:
            if exc.errno != EEXIST:
                raise
            pass

def find_pbed_input(file, file_path):
    '''
    Attempts to locate the start, end, and format of Serpent pbed position input in file.

    file: (str) name of file with pbed data 
    file_path: (str) path to file
    '''

    found_start = False # keeps track of whether or not start index had been found
    start_line = None # stores fist pbed geometry input line index
    end_line = None # stores last pbed geometry input line index
    format = None # indicates format of pbed geometry input line

    input = open(path.join(file_path, file)).readlines()
    
    for i in range(len(input)):
        temp = input[i].split()
        if len(temp)==6:
            try:
                float(temp[5])
            except:
                if not found_start:
                    found_start = True
                    format = 1
                    start_line = i
        elif len(temp)==5:
            try:
                float(temp[4])
            except:
                if not found_start:
                    found_start = True
                    start_line = i
                    format = 0
        else:
            if found_start:
                end_line = i
    
    return start_line, end_line, format

def compare_pbeds(solution_file, solution_path, test_file, test_path, solution_start_line=0, solution_end_line=None, format=0):
    '''
    Reads in the position (x, y, z) and radius of pebbles for comparison with expectation.
    In some edge cases, variable rounding due to numpy version can result in pebbles being placed in different 
    universes, thus universe names are not accounted for.

    solution_file: (str) file name of pre-generated solution output used for comparison
    solution_path: (str) path to solution output file
    test_file: (str) file name of pre-generated test output used for comparison
    test_path: (str) path to test output file
    solution_start_line: (str) index of line in solution file where pebble positions begin (0 by default)
    solution_end_line: (str) index of line in solution file where pebble positions end (None by default)
    format: (int) 1 if lines are numbered, 0 otherwise
    '''

    # read in solution and test files
    solution = open(path.join(solution_path, solution_file)).readlines()[solution_start_line:solution_end_line]
    test = open(path.join(test_path, test_file)).readlines()
    
    # remove new line characters
    while '\n' in solution:
        solution.remove('\n')
    while '\n' in test:
        test.remove('\n') 

    if len(solution) != len(test):
        # if files contain different number of pebbles, write failed
        print("compare_pbeds() Error: Different number of pebbles")
        print("Solution Length: ", len(solution))
        print("Test Length: ", len(test))
        return False
    else:
        # format solution and test lists
        for i in range(len(solution)):
            temp = solution[i].split()
            solution[i] = f'{temp[0+format]} {temp[1+format]} {temp[2+format]} {temp[3+format]}'
            temp = test[i].split()
            test[i] = f'{temp[0+format]} {temp[1+format]} {temp[2+format]} {temp[3+format]}'
        
        for line in test:
            # check to make sure every pebble in test is also in solution
            if line in solution:
                # remove line from solution to reduce number of comparison operations
                solution.remove(line)
            else:
                # pebble in line not contained in solution, write failed
                print("Incorrect line: ", line)
                print("Remaining length: ", len(solution))
                return False
        
        return True

#===============================================================================
# Main
#===============================================================================
if __name__ == '__main__':
    pass

