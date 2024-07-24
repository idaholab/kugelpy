'''
Created on mar 30, 2020
@author: balep, stewryan, ethan-fowler

Copyright 2024, Battelle Energy Alliance, LLC, ALL RIGHTS RESERVED
'''

import os
from re import sub
import numpy as np

def bu_reader(path_to_bu):
    '''
    Given a file directory, grab each `bumat` file and return a dictionary based on the burnup step and pebble compositions
    '''
    files = [x[2] for x in os.walk(path_to_bu)]
    pebble_dict = {}
    for file_name in files[0]:
        if 'bumat' in file_name:
            #time is denotes by `bumat#`, where the # gives the time step
            time = file_name.split('bumat')
            time = int(time[-1])
            a_dens = nuclide_loop(path_to_bu, file_name)
            pebble_dict[time] = a_dens
    return pebble_dict

def nuclide_loop(path_to_bu, file_name):
    '''
    Extract the atom densities for each pebble   
    '''
    f = open(f'{path_to_bu}/{file_name}', "r")
    nuclide_dict = {}
    correct_lines = False
    for line in f:
        if 'fuel' in line or 'uco' in line:
            correct_lines = True
            mat, a_density, volume = line.split('  ')[1], float(line.split(' ')[-3]), float(line.split(' ')[-1])
            nuclide_dict[mat] = {}
            nuclide_dict[mat]['volume'] = volume
        elif correct_lines:
            nuclide, a_den = read_nuclide_atom_density(line)
            nuclide_dict[mat][nuclide] = a_den
            
    f.close()  
    return nuclide_dict

def read_nuclide_atom_density(line):
    '''
    Read the atomic densities in the `bumat` file
    '''
    split_line = line.split('  ')
    nuclide = str(int(split_line[-2].split('.')[0]))
    a_den = float(split_line[-1])
    return nuclide, a_den


def serpent_rd(file_path, xs_name_list, material_ids):
    '''
    Extract Data from Serpent 2.0 output file.
    '''
    # Do not process all the line when looking for headers.
    line_cutoff = 42
    # initialize the line byte counter.
    line_byte = 0
    # initialize dictionaries.
    data_info = {}
    for xs_name in xs_name_list:
        data_info[xs_name] = []
    # First Reading to determine data position.
    with open(file_path, 'r') as sf:
        for line in sf:
            # cutoff very long lines.
            line_len = len(line)
            if line_len > line_cutoff:
                line = line[:line_cutoff]
            # split the line to check the first word.
            line_split = line.split()
            # If the split worked.
            if line_split:
                for xs_name in xs_name_list:
                    if line_split[0] == xs_name.strip():
                        for word in line_split:
                            if ')' in word:
                                numf = int(''.join([x for x in word if x not in ')]']))
                        data_info[xs_name].append([line_byte, numf])
                        break
            # Update line byte position counter.
            line_byte += line_len
    # Initialize dictionaries.
    data = {}
    for xs_name in xs_name_list:
        data[xs_name] = []
    # Second reading to grab the data.
    with open(file_path, 'r') as sf:
        for xid in material_ids:
            for xs_name in xs_name_list:
                if len(data_info[xs_name]) == 0:
                    raise RuntimeError(xs_name + ' not avaliable...')
                sf.seek(data_info[xs_name][xid][0])
                dummy, values = sf.readline().split('=', 1)
                values = sub(r"\[|\]|;", "", values).strip()
                try:
                    float(values[0])
                    values = np.fromstring(values, dtype=float, sep=' ')
                except ValueError:
                    ...
                data[xs_name].append(values)
    # Elaborate data.
    for xs_name in xs_name_list:
        for id_x in range(len(material_ids)):
            if xs_name in ['PRECURSOR_GROUPS', 'MACRO_NG']:
                data[xs_name][id_x] = int(data[xs_name][id_x][0])
            elif xs_name in ['GC_UNIVERSE_NAME']:
                data[xs_name][id_x] = sub("'", "", data[xs_name][id_x]).strip()
            else:
                data[xs_name][id_x] = data[xs_name][id_x][0::2]

    # Return  the materials cross sections.
    return data
