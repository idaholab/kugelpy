'''Testing runutils module.

Created on Jan 27, 2022

@authors: balep, stewryan

Copyright 2024, Battelle Energy Alliance, LLC, ALL RIGHTS RESERVED
'''
#===============================================================================
# Import
#===============================================================================
from os import path

from kugelpy.kugelpy.kugelpy.maelstream import GenPBDist
from kugelpy.kugelpy.mutineer.logutils import LogTracker
from kugelpy.kugelpy.mutineer.testutils import gen_tmp_folder, find_pbed_input, compare_pbeds

#===============================================================================
# Shared objects
#===============================================================================
# Paths.
main_dir = path.dirname(path.realpath(__file__))
ifiles_dir = path.join(main_dir, 'testfiles')
distfile_path = path.join(ifiles_dir, 'dist.txt')
main_tests_dir = path.join(main_dir, '_tmp')
distfile_out_path = path.join(main_tests_dir, 'dist_part.txt')
regdistfile_out_path = path.join(main_tests_dir, 'reg_dist_part.txt')
gen_tmp_folder(main_tests_dir)
# Log.
log = LogTracker(); log.fllchar = ''; log.mltplflag = True; log.NTab = 1;
log.cmmchar = '@INF@'


#===============================================================================
# Tests
#===============================================================================
def test_distgen_rand_distr():
    log = LogTracker(); log.fllchar = '-'; log.mltplflag = True; log.NTab = 1
    chcurvs = [
            [[37.00, 0.00],
            [0.00, 0.00]],

            [[37.00, 12.0, 0.00],
            [60.00, 60.0, 12.00]],

            [[37.00, 12.00, 0.00],
            [120.00, 120.00, 24.00]]]
    trgtchnv = [3, 2]

    log.start()
    pbdist = GenPBDist(pbcyll=25.0, pblwconl=12.0, pbupconl=0.0, pbr=120.0,
                        dcr=24.0, idistrfile=distfile_path,
                        odistrfile=distfile_out_path, chcurvs=chcurvs,
                        log=log, trgtchnv=trgtchnv)
    pbdist.gen_distr()
    pbdist.divide_channels()
    pbdist.divide_sort_volumes()
    pbdist.write_distr()

    log.stop()

    # Check partition.
    # print(pbdist.chanpart, file=regtest)
    # print(pbdist.chanvolpart, file=regtest)
    '''
    We have bypassed the two above tests (will be included in a later version), 
    integral test (below) considered sufficient for time being
    '''

    # check file content
    # solution path
    solution_path = path.join(main_dir, '_regtest_outputs')

    # output path
    test_path = main_tests_dir

    solution_file ='test_maelstream.test_distgen_rand_distr.out'
    test_file = 'dist_part.txt'

    solution_start_line, solution_end_line, format = find_pbed_input(solution_file, solution_path)
    assert compare_pbeds(solution_file, solution_path, test_file, test_path, solution_start_line, solution_end_line, format) == True

def test_distgen_reg_distr():
    log = LogTracker(); log.fllchar = '-'; log.mltplflag = True; log.NTab = 1
    chcurvs = [
            [[37.00, 0.00],
            [0.00, 0.00]],

            [[37.00, 12.0, 0.00],
            [60.00, 60.0, 12.00]],

            [[37.00, 12.00, 0.00],
            [120.00, 120.00, 24.00]]]
    trgtchnv = [3, 2]

    log.start()
    pbdist = GenPBDist(pbcyll=25.0, pblwconl=12.0, pbupconl=0.0, pbr=120.0,
                       chcurvs=chcurvs, trgtchnv=trgtchnv, dcr=24.0, pr=3.0,
                       pbpfract=0.61, odistrfile=regdistfile_out_path)

    pbdist.gen_hcp_raw_distr()
    pbdist.gen_distr()
    pbdist.divide_channels()
    pbdist.divide_sort_volumes()
    pbdist.write_distr()

    # Check partition.
    # print(pbdist.chanpart, file=regtest)
    # print(pbdist.chanvolpart, file=regtest)
    '''
    We have bypassed the two above tests (will be included in a later version), 
    integral test (below) considered sufficient for time being
    '''

    # check file content
    # solution path
    solution_path = path.join(main_dir, '_regtest_outputs')

    # output path
    test_path = main_tests_dir

    solution_file ='test_maelstream.test_distgen_reg_distr.out'
    test_file = 'reg_dist_part.txt'

    solution_start_line, solution_end_line, format = find_pbed_input(solution_file, solution_path)
    assert compare_pbeds(solution_file, solution_path, test_file, test_path, solution_start_line, solution_end_line, format) == True

def test_distgen_rand_distr_axial_shift():

    log = LogTracker(); log.fllchar = '-'; log.mltplflag = True; log.NTab = 1
    chcurvs = [
            [[37.00, 0.00],
            [0.00, 0.00]],

            [[37.00, 12.0, 0.00],
            [60.00, 60.0, 12.00]],

            [[37.00, 12.00, 0.00],
            [120.00, 120.00, 24.00]]]
    trgtchnv = [3, 2]

    log.start()
    pbdist = GenPBDist(pbcyll=25.0, pblwconl=12.0, pbupconl=0.0, pbr=120.0,
                        dcr=24.0, axial_offset=200.0, idistrfile=distfile_path,
                        odistrfile=distfile_out_path, chcurvs=chcurvs,
                        log=log, trgtchnv=trgtchnv)
    pbdist.gen_distr()
    pbdist.divide_channels()
    pbdist.divide_sort_volumes()
    pbdist.write_distr()

    log.stop()

    # Check chcurve.
    # print(pbdist.chcurvs, regtest)
    # Check partition.
    # print(pbdist.chanpart, file=regtest)
    # print(pbdist.chanvolpart, file=regtest)
    '''
    We have bypassed the two above tests (will be included in a later version), 
    integral test (below) considered sufficient for time being
    '''

    # Check file content.
    # solution path
    solution_path = path.join(main_dir, '_regtest_outputs')

    # output path
    test_path = main_tests_dir

    solution_file ='test_maelstream.test_distgen_rand_distr_axial_shift.out'
    test_file = 'dist_part.txt'

    solution_start_line, solution_end_line, format = find_pbed_input(solution_file, solution_path)
    assert compare_pbeds(solution_file, solution_path, test_file, test_path, solution_start_line, solution_end_line, format) == True
