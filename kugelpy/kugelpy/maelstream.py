'''
Created on Jan 27, 2022

@authors: balep, stewryan

Copyright 2024, Battelle Energy Alliance, LLC, ALL RIGHTS RESERVED
'''

#===============================================================================
# Importing
#===============================================================================
import numpy as np
from pyrates.kugelpy_open_source.kugelpy.mutineer.logutils import LogTracker


#===============================================================================
# Generate HCP distribution
#===============================================================================
class GenPBDist(object):
    '''Class to generate and or divide a pebble distribution in channels and
        volumes.

    Parameters
    ----------
    pbcyll: float, optional
        Pebble bed cylindrical section height (cm).
    pblwconl:
        Pebble bed lower cone section height (cm).
    pbupconl:
        Pebble bed upper cone section height (cm).
    pbr:
        Pebble bed radius (cm).
    pbdr:
        Pebble bed radius with dimples (cm).
    dcr:
        Discharging chute radius (cm).
    pr:
        Pebble radius (cm).
    pbpfract:
        Pebble bed packing fraction.
    idistrfile:
        Input file path with raw distribution obtained from external source.
    odistrfile:
        Output distribution file path.
    chcurvs:
        Channels delimiting curves. First curve is the symmetry axis the last
        one is the external profile of the pebble bed.
        chcurvs = [crv00, crv01, crv02, ...] list of channels delimiting curves
        crv00 = [[z0, z1, z2, z3,...]
                [x0, x1, x2, x3,...]] list of z and x coordinates of the curves
        First curve is the distribution centerline, the last is the bed
        external profile.

    trgtchnv:
        Target number of volumes per channel (curves-1)
    log: LogTracker, optional
        Log file object passed by main.

    Attributes
    ----------
    latxypitch:
        horizontal pitch for HCP lattice.
    latzpitch:
        vertical pitch for HCP lattice.
    nx:
        number of pebbles in the x direction.
    ny:
        number of pebbles in the y direction.
    xv:
        x coordinate of the centers.
    yv:
        y coordinate of the centers.
    np:
        Number of pebbles
    nc:
        Number of channels (curves-1)
    cxv:
        Center x of the distribution.
    cyv:
        Center y of the distribution.
    p1xv, p1yv, p1zv, p2xv, p2yv, p2zv:
        x,y,z coordinates of the 2 planes used to genrate the HCP distribution.
    chanpart:
        List containing the Ids of pebbles per channels
        chanpart = [ch00, ch01, ch02, ...] list of channels
        ch00 = [1, 2, 3, 4 , 5 ...] pebbles id
    chanvolpart:
        List containing the Ids of pebbles per channels and volumes
        chanvolpart = [ch00, ch01, ch02, ...] list of channels
        ch00 = [vol00, vol01, vol02, ...] list of volumes
        vol00 = [1, 2, 3, 4 , 5 ...] pebbles id

    Notes
    -----
    1. Read and write the distribution files in Serpent pbed format.

    '''

    def __init__(self, pbcyll:float=1000.0, pblwconl:float=0.0, pbupconl:float=0.0,
                pbr:float=100.0, pbdr:float=105.0, dcr:float=10.0, pr:float=3.0,
                pbpfract:float=0.61, axial_offset:float=0.0, idistrfile:str=None, odistrfile:str=None,
                chcurvs:list=None, trgtchnv:list=None, log:LogTracker=None):

        self.pbcyll = pbcyll #+ axial_offset
        self.pblwconl = pblwconl + axial_offset
        self.pbupconl = pbupconl #+ axial_offset
        self.pbttlen = pbcyll + pblwconl + pbupconl 
        self.pebble_bed_height_without_conuses = pbcyll - pbupconl
        self.dcr = dcr
        self.pbr = pbr
        self.pbdr = pbdr
        self.pr = pr
        self.pbpfract = pbpfract
        self.axial_offset = axial_offset
        self.idistrfile = idistrfile
        self.odistrfile = odistrfile
        self.latxypitch = np.cbrt(4 * np.sqrt(2) / 3 * np.pi * pr ** 3 / pbpfract)
        self.latzpitch = np.sqrt(2 / 3) * self.latxypitch
        self.nx = np.ceil(2 * pbr / self.latxypitch)
        self.ny = np.ceil(2 * pbr / (self.latxypitch * np.sqrt(3) / 2))
        self.nz = int(np.ceil(self.pbttlen / self.latzpitch))
        self.chcurvs = chcurvs
        self.update_chcurvs()
        if chcurvs:
            self.nc = len(self.chcurvs) - 1
            for crv in self.chcurvs:
                crv[0] = np.asarray(crv[0])
                crv[1] = np.asarray(crv[1])
                arr1inds = np.argsort(crv[0])
                crv[0] = crv[0][arr1inds]
                crv[1] = crv[1][arr1inds]
        self.np = 0
        self.trgtchnv = trgtchnv
        self.log = log
        
        self.lower_core_height = 0.0 if pblwconl == 0.0 else -50.548 
        
    def update_chcurvs(self):
        """
        Update the axial height of the pebble streams given an axial offset
        """
        for ch_num, channel in enumerate(self.chcurvs):
            for vol_num, volume in enumerate(channel[0]):
                self.chcurvs[ch_num][0][vol_num] += self.axial_offset
        
    def gen_hex_planes(self):
        '''Generate the 2 basic planes for the hex distribution.

        '''
        # Generate cartesian distribution.
        self.p1xv, self.p1yv = np.meshgrid(np.arange(self.nx), np.arange(self.ny), sparse=False, indexing='xy')
        # Stretch y coordinates to np.sqrt(3) / 2 of the pitch.
        self.p1yv = self.p1yv * self.latxypitch * np.sqrt(3) / 2
        self.p1yv = self.p1yv.flatten()
        #------------------------------------------------ stretch x to the pitch
        self.p1xv = self.p1xv * self.latxypitch
        #------------------------------------ add every 2 rows half of the pitch
        self.p1xv[::2,:] += self.latxypitch / 2
        self.p1xv = self.p1xv.flatten()
        #--------------------- add z coordinate a pebble radius above the bottom
        self.p1zv = np.full(self.p1xv.shape, [self.pr])
        #---------------------------------------------------------- second plane
        self.p2xv = self.p1xv + self.latxypitch / 2
        self.p2yv = self.p1yv + self.latxypitch * np.sqrt(3) / 6
        self.p2zv = self.p1zv

    def center_the_hex_planes(self):
        ''' Move the distribution of the 2 planess on xy to have them centered
            in x=0 y=0

        '''
        # Find the Center coordinates.
        self.cxv = np.mean(self.p1xv)
        self.cyv = np.mean(self.p1yv)
        dist_array = np.sqrt((self.p1xv - self.cxv) ** 2 + (self.p1yv - self.cyv) ** 2)
        smll_diff = dist_array.argmin()
        self.cxv = self.p1xv[smll_diff]
        self.cyv = self.p1yv[smll_diff]
        self.p1xv -= self.cxv
        self.p1yv -= self.cyv
        self.p2xv -= self.cxv
        self.p2yv -= self.cyv

    def gen_hcp_raw_distr(self):
        '''Generate raw hexagonal compact regular pebble distribution on a
            parallelepiped geometry.

        '''
        if self.log: self.log.lprint('Generate HCP distribution', NTab=2, fllchar='-')
        if self.log: self.log.lprint('Porosity: %1.4f' % (self.pbpfract), NTab=3, fllchar='')
        self.gen_hex_planes()
        self.center_the_hex_planes()
        self.xv = self.p1xv
        self.yv = self.p1yv
        self.zv = self.p1zv
        for i in range(1, self.nz):
            if (i % 2) == 0:
                self.xv = np.concatenate((self.xv, self.p1xv))
                self.yv = np.concatenate((self.yv, self.p1yv))
                self.zv = np.concatenate((self.zv, self.p1zv + self.latzpitch * i))
            else:
                self.xv = np.concatenate((self.xv, self.p2xv))
                self.yv = np.concatenate((self.yv, self.p2yv))
                self.zv = np.concatenate((self.zv, self.p2zv + self.latzpitch * i))
        self.np = len(self.xv)
        if self.log: self.log.lprint('Total number of pebbles: %d' % (self.np), NTab=3, fllchar='')

    def read_raw_distr(self):
        ''' Read a file of coordinates in the form:
            x0 y0 z0
            x1 y1 z1
            x2 y2 z2
            ...

        NOTE: float formatting was applied to lines 221-223 (append calls)
        '''
        if self.log: self.log.lprint('Read pebble distribution', NTab=2, fllchar='-')
        if self.log: self.log.lprint('Reading distribution file: %s' % (self.idistrfile), NTab=3, fllchar='')
        with open(self.idistrfile) as df:
            self.xv, self.yv, self.zv = [], [], []
            for l in df:
                row = l.split()
                self.xv.append(float(row[0]))
                self.yv.append(float(row[1]))
                self.zv.append(float(row[2]) + self.axial_offset)

                # num_digits = 12
                # self.xv.append(np.round(float(row[0]), num_digits))
                # self.yv.append(np.round(float(row[1]), num_digits))
                # self.zv.append(np.round(float(row[2]) + self.axial_offset, num_digits))

                # self.xv.append("{:.5f}".format(float(row[0])))
                # self.yv.append("{:.5f}".format(float(row[1])))
                # self.zv.append("{:.5f}".format(float(row[2]) + self.axial_offset))
        self.xv = np.asarray(self.xv)
        self.yv = np.asarray(self.yv)
        self.zv = np.asarray(self.zv)
        self.np = len(self.xv)
        if self.log: self.log.lprint('Total number of pebbles: %d' % (self.np), NTab=3, fllchar='')

    def write_distr(self):
        ''' Write a file of coordinates in the form:
            x0 y0 z0
            x1 y1 z1
            x2 y2 z2
            ...

        '''
        if self.log: self.log.lprint('Write pebble distribution', fllchar='=')
        if self.log: self.log.lprint('Writing distribution file: %s' % (self.odistrfile), NTab=2, fllchar='')
        peb_num = 1
        with open(self.odistrfile, "w") as df:
            for chi, ch in enumerate(self.chanvolpart):
                for voli, vol in enumerate(ch):
                    for i in vol:
                        df.write("%2d %11.4E %11.4E %11.4E %11.4E ch%02dvol%02d\n" % (peb_num, self.xv[i], self.yv[i], self.zv[i], self.pr, chi, voli))
                        peb_num += 1
        if self.log: self.log.lprint('Total number of pebbles: %d' % (self.np), NTab=2, fllchar='')

    def cut_cylinder(self):
        '''Exclude the pebbles outside the cylinder with radius self.pbr.

        '''
        if self.log: self.log.lprint('Cutting cylinder vertically', NTab=2, fllchar='-')
        if self.log: self.log.lprint('Cylinder radius: %1.4f (cm)' % (self.pbr), NTab=3, fllchar='')
        if self.log: self.log.lprint('Cylinder plus dimple radius: %1.4f (cm)' % (self.pbdr), NTab=3, fllchar='')
        pebble2keep = np.sqrt(self.xv ** 2 + self.yv ** 2) + self.pr < self.pbdr
        self.xv = self.xv[pebble2keep]
        self.yv = self.yv[pebble2keep]
        self.zv = self.zv[pebble2keep]
        self.np = len(self.xv)
        if self.log: self.log.lprint('Total number of pebbles: %d' % (self.np), NTab=3, fllchar='')

    def cut_lower_conus(self):
        '''Exclude the pebbles outside the lower conus with lower radius
            self.pblwconl.

        '''
        if self.log: self.log.lprint('Cutting lower conus', NTab=2, fllchar='-')
        if self.log: self.log.lprint('Conus height: %1.4f (cm)' % (self.pblwconl), NTab=3, fllchar='')
        if self.log: self.log.lprint('Conus bottom radius: %1.4f (cm)' % (self.dcr), NTab=3, fllchar='')
        m = self.pblwconl / (self.pbr - self.dcr)
        b = -m * self.dcr
        pebble2keep = self.zv - self.pr > self.pblwconl
        for i in range(self.np):
            if not pebble2keep[i]:
                rotx = np.sqrt(self.yv[i] ** 2 + self.xv[i] ** 2)
                roty = self.zv[i]
                dist = (roty - m * rotx - b) / np.sqrt(1 + m ** 2)
                if dist > self.pr:
                    pebble2keep[i] = True

        self.xv = self.xv[pebble2keep]
        self.yv = self.yv[pebble2keep]
        self.zv = self.zv[pebble2keep]
        self.np = len(self.xv)
        if self.log: self.log.lprint('Total number of pebbles: %d' % (self.np), NTab=3, fllchar='')

    def cut_upper_conus(self):
        '''Exclude the pebbles outside the upper conus with conus height
            self.pbupconl.

        '''
        if self.log: self.log.lprint('Cutting upper conus', NTab=2, fllchar='-')
        if self.log: self.log.lprint('Conus height: %1.4f (cm)' % (self.pbupconl), NTab=3, fllchar='')
        m = -self.pbupconl / self.pbr
        b = self.pebble_bed_height_without_conuses + self.pbupconl

        pebble2keep = self.zv + self.pr < self.pebble_bed_height_without_conuses
        for i in range(self.np):
            if not pebble2keep[i]:
                rotx = np.sqrt(self.yv[i] ** 2 + self.xv[i] ** 2)
                roty = self.zv[i]
                dist = (roty - m * rotx - b) / np.sqrt(1 + m ** 2)
                if dist < -self.pr:
                    pebble2keep[i] = True

        self.xv = self.xv[pebble2keep]
        self.yv = self.yv[pebble2keep]
        self.zv = self.zv[pebble2keep]
        self.np = len(self.xv)
        if self.log: self.log.lprint('Total number of pebbles: %d' % (self.np), NTab=3, fllchar='')

    def cut_lower_core(self):
        if self.log: self.log.lprint('Cutting lower core', NTab=2, fllchar='-')
        if self.log: self.log.lprint('Lower core height: %1.4f (cm)' % (self.lower_core_height), NTab=3, fllchar='')
        pebble2keep = self.zv + self.pr > self.lower_core_height
        for i in range(self.np):
            if not pebble2keep[i]:
                if self.zv[i] > self.lower_core_height:
                    pebble2keep[i] = True
        self.xv = self.xv[pebble2keep]
        self.yv = self.yv[pebble2keep]
        self.zv = self.zv[pebble2keep]
        self.np = len(self.xv)
        if self.log: self.log.lprint('Total number of pebbles: %d' % (self.np), NTab=3, fllchar='')
        
    def gen_distr(self):
        '''Generate HCP distribution with optional upper and lower conuses.

        '''
        if self.log: self.log.lprint('Generate pebble distribution', fllchar='=')
        if self.idistrfile:
            self.read_raw_distr()
        else:
            self.gen_hcp_raw_distr()
        self.cut_cylinder()       
        if self.pblwconl > 0.0 + self.axial_offset: self.cut_lower_conus()
        if self.pbupconl > 0.0 + self.axial_offset: self.cut_upper_conus()
        self.cut_lower_core()

    def divide_channels(self):
        '''Divide the distribution in channels generating list of list of IDs.

        '''
        if self.log: self.log.lprint('Divide distribution in channels', fllchar='=')
        pebble2keep = self.xv == self.xv
        ttpebbles = 0
        self.chanpart = []
        self.channp = []
        for cn in range(1, self.nc + 1):
            if self.log: self.log.lprint('Channel: %02d' % (cn - 1), NTab=2, fllchar='-')
            pebparttemp = []
            for pn in range(self.np):
                if pebble2keep[pn]:
                    bndmaxid = (self.chcurvs[cn][0] < self.zv[pn]).argmin()
                    bndminid = bndmaxid - 1
                    m = (self.chcurvs[cn][1][bndmaxid] - self.chcurvs[cn][1][bndminid])\
                         / (self.chcurvs[cn][0][bndmaxid] - self.chcurvs[cn][0][bndminid])
                    b = self.chcurvs[cn][1][bndminid] - m * self.chcurvs[cn][0][bndminid]
                    roty = np.sqrt(self.yv[pn] ** 2 + self.xv[pn] ** 2)
                    rotx = self.zv[pn]
                    dist = (roty - m * rotx - b) / np.sqrt(1 + m ** 2)
                    if dist < 0:
                        pebparttemp.append(pn)
                        pebble2keep[pn] = False
            self.channp.append(len(pebparttemp))
            ttpebbles += len(pebparttemp)
            if self.log: self.log.lprint('Channel total number of pebbles: %d'
                % (len(pebparttemp)), NTab=3, fllchar='')
            self.chanpart.append(np.asarray(pebparttemp))
        if self.log: self.log.lprint('Total', NTab=2, fllchar='-')
        if self.log: self.log.lprint('Total number of pebbles: %d/%d'
                % (ttpebbles, self.np), NTab=3, fllchar='')

    def divide_sort_volumes(self):
        '''Divide the distribution in volumes channels generating list of list
            of list of IDs.

        '''
        if self.log: self.log.lprint('Divide Channels in volumes', fllchar='=')
        self.chanvolpart = []
        for cn in range(self.nc):
            if self.log: self.log.lprint('Channel: %02d Number of volumes: %02d '
                % (cn, self.trgtchnv[cn]), NTab=2, fllchar='-')
            arr1inds = np.flip(np.argsort(self.zv[self.chanpart[cn]]))
            vnp = int(np.round(self.channp[cn] / self.trgtchnv[cn]))
            chanvolparttemp = []
            for vn in range(self.trgtchnv[cn] - 1):
                chanvolparttemp.append(self.chanpart[cn][arr1inds[vn * vnp:(vn + 1) * vnp]])
                if self.log: self.log.lprint('Volume: %02d pebbles: %d'
                    % (vn, len(chanvolparttemp[-1])), NTab=3, fllchar='')
            chanvolparttemp.append(self.chanpart[cn][arr1inds[(self.trgtchnv[cn] - 1) * vnp:]])
            if self.log: self.log.lprint('Volume: %02d pebbles: %d'
                % (self.trgtchnv[cn], len(chanvolparttemp[-1])), NTab=3, fllchar='')
            #chanvolparttemp.reverse()
            self.chanvolpart.append(chanvolparttemp)
        heights = []
        for cn in range(self.nc):
            if self.log: self.log.lprint(f'Channel: {cn}')            
            heights.append([893.0])
            for vn in range(self.trgtchnv[cn]):
                if self.log: self.log.lprint(f'Axial Volume: {vn}, Lower Z: {self.zv[self.chanvolpart[cn][vn][-1]]}', NTab=3, fllchar='')  
                heights[cn].append(self.zv[self.chanvolpart[cn][vn][-1]])
#===============================================================================
# Main
#===============================================================================
if __name__ == '__main__':
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
                        dcr=24.0, idistrfile='dist.txt', odistrfile='dist_part.txt',
                        chcurvs=chcurvs, log=log, trgtchnv=trgtchnv)
    pbdist.gen_distr()
    pbdist.divide_channels()
    pbdist.divide_sort_volumes()
    pbdist.write_distr()

    log.stop()
