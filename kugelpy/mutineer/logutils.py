'''Utility module to create and write log file or string.

Created on Jan 27, 2022

@authors: balep, stewryan, ethan-fowler

Copyright 2024, Battelle Energy Alliance, LLC, ALL RIGHTS RESERVED
'''

#===============================================================================
# Import
#===============================================================================
from os import path, makedirs
from time import strftime
from time import time

#===============================================================================
# Definitions
#===============================================================================


class LogTracker(object):
    '''Initialize log utility function.

    Parameters
    ----------
    basestr: str, optional
        Base string to print.
    fllchar: str, optional
        Filler char for the line.
    cmmchar: str, optional
        Comment char at the beginning of the line.
    NTab: int, optional
        Number of tabulation between comment and beginning of the string.
    ttlen: int, optional
        Maximum number of columns per line.
    strflag: bool, optional
        If True push into log string the just printed line.
    filflag: bool, optional
        If False, not writing to file id True it write to log_path.
    mltplflag: bool, optional
        If False, the line is cut to ttlen; the line is split into
        multiple line otherwise.
    log_path: str, optional
        Path to the log output file.

    Notes
    -----
    1: if 'time' inputed max length must be defined at least len($   15:16:15)
    2: if fllchar is more than one char it does not work

    '''

    def __init__(self, basestr:str='', fllchar:str='', cmmchar:str='#', NTab:int=0,
                 ttlen:int=100, strflag:bool=False, filflag:bool=False,
                 mltplflag:bool=False, log_path:str='log.out'):

        self.basestr = basestr
        self.fllchar = fllchar
        self.cmmchar = cmmchar
        self.NTab = NTab
        self.ttlen = ttlen
        self.strflag = strflag
        self.filflag = filflag
        self.mltplflag = mltplflag
        self.log_path = log_path
        self.log = ''
        self.timing = None

    def lprint(self, basestr=None, fllchar=None, cmmchar=None, NTab=None,
             ttlen=None, strflag=None, filflag=None, mltplflag=None, log_path=None):
        '''Print string with comment and filler.

        Parameters
        ----------
        Same as input parameters.

        '''
        # Replace default values if needed.
        if basestr or basestr == '': basestr_tmp = basestr
        else: basestr_tmp = self.basestr
        if fllchar or fllchar == '': fllchar_tmp = fllchar
        else: fllchar_tmp = self.fllchar
        if cmmchar or cmmchar == '': cmmchar_tmp = cmmchar
        else: cmmchar_tmp = self.cmmchar
        if NTab or NTab == 0: NTab_tmp = NTab
        else: NTab_tmp = self.NTab
        if ttlen: ttlen_tmp = ttlen
        else: ttlen_tmp = self.ttlen
        if strflag != None: strflag_tmp = strflag
        else: strflag_tmp = self.strflag
        if filflag != None: filflag_tmp = filflag
        else: filflag_tmp = self.filflag
        if mltplflag != None: mltplflag_tmp = mltplflag
        else: mltplflag_tmp = self.mltplflag
        if log_path != None: log_path_tmp = log_path
        else: log_path_tmp = self.log_path
        # Calculate how many char cut.
        cutchar = 0
        if (cmmchar_tmp): cutchar = cutchar + len(cmmchar_tmp) + 1  # '# '
        if (fllchar_tmp): cutchar = cutchar + 2  # ' -'
        sngltab = '  '
        tabstr = sngltab * NTab_tmp
        cutchar = cutchar + len(tabstr)
        # Calculate length and limitR length.
        strlen, maxlen = len(basestr_tmp), ttlen_tmp - cutchar
        # Prepare base string (cut or split).
        if basestr_tmp == 'time':
            basestr_tmp = self.comm_fill(strftime("%d/%m/%Y %H:%M:%S"), tabstr, \
                                        cmmchar_tmp, fllchar_tmp, ttlen_tmp)
        elif strlen >= maxlen:
            # Split string.
            if mltplflag_tmp:
                # Splitting string.
                linlist = [ basestr_tmp[0: maxlen]]
                basestr_tmp = basestr_tmp[maxlen:]
                linlist += [ basestr_tmp[i:i + maxlen - len(sngltab)] for i in
                           range(0, len(basestr_tmp), maxlen - len(sngltab)) ]
                # Add comment and filler to each line.
                basestr_tmp = ''
                # Push each line into base string.
                for i, line in enumerate(linlist):
                    basestr_tmp += ('\n' if i != 0 else '') + \
                    self.comm_fill(line, tabstr + (sngltab if i != 0 else '') , cmmchar_tmp, fllchar_tmp, \
                                  ttlen_tmp)
            # Cut string.
            else:
                # Push into base string.
                basestr_tmp = self.comm_fill(basestr_tmp[0:maxlen], tabstr,
                                            cmmchar_tmp, fllchar_tmp, ttlen_tmp)
        else:
            basestr_tmp = self.comm_fill(basestr_tmp, tabstr, cmmchar_tmp, \
                                        fllchar_tmp, ttlen_tmp)
        # Print string.
        print(basestr_tmp)
        # Push into the log string.
        if strflag_tmp:
            self.log = self.log + ('\n' if self.log else '') + basestr_tmp
        # Print to file.
        if filflag_tmp:
            if not path.isdir(path.dirname(log_path_tmp)):
                makedirs(path.dirname(log_path_tmp))
            with open(log_path_tmp, 'a') as lo:
                lo.write(basestr_tmp + '\n')

    def comm_fill(self, basestr, tabstr, cmmchar, fllchar, ttlen):
        '''Add comment and filler to a string with defined length.

        Parameters
        ----------
        basestr: str
            Base string to print.
        tabstr: str
            Total space before (multiple tabs) string.
        cmmchar: str
            Comment char at the beginning of the line.
        fllchar: str
            Filler char for the line.
        ttlen: int
            Maximum number of columns per line.

        '''
        # Add comment.
        basestr = (cmmchar if cmmchar else '') + \
        (' ' if basestr else '') + tabstr + basestr
        # Add filler.
        if fllchar:
            basestr = basestr + ' ' + \
            fllchar * (ttlen - len(basestr) - 1)
        # Return the string with comment and filler.
        return basestr

    def str_out(self):
        '''Return log string as output argument.'''
        return self.log

    def str_reset(self):
        '''Reset log string.'''
        self.log = ''

    def cnvrt_sec(self, time):
        '''Convert seconds to days hours minutes and seconds format

        Parameters
        ----------
        time:
            Time in seconds.

        Returns
        -------
        str:
            String with day, hour, minutes, seconds.

        '''
        day = time // (24 * 3600)
        time = time % (24 * 3600)
        hour = time // 3600
        time %= 3600
        minutes = time // 60
        time %= 60
        seconds = time
        return "%02d:%02d:%02d:%02d" % (day, hour, minutes, seconds)

    def start(self):
        '''Start logging message.'''
        self.lprint('Starting activities', '+', NTab=0)
        self.lprint('time', '', NTab=0)
        self.lprint('', fllchar='')
        self.timing = time()

    def stop(self):
        '''Stop logging message.'''
        self.lprint('', fllchar='')
        self.lprint('End of activities', '+', NTab=0)
        self.lprint('time', '', NTab=0)
        if self.timing:
            self.lprint('', '', NTab=0)
            self.lprint('Execution time(DD:HH:MM:SS)', '+', NTab=0)
            self.lprint(self.cnvrt_sec(time() - self.timing), '', NTab=0)
        self.lprint('', '', NTab=0, cmmchar='')
        self.timing = None

#===============================================================================
# LOG TEXT PRINTING
#===============================================================================
class logln(object):

    #----------------------------------------------------------------- Arguments
    # basestr = base string to print
    # fllchar = filler char for the line
    # cmmchar = comment char at the beginning of the line
    # NTab    = NTab number of tabulation between comment and beginning of sting
    # ttlen  = maximum number of columns per line
    # strflag = if True push into log string the just printed line
    # mltplflag = if False the line is cut otherwise multiple line plot
    #----------------------------------------------------------------------- WIP
    # 1 - if 'time' inputed max length must be defined at least len($   15:16:15)
    # 2 - if fllchar is more than one char is a mess
    #------------------------------------------ Initialize object & default data
    def __init__(self, basestr='', fllchar='', cmmchar='#', NTab=0,
                 ttlen=100, strflag=False, mltplflag=False, timing=None):
        self.basestr = basestr
        self.fllchar = fllchar
        self.cmmchar = cmmchar
        self.NTab = NTab
        self.ttlen = ttlen
        self.strflag = strflag
        self.mltplflag = mltplflag
        self.log = ''
        self.timing = timing

    #-------------------------------------- Print string with comment and filler
    def prnt(self, basestr=None, fllchar=None, cmmchar=None, NTab=None,
             ttlen=None, strflag=None, mltplflag=None, timing=None):
        #-------------------------------------- Replace default values if needed
        if basestr or basestr == '': basestr_tmp = basestr
        else: basestr_tmp = self.basestr
        if fllchar or fllchar == '': fllchar_tmp = fllchar
        else: fllchar_tmp = self.fllchar
        if cmmchar or cmmchar == '': cmmchar_tmp = cmmchar
        else: cmmchar_tmp = self.cmmchar
        if NTab or NTab == 0: NTab_tmp = NTab
        else: NTab_tmp = self.NTab
        if ttlen: ttlen_tmp = ttlen
        else: ttlen_tmp = self.ttlen
        if strflag != None: strflag_tmp = strflag
        else: strflag_tmp = self.strflag
        if mltplflag != None: mltplflag_tmp = strflag
        else: mltplflag_tmp = self.mltplflag
        if timing != None: timing_tmp = timing
        else: timing_tmp = self.timing
        #------------------------------------------- Calculate how many char cut
        cutchar = 0
        if (cmmchar_tmp): cutchar = cutchar + len(cmmchar_tmp) + 1  # '# '
        if (fllchar_tmp): cutchar = cutchar + 2  # ' -'
        tabstr = '  ' * NTab_tmp
        cutchar = cutchar + len(tabstr)
        #------------------------------------ Calculate length and limitR length
        strlen, maxlen = len(basestr_tmp), ttlen_tmp - cutchar
        #------------------------------------ Prepare base string (cut or split)
        if basestr_tmp == 'time':
            import time
            basestr_tmp = self.commfill(time.strftime("%d/%m/%Y %H:%M:%S"), tabstr, \
                                        cmmchar_tmp, fllchar_tmp, ttlen_tmp)
        else:
            if timing_tmp == 's':
                maxlen -= 6
                suffix = ' START'
            elif timing_tmp == 'e':
                maxlen -= 4
                suffix = ' END'
            else:
                suffix = ''

            if strlen >= maxlen:
                #-------------------------------------------------- Split string
                if mltplflag_tmp:
                    #------------------------------------------------ add suffix
                    basestr_tmp += suffix
                    #------------------------------------------ Splitting string
                    linlist = [ basestr_tmp[i:i + maxlen] for i in
                               range(0, strlen, maxlen) ]
                    #----------------------- Add comment and filler to each line
                    basestr_tmp = self.commfill('', tabstr, cmmchar_tmp, \
                                                fllchar_tmp, ttlen_tmp)
                    #--------------------------- Push each line into base string
                    for i, line in enumerate(linlist):
                        basestr_tmp = basestr_tmp + '\n' + \
                        self.commfill(line, tabstr, cmmchar_tmp, fllchar_tmp, \
                                      ttlen_tmp)
                #---------------------------------------------------- Cut string
                else:
                    #------------------------------------- Push into base string
                    basestr_tmp = self.commfill(basestr_tmp[0:maxlen] + suffix, tabstr,
                                                cmmchar_tmp, fllchar_tmp, ttlen_tmp)
            else:
                basestr_tmp = self.commfill(basestr_tmp + suffix, tabstr, cmmchar_tmp, \
                                            fllchar_tmp, ttlen_tmp)
        #---------------------------------------------------------- Print string
        print(basestr_tmp)
        #---------------------------------------------- Push into the log string
        if strflag_tmp:
            self.log += ('\n' if self.log else '') + basestr_tmp

    #-------------------- Add comment and filler to a string with defined length
    def commfill(self, basestr, tabstr, cmmchar, fllchar, ttlen):
        #----------------------------------------------------------- Add comment
        basestr = (cmmchar if cmmchar else '') + \
        (' ' if basestr else '') + tabstr + basestr
        #------------------------------------------------------------ Add filler
        if fllchar:
            basestr = basestr + ' ' + \
            fllchar * (ttlen - len(basestr) - 1)
        #----------------------------- Return the string with comment and filler
        return basestr

    #-------------------------------------- Return log string as output argument
    def logout(self):
        return self.log

    #---------------------------------------------------------- Reset log string
    def logreset(self):
        self.log = ''
#===============================================================================


#===============================================================================
# Main
#===============================================================================
if __name__ == '__main__':
    log = LogTracker(fllchar='', mltplflag=True, NTab=1, cmmchar='@INF@')
