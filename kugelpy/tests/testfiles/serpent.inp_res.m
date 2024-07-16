
% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.32' ;
COMPILE_DATE              (idx, [1: 20])  = 'Oct 21 2021 21:31:23' ;
DEBUG                     (idx, 1)        = 0 ;
TITLE                     (idx, [1:  8])  = 'Untitled' ;
CONFIDENTIAL_DATA         (idx, 1)        = 0 ;
INPUT_FILE_NAME           (idx, [1: 14])  = 'pbr_run_in.inp' ;
WORKING_DIRECTORY         (idx, [1: 60])  = '/home/stewryan/projects/NEAMS/pebshufpy/examples/auto_run_in' ;
HOSTNAME                  (idx, [1:  9])  = 'lemhi0447' ;
CPU_TYPE                  (idx, [1: 40])  = 'Intel(R) Xeon(R) Gold 6148 CPU @ 2.40GHz' ;
CPU_MHZ                   (idx, 1)        = 33581830.0 ;
START_DATE                (idx, [1: 24])  = 'Thu Mar  3 11:06:38 2022' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Mar  3 11:09:10 2022' ;

% Run parameters:

POP                       (idx, 1)        = 5000 ;
CYCLES                    (idx, 1)        = 100 ;
SKIP                      (idx, 1)        = 20 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1646330798446 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 0 ;
B1_CALCULATION            (idx, [1:  3])  = [ 0 0 0 ];
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;

CRIT_SPEC_MODE            (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 2 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 0 ;
DOUBLE_INDEXING           (idx, 1)        = 0 ;
MG_MAJORANT_MODE          (idx, 1)        = 1 ;
SPECTRUM_COLLAPSE         (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 4 ;
OMP_THREADS               (idx, 1)        = 40 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  40]) = [  1.00790E+00  9.97516E-01  1.02389E+00  1.01563E+00  1.04306E+00  1.01776E+00  1.00071E+00  1.01669E+00  9.82866E-01  9.90591E-01  1.02149E+00  1.02735E+00  9.60759E-01  9.94586E-01  1.02016E+00  1.02735E+00  9.85264E-01  9.86063E-01  9.93254E-01  1.01643E+00  9.86329E-01  9.93521E-01  9.87661E-01  9.65020E-01  9.79137E-01  9.75408E-01  1.01882E+00  9.94853E-01  1.02282E+00  1.03561E+00  1.03534E+00  9.61558E-01  1.02069E+00  1.00125E+00  9.68217E-01  9.56763E-01  1.00711E+00  9.94054E-01  9.68217E-01  9.98315E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;
OMP_SHARED_QUEUE_LIM      (idx, 1)        = 0 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 64])  = '/hpc-common/data/serpent/xsdata/endfb71_edep/endfb71_edep.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 46])  = '/hpc-common/data/serpent/xsdata/sss_endfb7.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 46])  = '/hpc-common/data/serpent/xsdata/sss_endfb7.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 46])  = '/hpc-common/data/serpent/xsdata/sss_endfb7.nfy' ;
BRA_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:   4]) = [  5.00000E-02 6.6E-10  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  9.49217E-01 7.7E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  5.07831E-02 0.00145  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  2.97805E-01 0.00023  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  9.97937E-01 4.8E-06  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  7.39068E-01 0.00038  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  3.34173E+01 0.00142  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  3.75624E+02 0.00143  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  3.75580E+02 0.00143  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.31476E+02 0.00037  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  3.18284E+03 0.00155  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 100 ;
SIMULATED_HISTORIES       (idx, 1)        = 125088 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  1.25136E+03 0.00231 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  1.25136E+03 0.00231 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.71584E+01 ;
RUNNING_TIME              (idx, 1)        =  2.52617E+00 ;
INIT_TIME                 (idx, [1:  2])  = [  1.34072E+00  1.34072E+00 ];
PROCESS_TIME              (idx, [1:  2])  = [  1.00500E-02  1.00500E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.17528E+00  1.17528E+00  0.00000E+00 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  1.23067E-01  6.50001E-04 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  2.52362E+00  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 10.75085 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  3.80890E+01 0.00663 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  1.89958E-01 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 192031.22 ;
ALLOC_MEMSIZE             (idx, 1)        = 28280.46;
MEMSIZE                   (idx, 1)        = 27989.25;
XS_MEMSIZE                (idx, 1)        = 23187.29;
MAT_MEMSIZE               (idx, 1)        = 138.58;
RES_MEMSIZE               (idx, 1)        = 16.29;
IFC_MEMSIZE               (idx, 1)        = 0.00;
MISC_MEMSIZE              (idx, 1)        = 4647.09;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 291.21;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 1518 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  5.00000E-05 ;
NEUTRON_ERG_NE            (idx, 1)        = 413898 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Unresolved resonance probability table sampling:

URES_DILU_CUT             (idx, 1)        =  1.00000E-09 ;
URES_EMIN                 (idx, 1)        =  1.00000E+37 ;
URES_EMAX                 (idx, 1)        = -1.00000E+37 ;
URES_AVAIL                (idx, 1)        = 244 ;
URES_USED                 (idx, 1)        = 0 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 1889 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 728 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 1161 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 18115 ;
TOT_TRANSMU_REA           (idx, 1)        = 3087 ;

% Neutron physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 0 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_PREPROCESSOR      (idx, 1)        = 1 ;
TMS_MODE                  (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Energy deposition:

EDEP_MODE                 (idx, 1)        = 0 ;
EDEP_DELAYED              (idx, 1)        = 1 ;
EDEP_KEFF_CORR            (idx, 1)        = 1 ;
EDEP_LOCAL_EGD            (idx, 1)        = 0 ;
EDEP_COMP                 (idx, [1:  9])  = [ 0 0 0 0 0 0 0 0 0 ];
EDEP_CAPT_E               (idx, 1)        =  0.00000E+00 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  1.70841E+18 ;
TOT_DECAY_HEAT            (idx, 1)        =  1.68768E+05 ;
TOT_SF_RATE               (idx, 1)        =  3.11761E+06 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  7.27934E+17 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  5.08255E+04 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  9.80472E+17 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  1.17942E+05 ;
INHALATION_TOXICITY       (idx, 1)        =  8.39999E+09 ;
INGESTION_TOXICITY        (idx, 1)        =  2.45972E+09 ;
ACTINIDE_INH_TOX          (idx, 1)        =  3.10800E+09 ;
ACTINIDE_ING_TOX          (idx, 1)        =  3.07266E+08 ;
FISSION_PRODUCT_INH_TOX   (idx, 1)        =  5.29199E+09 ;
FISSION_PRODUCT_ING_TOX   (idx, 1)        =  2.15245E+09 ;
SR90_ACTIVITY             (idx, 1)        =  2.26937E+15 ;
TE132_ACTIVITY            (idx, 1)        =  4.57656E+16 ;
I131_ACTIVITY             (idx, 1)        =  3.12280E+16 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  2.32576E+14 ;
CS137_ACTIVITY            (idx, 1)        =  2.44217E+15 ;
PHOTON_DECAY_SOURCE       (idx, 1)        =  1.67338E+18 ;
NEUTRON_DECAY_SOURCE      (idx, 1)        =  0.00000E+00 ;
ALPHA_DECAY_SOURCE        (idx, 1)        =  2.97932E+13 ;
ELECTRON_DECAY_SOURCE     (idx, 1)        =  3.36629E+18 ;

% Normalization coefficient:

NORM_COEF                 (idx, [1:   4]) = [  1.61861E+15 0.00160  0.00000E+00 0.0E+00 ];

% Parameters for burnup calculation:

BURN_MATERIALS            (idx, 1)        = 55 ;
BURN_MODE                 (idx, 1)        = 2 ;
BURN_STEP                 (idx, 1)        = 0 ;
BURN_RANDOMIZE_DATA       (idx, [1:  3])  = [ 0 0 0 ];
BURNUP                    (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BURN_DAYS                 (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
FIMA                      (idx, [1:  3])  = [  0.00000E+00  0.00000E+00  8.19829E+27 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  3.03701E-01 0.00410 ];
U235_FISS                 (idx, [1:   4]) = [  8.29309E+17 0.00083  8.98443E-01 0.00081 ];
U238_FISS                 (idx, [1:   4]) = [  2.07081E+15 0.04287  2.24361E-03 0.04287 ];
PU239_FISS                (idx, [1:   4]) = [  9.00685E+16 0.00723  9.75833E-02 0.00726 ];
PU241_FISS                (idx, [1:   4]) = [  1.53762E+15 0.05582  1.66596E-03 0.05582 ];
U235_CAPT                 (idx, [1:   4]) = [  1.56968E+17 0.00538  1.55493E-01 0.00461 ];
U238_CAPT                 (idx, [1:   4]) = [  3.19434E+17 0.00435  3.16321E-01 0.00303 ];
PU239_CAPT                (idx, [1:   4]) = [  5.28514E+16 0.00994  5.22966E-02 0.00920 ];
PU240_CAPT                (idx, [1:   4]) = [  8.54486E+15 0.02336  8.46472E-03 0.02316 ];
PU241_CAPT                (idx, [1:   4]) = [  5.93114E+14 0.08454  5.86834E-04 0.08433 ];
XE135_CAPT                (idx, [1:   4]) = [  3.65000E+16 0.01052  3.61397E-02 0.01001 ];
SM149_CAPT                (idx, [1:   4]) = [  9.66891E+15 0.02081  9.57858E-03 0.02056 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS    (idx, [1:  2])  = [ 500544 5.00000E+05 ];
BALA_SRC_NEUTRON_NXN     (idx, [1:  2])  = [ 0 9.92981E+00 ];
BALA_SRC_NEUTRON_VR      (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT     (idx, [1:  2])  = [ 500544 5.00010E+05 ];

BALA_LOSS_NEUTRON_CAPT    (idx, [1:  2])  = [ 249566 2.49302E+05 ];
BALA_LOSS_NEUTRON_FISS    (idx, [1:  2])  = [ 228582 2.28337E+05 ];
BALA_LOSS_NEUTRON_LEAK    (idx, [1:  2])  = [ 22396 2.23708E+04 ];
BALA_LOSS_NEUTRON_CUT     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_ERR     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT     (idx, [1:  2])  = [ 500544 5.00010E+05 ];

BALA_NEUTRON_DIFF         (idx, [1:  2])  = [ 0 -1.10595E-09 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   6]) = [  3.00000E+07 0.0E+00  3.00000E+07 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_POWDENS               (idx, [1:   6]) = [  9.26200E-03 2.6E-09  9.26200E-03 2.6E-09  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   6]) = [  2.28922E+18 0.00011  2.28922E+18 0.00011  0.00000E+00 0.0E+00 ];
TOT_FISSRATE              (idx, [1:   6]) = [  9.23045E+17 2.1E-05  9.23045E+17 2.1E-05  0.00000E+00 0.0E+00 ];
TOT_CAPTRATE              (idx, [1:   6]) = [  1.00966E+18 0.00299  6.19150E+17 0.00358  3.90508E+17 0.00384 ];
TOT_ABSRATE               (idx, [1:   6]) = [  1.93270E+18 0.00156  1.54220E+18 0.00144  3.90508E+17 0.00384 ];
TOT_SRCRATE               (idx, [1:   6]) = [  2.02327E+18 0.00160  2.02327E+18 0.00160  0.00000E+00 0.0E+00 ];
TOT_FLUX                  (idx, [1:   6]) = [  1.84636E+21 0.00210  5.09618E+18 0.00171  1.84127E+21 0.00210 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  9.06056E+16 0.00696 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  2.02331E+18 0.00160 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  7.58335E+20 0.00213 ];
INI_FMASS                 (idx, 1)        =  3.23904E+03 ;
TOT_FMASS                 (idx, 1)        =  3.23904E+03 ;
INI_BURN_FMASS            (idx, 1)        =  3.23904E+03 ;
TOT_BURN_FMASS            (idx, 1)        =  3.23904E+03 ;

% Six-factor formula:

SIX_FF_ETA                (idx, [1:   2]) = [  1.75061E+00 0.00119 ];
SIX_FF_F                  (idx, [1:   2]) = [  7.70205E-01 0.00084 ];
SIX_FF_P                  (idx, [1:   2]) = [  8.50693E-01 0.00067 ];
SIX_FF_EPSILON            (idx, [1:   2]) = [  1.03373E+00 0.00039 ];
SIX_FF_LF                 (idx, [1:   2]) = [  9.99787E-01 2.0E-05 ];
SIX_FF_LT                 (idx, [1:   2]) = [  9.55462E-01 0.00030 ];
SIX_FF_KINF               (idx, [1:   2]) = [  1.18563E+00 0.00154 ];
SIX_FF_KEFF               (idx, [1:   2]) = [  1.13259E+00 0.00158 ];

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.48008E+00 0.00013 ];
FISSE                     (idx, [1:   2]) = [  2.02856E+02 2.1E-05 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.13164E+00 0.00163  7.03716E-02 0.00160  4.14976E-04 0.02859 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.13259E+00 0.00158 ];
COL_KEFF                  (idx, [1:   2]) = [  1.13259E+00 0.00158 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.13259E+00 0.00158 ];
ABS_KINF                  (idx, [1:   2]) = [  1.18563E+00 0.00154 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.90292E+01 0.00018 ];
IMP_ALF                   (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  1.09099E-07 0.00354 ];
IMP_EALF                  (idx, [1:   2]) = [  2.00000E+01 0.0E+00 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  7.18126E-03 0.04456 ];
IMP_AFGE                  (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% Forward-weighted delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 6 ;
FWD_ANA_BETA_ZERO         (idx, [1:  14]) = [  5.17816E-03 0.02053  1.80713E-04 0.10356  9.43664E-04 0.04497  8.91057E-04 0.04519  2.00918E-03 0.03089  8.26685E-04 0.04533  3.26862E-04 0.07775 ];
FWD_ANA_LAMBDA            (idx, [1:  14]) = [  4.62591E-01 0.02963  2.90025E-03 0.09496  2.35819E-02 0.03103  8.55027E-02 0.03200  2.82078E-01 0.01347  5.91225E-01 0.03317  9.98063E-01 0.06823 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  14]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  14]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Adjoint weighted time constants using Nauchi's method:

IFP_CHAIN_LENGTH          (idx, 1)        = 15 ;
ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  1.17847E-03 0.00328  1.17847E-03 0.00328  1.04307E-03 0.04606 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  1.33216E-03 0.00281  1.33217E-03 0.00282  1.17736E-03 0.04557 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  14]) = [  5.86285E-03 0.02887  2.28252E-04 0.13698  1.06800E-03 0.06561  1.02143E-03 0.06680  2.21241E-03 0.04459  9.44769E-04 0.07170  3.87996E-04 0.11407 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  14]) = [  4.64026E-01 0.04715  1.33334E-02 0.00014  3.26339E-02 0.00092  1.20355E-01 0.00100  3.02328E-01 0.00040  8.50804E-01 0.00055  2.85053E+00 0.00064 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  1.15574E-03 0.00844  1.15668E-03 0.00846  4.70778E-04 0.09528 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  1.30619E-03 0.00822  1.30725E-03 0.00824  5.30769E-04 0.09520 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  14]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  14]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  14]) = [  6.05006E-03 0.07656  1.65332E-04 0.41472  9.73394E-04 0.20187  1.17897E-03 0.16260  2.32313E-03 0.12917  1.01319E-03 0.19152  3.96045E-04 0.37597 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  14]) = [  4.44038E-01 0.09819  1.33295E-02 0.00049  3.27390E-02 0.0E+00  1.19891E-01 0.00287  3.02333E-01 0.00073  8.50605E-01 0.00071  2.85300E+00 0.0E+00 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  1.16732E-03 0.00221 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  1.31953E-03 0.00141 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  6.09879E-03 0.01637 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -5.24226E+00 0.01673 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  1.66738E-06 0.00053 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  3.01128E-05 0.00046  3.01138E-05 0.00046  3.00264E-05 0.00694 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  1.74179E-03 0.00179  1.74166E-03 0.00180  1.78766E-03 0.02839 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  8.58389E-01 0.00063  8.57845E-01 0.00065  1.21818E+00 0.04686 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.10314E+01 0.04392 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  3.74805E+02 0.00143  3.48254E+02 0.00179 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.32' ;
COMPILE_DATE              (idx, [1: 20])  = 'Oct 21 2021 21:31:23' ;
DEBUG                     (idx, 1)        = 0 ;
TITLE                     (idx, [1:  8])  = 'Untitled' ;
CONFIDENTIAL_DATA         (idx, 1)        = 0 ;
INPUT_FILE_NAME           (idx, [1: 14])  = 'pbr_run_in.inp' ;
WORKING_DIRECTORY         (idx, [1: 60])  = '/home/stewryan/projects/NEAMS/pebshufpy/examples/auto_run_in' ;
HOSTNAME                  (idx, [1:  9])  = 'lemhi0447' ;
CPU_TYPE                  (idx, [1: 40])  = 'Intel(R) Xeon(R) Gold 6148 CPU @ 2.40GHz' ;
CPU_MHZ                   (idx, 1)        = 33581830.0 ;
START_DATE                (idx, [1: 24])  = 'Thu Mar  3 11:06:38 2022' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Mar  3 11:11:06 2022' ;

% Run parameters:

POP                       (idx, 1)        = 5000 ;
CYCLES                    (idx, 1)        = 100 ;
SKIP                      (idx, 1)        = 20 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1646330798446 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 0 ;
B1_CALCULATION            (idx, [1:  3])  = [ 0 0 0 ];
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;

CRIT_SPEC_MODE            (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 2 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 0 ;
DOUBLE_INDEXING           (idx, 1)        = 0 ;
MG_MAJORANT_MODE          (idx, 1)        = 1 ;
SPECTRUM_COLLAPSE         (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 4 ;
OMP_THREADS               (idx, 1)        = 40 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  40]) = [  9.88962E-01  9.92688E-01  1.02223E+00  1.01877E+00  1.01691E+00  1.02489E+00  9.94817E-01  1.03633E+00  9.73526E-01  1.01531E+00  1.01957E+00  1.01983E+00  9.83373E-01  9.99874E-01  1.01983E+00  1.03341E+00  9.70332E-01  9.86301E-01  9.50372E-01  9.70865E-01  9.96946E-01  1.03500E+00  9.79647E-01  9.66607E-01  1.00067E+00  9.76454E-01  1.02569E+00  9.78317E-01  1.00812E+00  1.00573E+00  1.01531E+00  9.76720E-01  1.01877E+00  1.02729E+00  9.77252E-01  9.79647E-01  1.02542E+00  9.53300E-01  1.00679E+00  1.00812E+00  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;
OMP_SHARED_QUEUE_LIM      (idx, 1)        = 0 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 64])  = '/hpc-common/data/serpent/xsdata/endfb71_edep/endfb71_edep.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 46])  = '/hpc-common/data/serpent/xsdata/sss_endfb7.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 46])  = '/hpc-common/data/serpent/xsdata/sss_endfb7.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 46])  = '/hpc-common/data/serpent/xsdata/sss_endfb7.nfy' ;
BRA_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:   4]) = [  5.00000E-02 0.0E+00  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  9.49122E-01 7.5E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  5.08780E-02 0.00141  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  2.97448E-01 0.00025  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  9.97926E-01 5.0E-06  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  7.38099E-01 0.00041  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  3.35383E+01 0.00147  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  3.74426E+02 0.00149  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  3.74381E+02 0.00149  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.31705E+02 0.00038  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  3.18129E+03 0.00150  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 100 ;
SIMULATED_HISTORIES       (idx, 1)        = 125219 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  1.25169E+03 0.00239 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  1.25169E+03 0.00239 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  6.43751E+01 ;
RUNNING_TIME              (idx, 1)        =  4.46957E+00 ;
INIT_TIME                 (idx, [1:  2])  = [  1.34072E+00  1.34072E+00 ];
PROCESS_TIME              (idx, [1:  2])  = [  1.51500E-02  2.50000E-03 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  3.10597E+00  9.57050E-01  9.73633E-01 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  4.43333E-03  2.36667E-03 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  2.21666E-03  1.08333E-03 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  3.57150E-01  1.16733E-01 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.35122E+00  1.29858E+01 ];
CPU_USAGE                 (idx, 1)        = 14.40298 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  3.81395E+01 0.00625 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  3.05667E-01 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 192031.22 ;
ALLOC_MEMSIZE             (idx, 1)        = 28280.46;
MEMSIZE                   (idx, 1)        = 27989.25;
XS_MEMSIZE                (idx, 1)        = 23187.29;
MAT_MEMSIZE               (idx, 1)        = 138.58;
RES_MEMSIZE               (idx, 1)        = 16.29;
IFC_MEMSIZE               (idx, 1)        = 0.00;
MISC_MEMSIZE              (idx, 1)        = 4647.09;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 291.21;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 1518 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  5.00000E-05 ;
NEUTRON_ERG_NE            (idx, 1)        = 413898 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Unresolved resonance probability table sampling:

URES_DILU_CUT             (idx, 1)        =  1.00000E-09 ;
URES_EMIN                 (idx, 1)        =  1.00000E+37 ;
URES_EMAX                 (idx, 1)        = -1.00000E+37 ;
URES_AVAIL                (idx, 1)        = 244 ;
URES_USED                 (idx, 1)        = 0 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 1889 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 728 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 1161 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 18115 ;
TOT_TRANSMU_REA           (idx, 1)        = 3087 ;

% Neutron physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 0 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_PREPROCESSOR      (idx, 1)        = 1 ;
TMS_MODE                  (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Energy deposition:

EDEP_MODE                 (idx, 1)        = 0 ;
EDEP_DELAYED              (idx, 1)        = 1 ;
EDEP_KEFF_CORR            (idx, 1)        = 1 ;
EDEP_LOCAL_EGD            (idx, 1)        = 0 ;
EDEP_COMP                 (idx, [1:  9])  = [ 0 0 0 0 0 0 0 0 0 ];
EDEP_CAPT_E               (idx, 1)        =  0.00000E+00 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  5.92401E+18 ;
TOT_DECAY_HEAT            (idx, 1)        =  1.88348E+06 ;
TOT_SF_RATE               (idx, 1)        =  3.13254E+06 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  6.61274E+17 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  4.56297E+04 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  5.26274E+18 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  1.83785E+06 ;
INHALATION_TOXICITY       (idx, 1)        =  8.62964E+09 ;
INGESTION_TOXICITY        (idx, 1)        =  3.02867E+09 ;
ACTINIDE_INH_TOX          (idx, 1)        =  3.10361E+09 ;
ACTINIDE_ING_TOX          (idx, 1)        =  2.80137E+08 ;
FISSION_PRODUCT_INH_TOX   (idx, 1)        =  5.52603E+09 ;
FISSION_PRODUCT_ING_TOX   (idx, 1)        =  2.74853E+09 ;
SR90_ACTIVITY             (idx, 1)        =  2.28503E+15 ;
TE132_ACTIVITY            (idx, 1)        =  4.22871E+16 ;
I131_ACTIVITY             (idx, 1)        =  2.95928E+16 ;
I132_ACTIVITY             (idx, 1)        =  4.27547E+16 ;
CS134_ACTIVITY            (idx, 1)        =  2.35160E+14 ;
CS137_ACTIVITY            (idx, 1)        =  2.45954E+15 ;
PHOTON_DECAY_SOURCE       (idx, 1)        =  4.95723E+18 ;
NEUTRON_DECAY_SOURCE      (idx, 1)        =  9.81594E+15 ;
ALPHA_DECAY_SOURCE        (idx, 1)        =  3.01307E+13 ;
ELECTRON_DECAY_SOURCE     (idx, 1)        =  7.09695E+18 ;

% Normalization coefficient:

NORM_COEF                 (idx, [1:   4]) = [  1.62660E+15 0.00152  0.00000E+00 0.0E+00 ];

% Parameters for burnup calculation:

BURN_MATERIALS            (idx, 1)        = 55 ;
BURN_MODE                 (idx, 1)        = 2 ;
BURN_STEP                 (idx, 1)        = 1 ;
BURN_RANDOMIZE_DATA       (idx, [1:  3])  = [ 0 0 0 ];
BURNUP                    (idx, [1:  2])  = [  4.63100E-02  4.63794E-02 ];
BURN_DAYS                 (idx, [1:  2])  = [  5.00000E+00  5.00000E+00 ];
FIMA                      (idx, [1:  3])  = [  4.87026E-05  3.99278E+23  8.19789E+27 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  3.05694E-01 0.00381 ];
U235_FISS                 (idx, [1:   4]) = [  8.19560E+17 0.00079  8.88145E-01 0.00077 ];
U238_FISS                 (idx, [1:   4]) = [  2.34010E+15 0.04335  2.53607E-03 0.04336 ];
PU239_FISS                (idx, [1:   4]) = [  9.89987E+16 0.00612  1.07289E-01 0.00614 ];
PU240_FISS                (idx, [1:   4]) = [  8.39998E+12 0.70623  9.09937E-06 0.70623 ];
PU241_FISS                (idx, [1:   4]) = [  1.82130E+15 0.04785  1.97392E-03 0.04785 ];
U235_CAPT                 (idx, [1:   4]) = [  1.55006E+17 0.00550  1.52179E-01 0.00471 ];
U238_CAPT                 (idx, [1:   4]) = [  3.21514E+17 0.00399  3.15676E-01 0.00286 ];
PU239_CAPT                (idx, [1:   4]) = [  5.95251E+16 0.00908  5.83790E-02 0.00833 ];
PU240_CAPT                (idx, [1:   4]) = [  9.94490E+15 0.02054  9.76699E-03 0.02030 ];
PU241_CAPT                (idx, [1:   4]) = [  7.95566E+14 0.07251  7.83917E-04 0.07265 ];
XE135_CAPT                (idx, [1:   4]) = [  3.75680E+16 0.01055  3.68954E-02 0.01026 ];
SM149_CAPT                (idx, [1:   4]) = [  9.81419E+15 0.02070  9.63284E-03 0.02050 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS    (idx, [1:  2])  = [ 500676 5.00000E+05 ];
BALA_SRC_NEUTRON_NXN     (idx, [1:  2])  = [ 0 2.49773E+01 ];
BALA_SRC_NEUTRON_VR      (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT     (idx, [1:  2])  = [ 500676 5.00025E+05 ];

BALA_LOSS_NEUTRON_CAPT    (idx, [1:  2])  = [ 250637 2.50292E+05 ];
BALA_LOSS_NEUTRON_FISS    (idx, [1:  2])  = [ 227407 2.27131E+05 ];
BALA_LOSS_NEUTRON_LEAK    (idx, [1:  2])  = [ 22632 2.26022E+04 ];
BALA_LOSS_NEUTRON_CUT     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_ERR     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT     (idx, [1:  2])  = [ 500676 5.00025E+05 ];

BALA_NEUTRON_DIFF         (idx, [1:  2])  = [ 0 -5.23869E-10 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   6]) = [  3.00000E+07 0.0E+00  3.00000E+07 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_POWDENS               (idx, [1:   6]) = [  9.26200E-03 2.6E-09  9.26200E-03 2.6E-09  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   6]) = [  2.29263E+18 9.9E-05  2.29263E+18 9.9E-05  0.00000E+00 0.0E+00 ];
TOT_FISSRATE              (idx, [1:   6]) = [  9.22772E+17 2.0E-05  9.22772E+17 2.0E-05  0.00000E+00 0.0E+00 ];
TOT_CAPTRATE              (idx, [1:   6]) = [  1.01860E+18 0.00287  6.30934E+17 0.00330  3.87669E+17 0.00399 ];
TOT_ABSRATE               (idx, [1:   6]) = [  1.94137E+18 0.00150  1.55371E+18 0.00134  3.87669E+17 0.00399 ];
TOT_SRCRATE               (idx, [1:   6]) = [  2.03325E+18 0.00152  2.03325E+18 0.00152  0.00000E+00 0.0E+00 ];
TOT_FLUX                  (idx, [1:   6]) = [  1.85095E+21 0.00218  5.13352E+18 0.00188  1.84582E+21 0.00218 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  9.19745E+16 0.00710 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  2.03335E+18 0.00152 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  7.59706E+20 0.00221 ];
INI_FMASS                 (idx, 1)        =  3.23904E+03 ;
TOT_FMASS                 (idx, 1)        =  3.23889E+03 ;
INI_BURN_FMASS            (idx, 1)        =  3.23904E+03 ;
TOT_BURN_FMASS            (idx, 1)        =  3.23889E+03 ;

% Six-factor formula:

SIX_FF_ETA                (idx, [1:   2]) = [  1.74177E+00 0.00119 ];
SIX_FF_F                  (idx, [1:   2]) = [  7.72273E-01 0.00089 ];
SIX_FF_P                  (idx, [1:   2]) = [  8.49717E-01 0.00059 ];
SIX_FF_EPSILON            (idx, [1:   2]) = [  1.03429E+00 0.00038 ];
SIX_FF_LF                 (idx, [1:   2]) = [  9.99776E-01 2.0E-05 ];
SIX_FF_LT                 (idx, [1:   2]) = [  9.55009E-01 0.00032 ];
SIX_FF_KINF               (idx, [1:   2]) = [  1.18206E+00 0.00151 ];
SIX_FF_KEFF               (idx, [1:   2]) = [  1.12862E+00 0.00153 ];

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.48450E+00 0.00012 ];
FISSE                     (idx, [1:   2]) = [  2.02916E+02 2.0E-05 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.12894E+00 0.00162  7.00920E-02 0.00153  4.46496E-04 0.02614 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.12862E+00 0.00153 ];
COL_KEFF                  (idx, [1:   2]) = [  1.12862E+00 0.00153 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.12862E+00 0.00153 ];
ABS_KINF                  (idx, [1:   2]) = [  1.18206E+00 0.00151 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.90160E+01 0.00018 ];
IMP_ALF                   (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  1.10555E-07 0.00355 ];
IMP_EALF                  (idx, [1:   2]) = [  2.00000E+01 0.0E+00 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  8.24250E-03 0.04813 ];
IMP_AFGE                  (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% Forward-weighted delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 6 ;
FWD_ANA_BETA_ZERO         (idx, [1:  14]) = [  5.49639E-03 0.01838  2.09319E-04 0.10569  1.06110E-03 0.04182  9.45579E-04 0.04204  2.13123E-03 0.02952  7.81808E-04 0.04924  3.67363E-04 0.06943 ];
FWD_ANA_LAMBDA            (idx, [1:  14]) = [  4.53763E-01 0.02901  3.13317E-03 0.09033  2.48089E-02 0.02814  9.14471E-02 0.02814  2.85788E-01 0.01208  5.72390E-01 0.03494  1.15493E+00 0.06069 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  14]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  14]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Adjoint weighted time constants using Nauchi's method:

IFP_CHAIN_LENGTH          (idx, 1)        = 15 ;
ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  1.18311E-03 0.00354  1.18324E-03 0.00354  1.03365E-03 0.04402 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  1.33413E-03 0.00306  1.33429E-03 0.00307  1.16308E-03 0.04380 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  14]) = [  6.31171E-03 0.02659  2.50117E-04 0.14378  1.21634E-03 0.05979  1.00901E-03 0.06888  2.47354E-03 0.04268  9.16788E-04 0.07106  4.45912E-04 0.10389 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  14]) = [  4.66875E-01 0.04495  1.33344E-02 9.9E-05  3.26636E-02 0.00073  1.20254E-01 0.00112  3.02450E-01 0.00046  8.50785E-01 0.00063  2.85295E+00 0.00155 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  1.15054E-03 0.00794  1.15061E-03 0.00798  6.01834E-04 0.09364 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  1.29689E-03 0.00762  1.29696E-03 0.00765  6.76570E-04 0.09352 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  14]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  14]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  14]) = [  6.29860E-03 0.07771  2.84463E-04 0.38248  1.22941E-03 0.18912  1.32939E-03 0.20055  2.21246E-03 0.13355  8.48004E-04 0.19994  3.94879E-04 0.26758 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  14]) = [  5.03250E-01 0.10004  1.33360E-02 5.5E-09  3.26182E-02 0.00212  1.20802E-01 0.00066  3.02663E-01 0.00039  8.53201E-01 0.00253  2.84684E+00 0.00217 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  1.16898E-03 0.00231 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  1.31823E-03 0.00152 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  6.36928E-03 0.01359 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -5.45746E+00 0.01375 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  1.66581E-06 0.00055 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  3.01338E-05 0.00046  3.01334E-05 0.00046  3.01602E-05 0.00679 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  1.73715E-03 0.00190  1.73744E-03 0.00191  1.68529E-03 0.02544 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  8.57518E-01 0.00057  8.56958E-01 0.00059  1.12429E+00 0.03223 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.19095E+01 0.04658 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  3.73605E+02 0.00149  3.47702E+02 0.00195 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.32' ;
COMPILE_DATE              (idx, [1: 20])  = 'Oct 21 2021 21:31:23' ;
DEBUG                     (idx, 1)        = 0 ;
TITLE                     (idx, [1:  8])  = 'Untitled' ;
CONFIDENTIAL_DATA         (idx, 1)        = 0 ;
INPUT_FILE_NAME           (idx, [1: 14])  = 'pbr_run_in.inp' ;
WORKING_DIRECTORY         (idx, [1: 60])  = '/home/stewryan/projects/NEAMS/pebshufpy/examples/auto_run_in' ;
HOSTNAME                  (idx, [1:  9])  = 'lemhi0447' ;
CPU_TYPE                  (idx, [1: 40])  = 'Intel(R) Xeon(R) Gold 6148 CPU @ 2.40GHz' ;
CPU_MHZ                   (idx, 1)        = 33581830.0 ;
START_DATE                (idx, [1: 24])  = 'Thu Mar  3 11:06:38 2022' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Mar  3 11:13:05 2022' ;

% Run parameters:

POP                       (idx, 1)        = 5000 ;
CYCLES                    (idx, 1)        = 100 ;
SKIP                      (idx, 1)        = 20 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1646330798446 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 0 ;
B1_CALCULATION            (idx, [1:  3])  = [ 0 0 0 ];
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;

CRIT_SPEC_MODE            (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 2 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 0 ;
DOUBLE_INDEXING           (idx, 1)        = 0 ;
MG_MAJORANT_MODE          (idx, 1)        = 1 ;
SPECTRUM_COLLAPSE         (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 4 ;
OMP_THREADS               (idx, 1)        = 40 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  40]) = [  9.96751E-01  9.74116E-01  1.01992E+00  1.01646E+00  1.02631E+00  1.03483E+00  9.74915E-01  9.98349E-01  9.49084E-01  1.02285E+00  1.01965E+00  1.03403E+00  9.63730E-01  9.89295E-01  1.03963E+00  1.04069E+00  9.79708E-01  9.63198E-01  9.85833E-01  9.60801E-01  9.67192E-01  1.01726E+00  9.80773E-01  1.03084E+00  9.82904E-01  9.60801E-01  1.02205E+00  1.00581E+00  1.03856E+00  1.02924E+00  1.01805E+00  9.64263E-01  1.00900E+00  1.03430E+00  1.00048E+00  9.86632E-01  9.84768E-01  9.78377E-01  9.81040E-01  1.01752E+00  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;
OMP_SHARED_QUEUE_LIM      (idx, 1)        = 0 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 64])  = '/hpc-common/data/serpent/xsdata/endfb71_edep/endfb71_edep.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 46])  = '/hpc-common/data/serpent/xsdata/sss_endfb7.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 46])  = '/hpc-common/data/serpent/xsdata/sss_endfb7.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 46])  = '/hpc-common/data/serpent/xsdata/sss_endfb7.nfy' ;
BRA_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:   4]) = [  5.00000E-02 0.0E+00  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  9.49131E-01 7.3E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  5.08691E-02 0.00135  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  2.97588E-01 0.00024  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  9.97929E-01 5.1E-06  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  7.37924E-01 0.00038  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  3.34836E+01 0.00151  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  3.73956E+02 0.00142  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  3.73911E+02 0.00142  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.31671E+02 0.00036  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  3.18205E+03 0.00145  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 100 ;
SIMULATED_HISTORIES       (idx, 1)        = 125208 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  1.25179E+03 0.00232 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  1.25179E+03 0.00232 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  1.05571E+02 ;
RUNNING_TIME              (idx, 1)        =  6.45562E+00 ;
INIT_TIME                 (idx, [1:  2])  = [  1.34072E+00  1.34072E+00 ];
PROCESS_TIME              (idx, [1:  2])  = [  2.00667E-02  2.55000E-03 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  5.08000E+00  8.96050E-01  1.07798E+00 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  8.93333E-03  2.71667E-03 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  4.56667E-03  1.15000E-03 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  5.95683E-01  8.45167E-02 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  6.36977E+00  1.25065E+01 ];
CPU_USAGE                 (idx, 1)        = 16.35337 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  3.81196E+01 0.00665 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  3.48090E-01 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 192031.22 ;
ALLOC_MEMSIZE             (idx, 1)        = 28280.46;
MEMSIZE                   (idx, 1)        = 27989.25;
XS_MEMSIZE                (idx, 1)        = 23187.29;
MAT_MEMSIZE               (idx, 1)        = 138.58;
RES_MEMSIZE               (idx, 1)        = 16.29;
IFC_MEMSIZE               (idx, 1)        = 0.00;
MISC_MEMSIZE              (idx, 1)        = 4647.09;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 291.21;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 1518 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  5.00000E-05 ;
NEUTRON_ERG_NE            (idx, 1)        = 413898 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Unresolved resonance probability table sampling:

URES_DILU_CUT             (idx, 1)        =  1.00000E-09 ;
URES_EMIN                 (idx, 1)        =  1.00000E+37 ;
URES_EMAX                 (idx, 1)        = -1.00000E+37 ;
URES_AVAIL                (idx, 1)        = 244 ;
URES_USED                 (idx, 1)        = 0 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 1889 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 728 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 1161 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 18115 ;
TOT_TRANSMU_REA           (idx, 1)        = 3087 ;

% Neutron physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 0 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_PREPROCESSOR      (idx, 1)        = 1 ;
TMS_MODE                  (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Energy deposition:

EDEP_MODE                 (idx, 1)        = 0 ;
EDEP_DELAYED              (idx, 1)        = 1 ;
EDEP_KEFF_CORR            (idx, 1)        = 1 ;
EDEP_LOCAL_EGD            (idx, 1)        = 0 ;
EDEP_COMP                 (idx, [1:  9])  = [ 0 0 0 0 0 0 0 0 0 ];
EDEP_CAPT_E               (idx, 1)        =  0.00000E+00 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  5.88737E+18 ;
TOT_DECAY_HEAT            (idx, 1)        =  1.87148E+06 ;
TOT_SF_RATE               (idx, 1)        =  3.21722E+06 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  6.55743E+17 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  4.52744E+04 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  5.23163E+18 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  1.82620E+06 ;
INHALATION_TOXICITY       (idx, 1)        =  8.78112E+09 ;
INGESTION_TOXICITY        (idx, 1)        =  2.96408E+09 ;
ACTINIDE_INH_TOX          (idx, 1)        =  3.24912E+09 ;
ACTINIDE_ING_TOX          (idx, 1)        =  2.74354E+08 ;
FISSION_PRODUCT_INH_TOX   (idx, 1)        =  5.53200E+09 ;
FISSION_PRODUCT_ING_TOX   (idx, 1)        =  2.68972E+09 ;
SR90_ACTIVITY             (idx, 1)        =  2.36279E+15 ;
TE132_ACTIVITY            (idx, 1)        =  4.05695E+16 ;
I131_ACTIVITY             (idx, 1)        =  2.79170E+16 ;
I132_ACTIVITY             (idx, 1)        =  4.10157E+16 ;
CS134_ACTIVITY            (idx, 1)        =  2.50154E+14 ;
CS137_ACTIVITY            (idx, 1)        =  2.54656E+15 ;
PHOTON_DECAY_SOURCE       (idx, 1)        =  4.91380E+18 ;
NEUTRON_DECAY_SOURCE      (idx, 1)        =  9.70958E+15 ;
ALPHA_DECAY_SOURCE        (idx, 1)        =  3.19094E+13 ;
ELECTRON_DECAY_SOURCE     (idx, 1)        =  7.03301E+18 ;

% Normalization coefficient:

NORM_COEF                 (idx, [1:   4]) = [  1.64219E+15 0.00166  0.00000E+00 0.0E+00 ];

% Parameters for burnup calculation:

BURN_MATERIALS            (idx, 1)        = 55 ;
BURN_MODE                 (idx, 1)        = 2 ;
BURN_STEP                 (idx, 1)        = 2 ;
BURN_RANDOMIZE_DATA       (idx, [1:  3])  = [ 0 0 0 ];
BURNUP                    (idx, [1:  2])  = [  2.77860E-01  2.78480E-01 ];
BURN_DAYS                 (idx, [1:  2])  = [  3.00000E+01  2.50000E+01 ];
FIMA                      (idx, [1:  3])  = [  2.92392E-04  2.39711E+24  8.19590E+27 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  3.10036E-01 0.00389 ];
U235_FISS                 (idx, [1:   4]) = [  8.06031E+17 0.00089  8.73847E-01 0.00087 ];
U238_FISS                 (idx, [1:   4]) = [  2.09610E+15 0.04573  2.27250E-03 0.04573 ];
PU239_FISS                (idx, [1:   4]) = [  1.11637E+17 0.00613  1.21037E-01 0.00615 ];
PU240_FISS                (idx, [1:   4]) = [  3.91687E+12 1.00000  4.24448E-06 1.00000 ];
PU241_FISS                (idx, [1:   4]) = [  2.54189E+15 0.04360  2.75605E-03 0.04361 ];
U235_CAPT                 (idx, [1:   4]) = [  1.54022E+17 0.00582  1.48372E-01 0.00481 ];
U238_CAPT                 (idx, [1:   4]) = [  3.26292E+17 0.00423  3.14466E-01 0.00306 ];
PU239_CAPT                (idx, [1:   4]) = [  6.53709E+16 0.00807  6.30270E-02 0.00764 ];
PU240_CAPT                (idx, [1:   4]) = [  1.16048E+16 0.01844  1.11672E-02 0.01796 ];
PU241_CAPT                (idx, [1:   4]) = [  9.27759E+14 0.06662  8.97721E-04 0.06665 ];
XE135_CAPT                (idx, [1:   4]) = [  3.85068E+16 0.01031  3.71241E-02 0.00996 ];
SM149_CAPT                (idx, [1:   4]) = [  1.02361E+16 0.02068  9.88075E-03 0.02055 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS    (idx, [1:  2])  = [ 500717 5.00000E+05 ];
BALA_SRC_NEUTRON_NXN     (idx, [1:  2])  = [ 0 2.49825E+01 ];
BALA_SRC_NEUTRON_VR      (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT     (idx, [1:  2])  = [ 500717 5.00025E+05 ];

BALA_LOSS_NEUTRON_CAPT    (idx, [1:  2])  = [ 252889 2.52563E+05 ];
BALA_LOSS_NEUTRON_FISS    (idx, [1:  2])  = [ 225261 2.24918E+05 ];
BALA_LOSS_NEUTRON_LEAK    (idx, [1:  2])  = [ 22567 2.25437E+04 ];
BALA_LOSS_NEUTRON_CUT     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_ERR     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT     (idx, [1:  2])  = [ 500717 5.00025E+05 ];

BALA_NEUTRON_DIFF         (idx, [1:  2])  = [ 0 1.16415E-10 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   6]) = [  3.00000E+07 0.0E+00  3.00000E+07 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_POWDENS               (idx, [1:   6]) = [  9.26200E-03 2.6E-09  9.26200E-03 2.6E-09  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   6]) = [  2.29742E+18 0.00011  2.29742E+18 0.00011  0.00000E+00 0.0E+00 ];
TOT_FISSRATE              (idx, [1:   6]) = [  9.22387E+17 2.2E-05  9.22387E+17 2.2E-05  0.00000E+00 0.0E+00 ];
TOT_CAPTRATE              (idx, [1:   6]) = [  1.03782E+18 0.00308  6.45858E+17 0.00336  3.91965E+17 0.00427 ];
TOT_ABSRATE               (idx, [1:   6]) = [  1.96021E+18 0.00163  1.56824E+18 0.00138  3.91965E+17 0.00427 ];
TOT_SRCRATE               (idx, [1:   6]) = [  2.05274E+18 0.00166  2.05274E+18 0.00166  0.00000E+00 0.0E+00 ];
TOT_FLUX                  (idx, [1:   6]) = [  1.86648E+21 0.00222  5.18888E+18 0.00180  1.86129E+21 0.00223 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  9.26301E+16 0.00742 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  2.05284E+18 0.00166 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  7.66033E+20 0.00225 ];
INI_FMASS                 (idx, 1)        =  3.23904E+03 ;
TOT_FMASS                 (idx, 1)        =  3.23811E+03 ;
INI_BURN_FMASS            (idx, 1)        =  3.23904E+03 ;
TOT_BURN_FMASS            (idx, 1)        =  3.23811E+03 ;

% Six-factor formula:

SIX_FF_ETA                (idx, [1:   2]) = [  1.73206E+00 0.00116 ];
SIX_FF_F                  (idx, [1:   2]) = [  7.72191E-01 0.00094 ];
SIX_FF_P                  (idx, [1:   2]) = [  8.49294E-01 0.00061 ];
SIX_FF_EPSILON            (idx, [1:   2]) = [  1.03295E+00 0.00039 ];
SIX_FF_LF                 (idx, [1:   2]) = [  9.99794E-01 2.0E-05 ];
SIX_FF_LT                 (idx, [1:   2]) = [  9.55109E-01 0.00033 ];
SIX_FF_KINF               (idx, [1:   2]) = [  1.17332E+00 0.00163 ];
SIX_FF_KEFF               (idx, [1:   2]) = [  1.12042E+00 0.00166 ];

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.49074E+00 0.00013 ];
FISSE                     (idx, [1:   2]) = [  2.03001E+02 2.2E-05 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.12112E+00 0.00168  6.96175E-02 0.00166  4.08732E-04 0.02961 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.12042E+00 0.00166 ];
COL_KEFF                  (idx, [1:   2]) = [  1.12042E+00 0.00166 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.12042E+00 0.00166 ];
ABS_KINF                  (idx, [1:   2]) = [  1.17332E+00 0.00163 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.90194E+01 0.00019 ];
IMP_ALF                   (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  1.10205E-07 0.00373 ];
IMP_EALF                  (idx, [1:   2]) = [  2.00000E+01 0.0E+00 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  7.69041E-03 0.04959 ];
IMP_AFGE                  (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% Forward-weighted delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 6 ;
FWD_ANA_BETA_ZERO         (idx, [1:  14]) = [  5.17937E-03 0.02077  1.52169E-04 0.10681  9.68983E-04 0.04416  9.42671E-04 0.04380  1.95983E-03 0.03257  8.02473E-04 0.04825  3.53241E-04 0.07007 ];
FWD_ANA_LAMBDA            (idx, [1:  14]) = [  4.77548E-01 0.03135  2.60069E-03 0.10172  2.37921E-02 0.03046  8.80663E-02 0.03026  2.82752E-01 0.01320  5.65481E-01 0.03553  1.13843E+00 0.06132 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  14]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  14]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Adjoint weighted time constants using Nauchi's method:

IFP_CHAIN_LENGTH          (idx, 1)        = 15 ;
ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  1.19220E-03 0.00345  1.19223E-03 0.00346  1.10918E-03 0.04485 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  1.33518E-03 0.00306  1.33522E-03 0.00307  1.24161E-03 0.04475 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  14]) = [  5.84969E-03 0.03021  2.14263E-04 0.14297  1.04702E-03 0.06660  1.04677E-03 0.06419  2.17583E-03 0.05035  9.34580E-04 0.07248  4.31238E-04 0.10773 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  14]) = [  4.87729E-01 0.04898  1.33374E-02 0.00024  3.26257E-02 0.00096  1.20270E-01 0.00105  3.02511E-01 0.00041  8.50477E-01 0.00047  2.84557E+00 0.00114 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  1.15306E-03 0.00805  1.15366E-03 0.00801  4.35223E-04 0.10969 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  1.29142E-03 0.00790  1.29210E-03 0.00786  4.88123E-04 0.11018 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  14]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  14]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  14]) = [  5.78428E-03 0.08477  6.17275E-05 0.64340  1.22909E-03 0.17249  1.00666E-03 0.22986  2.41615E-03 0.13200  7.45210E-04 0.20025  3.25434E-04 0.30311 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  14]) = [  4.66531E-01 0.11077  1.33360E-02 0.0E+00  3.26178E-02 0.00210  1.20555E-01 0.00186  3.03070E-01 0.00129  8.49732E-01 0.00029  2.83656E+00 0.00395 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  1.16797E-03 0.00235 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  1.30794E-03 0.00163 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  5.68121E-03 0.01705 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -4.88975E+00 0.01776 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  1.66489E-06 0.00054 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  3.01443E-05 0.00046  3.01447E-05 0.00047  2.98547E-05 0.00764 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  1.73552E-03 0.00183  1.73583E-03 0.00183  1.65503E-03 0.02482 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  8.57039E-01 0.00058  8.56511E-01 0.00060  1.19513E+00 0.04387 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.12358E+01 0.04616 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  3.73137E+02 0.00142  3.47436E+02 0.00170 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.32' ;
COMPILE_DATE              (idx, [1: 20])  = 'Oct 21 2021 21:31:23' ;
DEBUG                     (idx, 1)        = 0 ;
TITLE                     (idx, [1:  8])  = 'Untitled' ;
CONFIDENTIAL_DATA         (idx, 1)        = 0 ;
INPUT_FILE_NAME           (idx, [1: 14])  = 'pbr_run_in.inp' ;
WORKING_DIRECTORY         (idx, [1: 60])  = '/home/stewryan/projects/NEAMS/pebshufpy/examples/auto_run_in' ;
HOSTNAME                  (idx, [1:  9])  = 'lemhi0447' ;
CPU_TYPE                  (idx, [1: 40])  = 'Intel(R) Xeon(R) Gold 6148 CPU @ 2.40GHz' ;
CPU_MHZ                   (idx, 1)        = 33581830.0 ;
START_DATE                (idx, [1: 24])  = 'Thu Mar  3 11:06:38 2022' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Mar  3 11:15:05 2022' ;

% Run parameters:

POP                       (idx, 1)        = 5000 ;
CYCLES                    (idx, 1)        = 100 ;
SKIP                      (idx, 1)        = 20 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1646330798446 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 0 ;
B1_CALCULATION            (idx, [1:  3])  = [ 0 0 0 ];
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;

CRIT_SPEC_MODE            (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 2 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 0 ;
DOUBLE_INDEXING           (idx, 1)        = 0 ;
MG_MAJORANT_MODE          (idx, 1)        = 1 ;
SPECTRUM_COLLAPSE         (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 4 ;
OMP_THREADS               (idx, 1)        = 40 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  40]) = [  1.02544E+00  9.96686E-01  1.04514E+00  9.92959E-01  1.04780E+00  9.97751E-01  9.78850E-01  1.01745E+00  9.71928E-01  1.00334E+00  1.03156E+00  1.00893E+00  9.58352E-01  9.94556E-01  9.84440E-01  1.01585E+00  9.63410E-01  9.78317E-01  9.90297E-01  9.80979E-01  9.90563E-01  1.02783E+00  9.89232E-01  9.79915E-01  9.90030E-01  9.74058E-01  1.03688E+00  9.81246E-01  1.00494E+00  1.03129E+00  1.02650E+00  9.99082E-01  1.01026E+00  1.01106E+00  9.65805E-01  9.77252E-01  1.00414E+00  9.81246E-01  9.90030E-01  1.04460E+00  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;
OMP_SHARED_QUEUE_LIM      (idx, 1)        = 0 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 64])  = '/hpc-common/data/serpent/xsdata/endfb71_edep/endfb71_edep.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 46])  = '/hpc-common/data/serpent/xsdata/sss_endfb7.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 46])  = '/hpc-common/data/serpent/xsdata/sss_endfb7.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 46])  = '/hpc-common/data/serpent/xsdata/sss_endfb7.nfy' ;
BRA_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:   4]) = [  5.00000E-02 0.0E+00  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  9.49094E-01 7.5E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  5.09056E-02 0.00140  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  2.97493E-01 0.00023  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  9.97942E-01 5.3E-06  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  7.39008E-01 0.00040  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  3.34509E+01 0.00147  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  3.76034E+02 0.00154  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  3.75988E+02 0.00154  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.31650E+02 0.00036  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  3.17648E+03 0.00151  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 100 ;
SIMULATED_HISTORIES       (idx, 1)        = 125146 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  1.25124E+03 0.00238 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  1.25124E+03 0.00238 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  1.48071E+02 ;
RUNNING_TIME              (idx, 1)        =  8.45323E+00 ;
INIT_TIME                 (idx, [1:  2])  = [  1.34072E+00  1.34072E+00 ];
PROCESS_TIME              (idx, [1:  2])  = [  2.49167E-02  2.26667E-03 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  7.06643E+00  9.25783E-01  1.06065E+00 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  1.24833E-02  1.85000E-03 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  7.05000E-03  1.28334E-03 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  8.16450E-01  1.12000E-01 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  8.33942E+00  1.22693E+01 ];
CPU_USAGE                 (idx, 1)        = 17.51654 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  3.80375E+01 0.00666 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  3.71160E-01 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 192031.22 ;
ALLOC_MEMSIZE             (idx, 1)        = 28280.46;
MEMSIZE                   (idx, 1)        = 27989.25;
XS_MEMSIZE                (idx, 1)        = 23187.29;
MAT_MEMSIZE               (idx, 1)        = 138.58;
RES_MEMSIZE               (idx, 1)        = 16.29;
IFC_MEMSIZE               (idx, 1)        = 0.00;
MISC_MEMSIZE              (idx, 1)        = 4647.09;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 291.21;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 1518 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  5.00000E-05 ;
NEUTRON_ERG_NE            (idx, 1)        = 413898 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Unresolved resonance probability table sampling:

URES_DILU_CUT             (idx, 1)        =  1.00000E-09 ;
URES_EMIN                 (idx, 1)        =  1.00000E+37 ;
URES_EMAX                 (idx, 1)        = -1.00000E+37 ;
URES_AVAIL                (idx, 1)        = 244 ;
URES_USED                 (idx, 1)        = 0 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 1889 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 728 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 1161 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 18115 ;
TOT_TRANSMU_REA           (idx, 1)        = 3087 ;

% Neutron physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 0 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_PREPROCESSOR      (idx, 1)        = 1 ;
TMS_MODE                  (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Energy deposition:

EDEP_MODE                 (idx, 1)        = 0 ;
EDEP_DELAYED              (idx, 1)        = 1 ;
EDEP_KEFF_CORR            (idx, 1)        = 1 ;
EDEP_LOCAL_EGD            (idx, 1)        = 0 ;
EDEP_COMP                 (idx, [1:  9])  = [ 0 0 0 0 0 0 0 0 0 ];
EDEP_CAPT_E               (idx, 1)        =  0.00000E+00 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  5.87104E+18 ;
TOT_DECAY_HEAT            (idx, 1)        =  1.86107E+06 ;
TOT_SF_RATE               (idx, 1)        =  3.37131E+06 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  6.62055E+17 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  4.57105E+04 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  5.20899E+18 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  1.81536E+06 ;
INHALATION_TOXICITY       (idx, 1)        =  9.04380E+09 ;
INGESTION_TOXICITY        (idx, 1)        =  2.96069E+09 ;
ACTINIDE_INH_TOX          (idx, 1)        =  3.45529E+09 ;
ACTINIDE_ING_TOX          (idx, 1)        =  2.77429E+08 ;
FISSION_PRODUCT_INH_TOX   (idx, 1)        =  5.58851E+09 ;
FISSION_PRODUCT_ING_TOX   (idx, 1)        =  2.68327E+09 ;
SR90_ACTIVITY             (idx, 1)        =  2.45472E+15 ;
TE132_ACTIVITY            (idx, 1)        =  4.05403E+16 ;
I131_ACTIVITY             (idx, 1)        =  2.77633E+16 ;
I132_ACTIVITY             (idx, 1)        =  4.10138E+16 ;
CS134_ACTIVITY            (idx, 1)        =  2.71937E+14 ;
CS137_ACTIVITY            (idx, 1)        =  2.65065E+15 ;
PHOTON_DECAY_SOURCE       (idx, 1)        =  4.90197E+18 ;
NEUTRON_DECAY_SOURCE      (idx, 1)        =  9.59889E+15 ;
ALPHA_DECAY_SOURCE        (idx, 1)        =  3.48683E+13 ;
ELECTRON_DECAY_SOURCE     (idx, 1)        =  7.02837E+18 ;

% Normalization coefficient:

NORM_COEF                 (idx, [1:   4]) = [  1.65255E+15 0.00164  0.00000E+00 0.0E+00 ];

% Parameters for burnup calculation:

BURN_MATERIALS            (idx, 1)        = 55 ;
BURN_MODE                 (idx, 1)        = 2 ;
BURN_STEP                 (idx, 1)        = 3 ;
BURN_RANDOMIZE_DATA       (idx, [1:  3])  = [ 0 0 0 ];
BURNUP                    (idx, [1:  2])  = [  5.55720E-01  5.56484E-01 ];
BURN_DAYS                 (idx, [1:  2])  = [  6.00000E+01  3.00000E+01 ];
FIMA                      (idx, [1:  3])  = [  5.84147E-04  4.78901E+24  8.19350E+27 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  3.11550E-01 0.00381 ];
U235_FISS                 (idx, [1:   4]) = [  7.97900E+17 0.00091  8.65245E-01 0.00089 ];
U238_FISS                 (idx, [1:   4]) = [  2.24240E+15 0.04242  2.43166E-03 0.04242 ];
PU239_FISS                (idx, [1:   4]) = [  1.19220E+17 0.00588  1.29290E-01 0.00590 ];
PU241_FISS                (idx, [1:   4]) = [  2.73504E+15 0.03911  2.96620E-03 0.03912 ];
U235_CAPT                 (idx, [1:   4]) = [  1.51219E+17 0.00604  1.44019E-01 0.00509 ];
U238_CAPT                 (idx, [1:   4]) = [  3.26827E+17 0.00406  3.11412E-01 0.00295 ];
PU239_CAPT                (idx, [1:   4]) = [  6.99407E+16 0.00815  6.65698E-02 0.00723 ];
PU240_CAPT                (idx, [1:   4]) = [  1.33316E+16 0.01827  1.27003E-02 0.01794 ];
PU241_CAPT                (idx, [1:   4]) = [  1.13112E+15 0.06249  1.07272E-03 0.06241 ];
XE135_CAPT                (idx, [1:   4]) = [  3.81603E+16 0.01119  3.63862E-02 0.01087 ];
SM149_CAPT                (idx, [1:   4]) = [  1.04800E+16 0.02022  9.99264E-03 0.02013 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS    (idx, [1:  2])  = [ 500497 5.00000E+05 ];
BALA_SRC_NEUTRON_NXN     (idx, [1:  2])  = [ 0 1.66490E+01 ];
BALA_SRC_NEUTRON_VR      (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT     (idx, [1:  2])  = [ 500497 5.00017E+05 ];

BALA_LOSS_NEUTRON_CAPT    (idx, [1:  2])  = [ 254119 2.53873E+05 ];
BALA_LOSS_NEUTRON_FISS    (idx, [1:  2])  = [ 223652 2.23449E+05 ];
BALA_LOSS_NEUTRON_LEAK    (idx, [1:  2])  = [ 22726 2.26947E+04 ];
BALA_LOSS_NEUTRON_CUT     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_ERR     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT     (idx, [1:  2])  = [ 500497 5.00017E+05 ];

BALA_NEUTRON_DIFF         (idx, [1:  2])  = [ 0 -4.07454E-10 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   6]) = [  3.00000E+07 0.0E+00  3.00000E+07 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_POWDENS               (idx, [1:   6]) = [  9.26200E-03 2.6E-09  9.26200E-03 2.6E-09  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   6]) = [  2.30027E+18 0.00011  2.30027E+18 0.00011  0.00000E+00 0.0E+00 ];
TOT_FISSRATE              (idx, [1:   6]) = [  9.22159E+17 2.2E-05  9.22159E+17 2.2E-05  0.00000E+00 0.0E+00 ];
TOT_CAPTRATE              (idx, [1:   6]) = [  1.04973E+18 0.00300  6.52161E+17 0.00345  3.97571E+17 0.00414 ];
TOT_ABSRATE               (idx, [1:   6]) = [  1.97189E+18 0.00160  1.57432E+18 0.00143  3.97571E+17 0.00414 ];
TOT_SRCRATE               (idx, [1:   6]) = [  2.06568E+18 0.00164  2.06568E+18 0.00164  0.00000E+00 0.0E+00 ];
TOT_FLUX                  (idx, [1:   6]) = [  1.88846E+21 0.00234  5.20768E+18 0.00188  1.88326E+21 0.00234 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  9.38604E+16 0.00765 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  2.06575E+18 0.00164 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  7.75172E+20 0.00236 ];
INI_FMASS                 (idx, 1)        =  3.23904E+03 ;
TOT_FMASS                 (idx, 1)        =  3.23717E+03 ;
INI_BURN_FMASS            (idx, 1)        =  3.23904E+03 ;
TOT_BURN_FMASS            (idx, 1)        =  3.23717E+03 ;

% Six-factor formula:

SIX_FF_ETA                (idx, [1:   2]) = [  1.72927E+00 0.00124 ];
SIX_FF_F                  (idx, [1:   2]) = [  7.70459E-01 0.00091 ];
SIX_FF_P                  (idx, [1:   2]) = [  8.48236E-01 0.00063 ];
SIX_FF_EPSILON            (idx, [1:   2]) = [  1.03336E+00 0.00038 ];
SIX_FF_LF                 (idx, [1:   2]) = [  9.99790E-01 2.0E-05 ];
SIX_FF_LT                 (idx, [1:   2]) = [  9.54811E-01 0.00034 ];
SIX_FF_KINF               (idx, [1:   2]) = [  1.16775E+00 0.00159 ];
SIX_FF_KEFF               (idx, [1:   2]) = [  1.11475E+00 0.00163 ];

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.49444E+00 0.00013 ];
FISSE                     (idx, [1:   2]) = [  2.03051E+02 2.2E-05 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.11482E+00 0.00167  6.92588E-02 0.00163  4.12982E-04 0.02799 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.11475E+00 0.00163 ];
COL_KEFF                  (idx, [1:   2]) = [  1.11475E+00 0.00163 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.11475E+00 0.00163 ];
ABS_KINF                  (idx, [1:   2]) = [  1.16775E+00 0.00159 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.90082E+01 0.00018 ];
IMP_ALF                   (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  1.11408E-07 0.00348 ];
IMP_EALF                  (idx, [1:   2]) = [  2.00000E+01 0.0E+00 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  8.22079E-03 0.04521 ];
IMP_AFGE                  (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% Forward-weighted delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 6 ;
FWD_ANA_BETA_ZERO         (idx, [1:  14]) = [  5.31797E-03 0.01764  1.63830E-04 0.10078  9.41537E-04 0.04490  9.72964E-04 0.04152  2.01269E-03 0.02892  8.91026E-04 0.04620  3.35914E-04 0.07172 ];
FWD_ANA_LAMBDA            (idx, [1:  14]) = [  4.62694E-01 0.02884  2.83357E-03 0.09637  2.33695E-02 0.03142  9.21408E-02 0.02775  2.84922E-01 0.01237  5.97881E-01 0.03258  1.06847E+00 0.06464 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  14]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  14]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Adjoint weighted time constants using Nauchi's method:

IFP_CHAIN_LENGTH          (idx, 1)        = 15 ;
ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  1.20114E-03 0.00364  1.20105E-03 0.00366  1.10155E-03 0.04651 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  1.33773E-03 0.00331  1.33760E-03 0.00332  1.22939E-03 0.04656 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  14]) = [  5.96107E-03 0.02913  1.81968E-04 0.15676  1.13681E-03 0.06662  1.03687E-03 0.06688  2.24543E-03 0.04541  1.00420E-03 0.06791  3.55801E-04 0.11918 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  14]) = [  4.56908E-01 0.05120  1.33360E-02 3.3E-09  3.25747E-02 0.00114  1.20533E-01 0.00085  3.02160E-01 0.00064  8.51232E-01 0.00065  2.84779E+00 0.00104 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  1.15578E-03 0.00729  1.15613E-03 0.00731  5.15699E-04 0.10019 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  1.28747E-03 0.00724  1.28788E-03 0.00727  5.71433E-04 0.09908 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  14]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  14]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  14]) = [  6.42479E-03 0.08598  1.40237E-04 0.54451  1.02147E-03 0.24522  1.03085E-03 0.19232  2.52537E-03 0.13797  1.15250E-03 0.20192  5.54365E-04 0.34279 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  14]) = [  4.84636E-01 0.10837  1.33360E-02 0.0E+00  3.25164E-02 0.00306  1.20150E-01 0.00283  3.02163E-01 0.00145  8.51503E-01 0.00186  2.85300E+00 0.0E+00 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  1.18427E-03 0.00234 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  1.31867E-03 0.00151 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  5.99507E-03 0.01486 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -5.07955E+00 0.01530 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  1.66860E-06 0.00057 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  3.01334E-05 0.00047  3.01335E-05 0.00047  2.99127E-05 0.00755 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  1.75091E-03 0.00201  1.75077E-03 0.00202  1.77979E-03 0.02686 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  8.56144E-01 0.00060  8.55648E-01 0.00062  1.10699E+00 0.03377 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.04785E+01 0.04070 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  3.75215E+02 0.00154  3.49183E+02 0.00188 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.32' ;
COMPILE_DATE              (idx, [1: 20])  = 'Oct 21 2021 21:31:23' ;
DEBUG                     (idx, 1)        = 0 ;
TITLE                     (idx, [1:  8])  = 'Untitled' ;
CONFIDENTIAL_DATA         (idx, 1)        = 0 ;
INPUT_FILE_NAME           (idx, [1: 14])  = 'pbr_run_in.inp' ;
WORKING_DIRECTORY         (idx, [1: 60])  = '/home/stewryan/projects/NEAMS/pebshufpy/examples/auto_run_in' ;
HOSTNAME                  (idx, [1:  9])  = 'lemhi0447' ;
CPU_TYPE                  (idx, [1: 40])  = 'Intel(R) Xeon(R) Gold 6148 CPU @ 2.40GHz' ;
CPU_MHZ                   (idx, 1)        = 33581830.0 ;
START_DATE                (idx, [1: 24])  = 'Thu Mar  3 11:06:38 2022' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Mar  3 11:17:01 2022' ;

% Run parameters:

POP                       (idx, 1)        = 5000 ;
CYCLES                    (idx, 1)        = 100 ;
SKIP                      (idx, 1)        = 20 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1646330798446 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 0 ;
B1_CALCULATION            (idx, [1:  3])  = [ 0 0 0 ];
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;

CRIT_SPEC_MODE            (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 2 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 0 ;
DOUBLE_INDEXING           (idx, 1)        = 0 ;
MG_MAJORANT_MODE          (idx, 1)        = 1 ;
SPECTRUM_COLLAPSE         (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 4 ;
OMP_THREADS               (idx, 1)        = 40 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  40]) = [  1.00540E+00  9.77441E-01  1.00114E+00  1.03176E+00  1.00806E+00  9.87559E-01  1.03549E+00  1.02084E+00  9.66524E-01  1.00859E+00  1.02617E+00  1.02350E+00  9.73980E-01  9.92618E-01  1.02963E+00  9.87026E-01  9.63063E-01  9.97943E-01  9.92352E-01  9.89689E-01  9.93683E-01  9.95813E-01  9.74779E-01  1.03575E+00  9.97943E-01  9.49750E-01  1.00407E+00  9.87559E-01  1.01871E+00  1.04853E+00  9.90488E-01  9.58537E-01  1.00300E+00  1.02643E+00  9.79571E-01  9.88358E-01  1.03815E+00  9.92352E-01  9.79039E-01  1.01871E+00  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;
OMP_SHARED_QUEUE_LIM      (idx, 1)        = 0 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 64])  = '/hpc-common/data/serpent/xsdata/endfb71_edep/endfb71_edep.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 46])  = '/hpc-common/data/serpent/xsdata/sss_endfb7.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 46])  = '/hpc-common/data/serpent/xsdata/sss_endfb7.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 46])  = '/hpc-common/data/serpent/xsdata/sss_endfb7.nfy' ;
BRA_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:   4]) = [  5.00000E-02 6.6E-10  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  9.49230E-01 7.3E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  5.07699E-02 0.00137  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  2.97588E-01 0.00024  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  9.97934E-01 5.1E-06  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  7.39740E-01 0.00037  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  3.35333E+01 0.00144  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  3.77331E+02 0.00142  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  3.77285E+02 0.00142  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.31609E+02 0.00037  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  3.18426E+03 0.00147  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 100 ;
SIMULATED_HISTORIES       (idx, 1)        = 125164 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  1.25092E+03 0.00223 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  1.25092E+03 0.00223 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  1.89792E+02 ;
RUNNING_TIME              (idx, 1)        =  1.03870E+01 ;
INIT_TIME                 (idx, [1:  2])  = [  1.34072E+00  1.34072E+00 ];
PROCESS_TIME              (idx, [1:  2])  = [  2.99500E-02  2.85000E-03 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  8.98805E+00  9.35750E-01  9.85867E-01 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  1.66833E-02  2.41667E-03 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  7.05000E-03  1.28334E-03 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  9.84433E-01  5.66669E-04 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.03848E+01  1.23069E+01 ];
CPU_USAGE                 (idx, 1)        = 18.27197 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  3.81487E+01 0.00646 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  3.87074E-01 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 192031.22 ;
ALLOC_MEMSIZE             (idx, 1)        = 28280.46;
MEMSIZE                   (idx, 1)        = 27989.25;
XS_MEMSIZE                (idx, 1)        = 23187.29;
MAT_MEMSIZE               (idx, 1)        = 138.58;
RES_MEMSIZE               (idx, 1)        = 16.29;
IFC_MEMSIZE               (idx, 1)        = 0.00;
MISC_MEMSIZE              (idx, 1)        = 4647.09;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 291.21;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 1518 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  5.00000E-05 ;
NEUTRON_ERG_NE            (idx, 1)        = 413898 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Unresolved resonance probability table sampling:

URES_DILU_CUT             (idx, 1)        =  1.00000E-09 ;
URES_EMIN                 (idx, 1)        =  1.00000E+37 ;
URES_EMAX                 (idx, 1)        = -1.00000E+37 ;
URES_AVAIL                (idx, 1)        = 244 ;
URES_USED                 (idx, 1)        = 0 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 1889 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 728 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 1161 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 18115 ;
TOT_TRANSMU_REA           (idx, 1)        = 3087 ;

% Neutron physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 0 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_PREPROCESSOR      (idx, 1)        = 1 ;
TMS_MODE                  (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Energy deposition:

EDEP_MODE                 (idx, 1)        = 0 ;
EDEP_DELAYED              (idx, 1)        = 1 ;
EDEP_KEFF_CORR            (idx, 1)        = 1 ;
EDEP_LOCAL_EGD            (idx, 1)        = 0 ;
EDEP_COMP                 (idx, [1:  9])  = [ 0 0 0 0 0 0 0 0 0 ];
EDEP_CAPT_E               (idx, 1)        =  0.00000E+00 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  5.86173E+18 ;
TOT_DECAY_HEAT            (idx, 1)        =  1.85441E+06 ;
TOT_SF_RATE               (idx, 1)        =  3.55839E+06 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  6.66124E+17 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  4.59965E+04 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  5.19560E+18 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  1.80842E+06 ;
INHALATION_TOXICITY       (idx, 1)        =  9.32884E+09 ;
INGESTION_TOXICITY        (idx, 1)        =  2.96653E+09 ;
ACTINIDE_INH_TOX          (idx, 1)        =  3.67538E+09 ;
ACTINIDE_ING_TOX          (idx, 1)        =  2.79575E+08 ;
FISSION_PRODUCT_INH_TOX   (idx, 1)        =  5.65346E+09 ;
FISSION_PRODUCT_ING_TOX   (idx, 1)        =  2.68695E+09 ;
SR90_ACTIVITY             (idx, 1)        =  2.54564E+15 ;
TE132_ACTIVITY            (idx, 1)        =  4.05180E+16 ;
I131_ACTIVITY             (idx, 1)        =  2.77710E+16 ;
I132_ACTIVITY             (idx, 1)        =  4.10103E+16 ;
CS134_ACTIVITY            (idx, 1)        =  2.95590E+14 ;
CS137_ACTIVITY            (idx, 1)        =  2.75440E+15 ;
PHOTON_DECAY_SOURCE       (idx, 1)        =  4.89511E+18 ;
NEUTRON_DECAY_SOURCE      (idx, 1)        =  9.52580E+15 ;
ALPHA_DECAY_SOURCE        (idx, 1)        =  3.83490E+13 ;
ELECTRON_DECAY_SOURCE     (idx, 1)        =  7.02767E+18 ;

% Normalization coefficient:

NORM_COEF                 (idx, [1:   4]) = [  1.66697E+15 0.00155  0.00000E+00 0.0E+00 ];

% Parameters for burnup calculation:

BURN_MATERIALS            (idx, 1)        = 55 ;
BURN_MODE                 (idx, 1)        = 2 ;
BURN_STEP                 (idx, 1)        = 4 ;
BURN_RANDOMIZE_DATA       (idx, [1:  3])  = [ 0 0 0 ];
BURNUP                    (idx, [1:  2])  = [  8.33580E-01  8.34031E-01 ];
BURN_DAYS                 (idx, [1:  2])  = [  9.00000E+01  3.00000E+01 ];
FIMA                      (idx, [1:  3])  = [  8.75327E-04  7.17618E+24  8.19112E+27 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  3.16668E-01 0.00391 ];
U235_FISS                 (idx, [1:   4]) = [  7.81892E+17 0.00093  8.48306E-01 0.00091 ];
U238_FISS                 (idx, [1:   4]) = [  2.40291E+15 0.04356  2.60724E-03 0.04356 ];
PU239_FISS                (idx, [1:   4]) = [  1.33430E+17 0.00506  1.44771E-01 0.00508 ];
PU240_FISS                (idx, [1:   4]) = [  8.21503E+12 0.70623  8.91291E-06 0.70623 ];
PU241_FISS                (idx, [1:   4]) = [  3.85271E+15 0.03390  4.18035E-03 0.03390 ];
U235_CAPT                 (idx, [1:   4]) = [  1.48294E+17 0.00568  1.39171E-01 0.00495 ];
U238_CAPT                 (idx, [1:   4]) = [  3.30438E+17 0.00415  3.10088E-01 0.00299 ];
PU239_CAPT                (idx, [1:   4]) = [  7.82333E+16 0.00783  7.33992E-02 0.00725 ];
PU240_CAPT                (idx, [1:   4]) = [  1.70486E+16 0.01589  1.59786E-02 0.01542 ];
PU241_CAPT                (idx, [1:   4]) = [  1.54273E+15 0.05306  1.44984E-03 0.05307 ];
XE135_CAPT                (idx, [1:   4]) = [  3.66484E+16 0.01116  3.44066E-02 0.01086 ];
SM149_CAPT                (idx, [1:   4]) = [  1.07967E+16 0.01975  1.01174E-02 0.01944 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS    (idx, [1:  2])  = [ 500370 5.00000E+05 ];
BALA_SRC_NEUTRON_NXN     (idx, [1:  2])  = [ 0 2.08248E+01 ];
BALA_SRC_NEUTRON_VR      (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT     (idx, [1:  2])  = [ 500370 5.00021E+05 ];

BALA_LOSS_NEUTRON_CAPT    (idx, [1:  2])  = [ 255687 2.55501E+05 ];
BALA_LOSS_NEUTRON_FISS    (idx, [1:  2])  = [ 221525 2.21379E+05 ];
BALA_LOSS_NEUTRON_LEAK    (idx, [1:  2])  = [ 23158 2.31404E+04 ];
BALA_LOSS_NEUTRON_CUT     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_ERR     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT     (idx, [1:  2])  = [ 500370 5.00021E+05 ];

BALA_NEUTRON_DIFF         (idx, [1:  2])  = [ 0 -1.16415E-10 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   6]) = [  3.00000E+07 0.0E+00  3.00000E+07 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_POWDENS               (idx, [1:   6]) = [  9.26200E-03 2.7E-09  9.26200E-03 2.7E-09  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   6]) = [  2.30584E+18 0.00011  2.30584E+18 0.00011  0.00000E+00 0.0E+00 ];
TOT_FISSRATE              (idx, [1:   6]) = [  9.21702E+17 2.2E-05  9.21702E+17 2.2E-05  0.00000E+00 0.0E+00 ];
TOT_CAPTRATE              (idx, [1:   6]) = [  1.06558E+18 0.00284  6.68272E+17 0.00331  3.97310E+17 0.00383 ];
TOT_ABSRATE               (idx, [1:   6]) = [  1.98728E+18 0.00152  1.58997E+18 0.00139  3.97310E+17 0.00383 ];
TOT_SRCRATE               (idx, [1:   6]) = [  2.08371E+18 0.00155  2.08371E+18 0.00155  0.00000E+00 0.0E+00 ];
TOT_FLUX                  (idx, [1:   6]) = [  1.91171E+21 0.00217  5.27929E+18 0.00164  1.90643E+21 0.00217 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  9.65114E+16 0.00718 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  2.08380E+18 0.00155 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  7.84615E+20 0.00219 ];
INI_FMASS                 (idx, 1)        =  3.23904E+03 ;
TOT_FMASS                 (idx, 1)        =  3.23624E+03 ;
INI_BURN_FMASS            (idx, 1)        =  3.23904E+03 ;
TOT_BURN_FMASS            (idx, 1)        =  3.23624E+03 ;

% Six-factor formula:

SIX_FF_ETA                (idx, [1:   2]) = [  1.71985E+00 0.00122 ];
SIX_FF_F                  (idx, [1:   2]) = [  7.71574E-01 0.00086 ];
SIX_FF_P                  (idx, [1:   2]) = [  8.47316E-01 0.00065 ];
SIX_FF_EPSILON            (idx, [1:   2]) = [  1.03304E+00 0.00042 ];
SIX_FF_LF                 (idx, [1:   2]) = [  9.99785E-01 2.2E-05 ];
SIX_FF_LT                 (idx, [1:   2]) = [  9.53924E-01 0.00032 ];
SIX_FF_KINF               (idx, [1:   2]) = [  1.16142E+00 0.00153 ];
SIX_FF_KEFF               (idx, [1:   2]) = [  1.10766E+00 0.00155 ];

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.50172E+00 0.00013 ];
FISSE                     (idx, [1:   2]) = [  2.03152E+02 2.2E-05 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.10740E+00 0.00159  6.88359E-02 0.00156  3.93020E-04 0.03077 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.10766E+00 0.00155 ];
COL_KEFF                  (idx, [1:   2]) = [  1.10766E+00 0.00155 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.10766E+00 0.00155 ];
ABS_KINF                  (idx, [1:   2]) = [  1.16142E+00 0.00153 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.89994E+01 0.00020 ];
IMP_ALF                   (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  1.12467E-07 0.00395 ];
IMP_EALF                  (idx, [1:   2]) = [  2.00000E+01 0.0E+00 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  8.60505E-03 0.04726 ];
IMP_AFGE                  (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% Forward-weighted delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 6 ;
FWD_ANA_BETA_ZERO         (idx, [1:  14]) = [  5.25022E-03 0.01993  2.15346E-04 0.10305  1.03717E-03 0.04276  9.30169E-04 0.04388  1.95355E-03 0.03121  8.17943E-04 0.04761  2.96049E-04 0.07867 ];
FWD_ANA_LAMBDA            (idx, [1:  14]) = [  4.32870E-01 0.02850  3.13282E-03 0.09033  2.45916E-02 0.02853  8.93155E-02 0.02949  2.82819E-01 0.01320  5.76787E-01 0.03454  9.77076E-01 0.06937 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  14]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  14]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Adjoint weighted time constants using Nauchi's method:

IFP_CHAIN_LENGTH          (idx, 1)        = 15 ;
ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  1.21705E-03 0.00343  1.21701E-03 0.00345  1.04798E-03 0.04949 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  1.34649E-03 0.00307  1.34645E-03 0.00309  1.16103E-03 0.04983 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  14]) = [  5.61596E-03 0.03114  2.47538E-04 0.14709  1.11867E-03 0.06281  9.17225E-04 0.07229  2.08191E-03 0.04833  8.93701E-04 0.07523  3.56922E-04 0.11146 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  14]) = [  4.59091E-01 0.04820  1.33332E-02 0.00015  3.25387E-02 0.00119  1.19994E-01 0.00139  3.02649E-01 0.00054  8.51221E-01 0.00063  2.85935E+00 0.00172 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  1.17606E-03 0.00784  1.17616E-03 0.00786  4.95657E-04 0.09553 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  1.30106E-03 0.00765  1.30114E-03 0.00767  5.48056E-04 0.09586 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  14]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  14]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  14]) = [  6.21253E-03 0.08077  3.10956E-04 0.44637  9.21427E-04 0.18818  1.26020E-03 0.19629  2.51617E-03 0.13166  9.05635E-04 0.18453  2.98137E-04 0.37244 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  14]) = [  4.04206E-01 0.10404  1.33295E-02 0.00049  3.24369E-02 0.00327  1.20285E-01 0.00234  3.01999E-01 0.00102  8.52860E-01 0.00226  2.84179E+00 0.00394 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  1.19984E-03 0.00237 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  1.32720E-03 0.00155 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  5.70891E-03 0.01784 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -4.76822E+00 0.01810 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  1.67125E-06 0.00051 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  3.01278E-05 0.00048  3.01271E-05 0.00047  3.01835E-05 0.00690 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  1.76138E-03 0.00178  1.76142E-03 0.00178  1.73651E-03 0.02760 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  8.55405E-01 0.00062  8.55007E-01 0.00065  1.16023E+00 0.04797 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.23096E+01 0.04921 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  3.76506E+02 0.00142  3.49420E+02 0.00180 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.32' ;
COMPILE_DATE              (idx, [1: 20])  = 'Oct 21 2021 21:31:23' ;
DEBUG                     (idx, 1)        = 0 ;
TITLE                     (idx, [1:  8])  = 'Untitled' ;
CONFIDENTIAL_DATA         (idx, 1)        = 0 ;
INPUT_FILE_NAME           (idx, [1: 14])  = 'pbr_run_in.inp' ;
WORKING_DIRECTORY         (idx, [1: 60])  = '/home/stewryan/projects/NEAMS/pebshufpy/examples/auto_run_in' ;
HOSTNAME                  (idx, [1:  9])  = 'lemhi0447' ;
CPU_TYPE                  (idx, [1: 40])  = 'Intel(R) Xeon(R) Gold 6148 CPU @ 2.40GHz' ;
CPU_MHZ                   (idx, 1)        = 33581830.0 ;
START_DATE                (idx, [1: 24])  = 'Thu Mar  3 11:06:38 2022' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Mar  3 11:18:48 2022' ;

% Run parameters:

POP                       (idx, 1)        = 5000 ;
CYCLES                    (idx, 1)        = 100 ;
SKIP                      (idx, 1)        = 20 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1646330798446 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 0 ;
B1_CALCULATION            (idx, [1:  3])  = [ 0 0 0 ];
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;

CRIT_SPEC_MODE            (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 2 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 0 ;
DOUBLE_INDEXING           (idx, 1)        = 0 ;
MG_MAJORANT_MODE          (idx, 1)        = 1 ;
SPECTRUM_COLLAPSE         (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 4 ;
OMP_THREADS               (idx, 1)        = 40 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  40]) = [  1.03001E+00  9.63705E-01  1.02974E+00  1.04918E+00  1.00764E+00  1.02655E+00  1.01989E+00  1.02788E+00  9.63705E-01  1.01989E+00  1.01430E+00  9.90334E-01  9.98056E-01  1.00578E+00  1.01217E+00  1.02362E+00  9.59710E-01  9.93529E-01  9.56249E-01  9.81014E-01  9.90067E-01  1.02841E+00  9.95926E-01  9.88470E-01  1.00658E+00  1.01936E+00  1.03773E+00  9.58113E-01  9.85540E-01  9.89535E-01  1.03454E+00  9.88203E-01  1.01270E+00  1.02229E+00  9.75421E-01  9.82345E-01  9.82611E-01  9.79149E-01  9.57314E-01  9.92730E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;
OMP_SHARED_QUEUE_LIM      (idx, 1)        = 0 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 64])  = '/hpc-common/data/serpent/xsdata/endfb71_edep/endfb71_edep.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 46])  = '/hpc-common/data/serpent/xsdata/sss_endfb7.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 46])  = '/hpc-common/data/serpent/xsdata/sss_endfb7.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 46])  = '/hpc-common/data/serpent/xsdata/sss_endfb7.nfy' ;
BRA_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:   4]) = [  5.00000E-02 0.0E+00  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  9.49227E-01 7.8E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  5.07729E-02 0.00145  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  2.97499E-01 0.00023  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  9.97944E-01 5.1E-06  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  7.40123E-01 0.00041  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  3.34665E+01 0.00152  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  3.78388E+02 0.00158  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  3.78342E+02 0.00158  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.31702E+02 0.00038  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  3.18537E+03 0.00157  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 100 ;
SIMULATED_HISTORIES       (idx, 1)        = 125115 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  1.25104E+03 0.00229 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  1.25104E+03 0.00229 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.30326E+02 ;
RUNNING_TIME              (idx, 1)        =  1.21669E+01 ;
INIT_TIME                 (idx, [1:  2])  = [  1.34072E+00  1.34072E+00 ];
PROCESS_TIME              (idx, [1:  2])  = [  3.43167E-02  2.11667E-03 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.07568E+01  9.05333E-01  8.63400E-01 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  2.03333E-02  2.08333E-03 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  9.53334E-03  1.23334E-03 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  1.03142E+00  6.33331E-04 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.21646E+01  1.21646E+01 ];
CPU_USAGE                 (idx, 1)        = 18.93054 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  3.80513E+01 0.00665 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  4.02061E-01 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 192031.22 ;
ALLOC_MEMSIZE             (idx, 1)        = 28280.46;
MEMSIZE                   (idx, 1)        = 27989.25;
XS_MEMSIZE                (idx, 1)        = 23187.29;
MAT_MEMSIZE               (idx, 1)        = 138.58;
RES_MEMSIZE               (idx, 1)        = 16.29;
IFC_MEMSIZE               (idx, 1)        = 0.00;
MISC_MEMSIZE              (idx, 1)        = 4647.09;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 291.21;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 1518 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  5.00000E-05 ;
NEUTRON_ERG_NE            (idx, 1)        = 413898 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Unresolved resonance probability table sampling:

URES_DILU_CUT             (idx, 1)        =  1.00000E-09 ;
URES_EMIN                 (idx, 1)        =  1.00000E+37 ;
URES_EMAX                 (idx, 1)        = -1.00000E+37 ;
URES_AVAIL                (idx, 1)        = 244 ;
URES_USED                 (idx, 1)        = 0 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 1889 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 728 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 1161 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 18115 ;
TOT_TRANSMU_REA           (idx, 1)        = 3087 ;

% Neutron physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 0 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_PREPROCESSOR      (idx, 1)        = 1 ;
TMS_MODE                  (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Energy deposition:

EDEP_MODE                 (idx, 1)        = 0 ;
EDEP_DELAYED              (idx, 1)        = 1 ;
EDEP_KEFF_CORR            (idx, 1)        = 1 ;
EDEP_LOCAL_EGD            (idx, 1)        = 0 ;
EDEP_COMP                 (idx, [1:  9])  = [ 0 0 0 0 0 0 0 0 0 ];
EDEP_CAPT_E               (idx, 1)        =  0.00000E+00 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  5.86803E+18 ;
TOT_DECAY_HEAT            (idx, 1)        =  1.85180E+06 ;
TOT_SF_RATE               (idx, 1)        =  3.83148E+06 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  6.72494E+17 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  4.64345E+04 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  5.19554E+18 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  1.80536E+06 ;
INHALATION_TOXICITY       (idx, 1)        =  9.64581E+09 ;
INGESTION_TOXICITY        (idx, 1)        =  2.98050E+09 ;
ACTINIDE_INH_TOX          (idx, 1)        =  3.92366E+09 ;
ACTINIDE_ING_TOX          (idx, 1)        =  2.82772E+08 ;
FISSION_PRODUCT_INH_TOX   (idx, 1)        =  5.72215E+09 ;
FISSION_PRODUCT_ING_TOX   (idx, 1)        =  2.69772E+09 ;
SR90_ACTIVITY             (idx, 1)        =  2.63546E+15 ;
TE132_ACTIVITY            (idx, 1)        =  4.06290E+16 ;
I131_ACTIVITY             (idx, 1)        =  2.78890E+16 ;
I132_ACTIVITY             (idx, 1)        =  4.11461E+16 ;
CS134_ACTIVITY            (idx, 1)        =  3.23658E+14 ;
CS137_ACTIVITY            (idx, 1)        =  2.85810E+15 ;
PHOTON_DECAY_SOURCE       (idx, 1)        =  4.90189E+18 ;
NEUTRON_DECAY_SOURCE      (idx, 1)        =  9.45999E+15 ;
ALPHA_DECAY_SOURCE        (idx, 1)        =  4.32017E+13 ;
ELECTRON_DECAY_SOURCE     (idx, 1)        =  7.04834E+18 ;

% Normalization coefficient:

NORM_COEF                 (idx, [1:   4]) = [  1.68319E+15 0.00156  0.00000E+00 0.0E+00 ];

% Parameters for burnup calculation:

BURN_MATERIALS            (idx, 1)        = 55 ;
BURN_MODE                 (idx, 1)        = 2 ;
BURN_STEP                 (idx, 1)        = 5 ;
BURN_RANDOMIZE_DATA       (idx, [1:  3])  = [ 0 0 0 ];
BURNUP                    (idx, [1:  2])  = [  1.11144E+00  1.11181E+00 ];
BURN_DAYS                 (idx, [1:  2])  = [  1.20000E+02  3.00000E+01 ];
FIMA                      (idx, [1:  3])  = [  1.16664E-03  9.56442E+24  8.18873E+27 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  3.17907E-01 0.00373 ];
U235_FISS                 (idx, [1:   4]) = [  7.72862E+17 0.00096  8.38746E-01 0.00094 ];
U238_FISS                 (idx, [1:   4]) = [  2.34507E+15 0.04201  2.54508E-03 0.04201 ];
PU239_FISS                (idx, [1:   4]) = [  1.41573E+17 0.00495  1.53649E-01 0.00498 ];
PU240_FISS                (idx, [1:   4]) = [  1.23733E+13 0.57679  1.34322E-05 0.57678 ];
PU241_FISS                (idx, [1:   4]) = [  4.54813E+15 0.03063  4.93630E-03 0.03064 ];
U235_CAPT                 (idx, [1:   4]) = [  1.48403E+17 0.00587  1.36884E-01 0.00533 ];
U238_CAPT                 (idx, [1:   4]) = [  3.30858E+17 0.00414  3.05002E-01 0.00292 ];
PU239_CAPT                (idx, [1:   4]) = [  8.22380E+16 0.00723  7.57990E-02 0.00654 ];
PU240_CAPT                (idx, [1:   4]) = [  1.92575E+16 0.01470  1.77743E-02 0.01464 ];
PU241_CAPT                (idx, [1:   4]) = [  1.72763E+15 0.05168  1.59399E-03 0.05187 ];
XE135_CAPT                (idx, [1:   4]) = [  3.72476E+16 0.01057  3.43258E-02 0.01006 ];
SM149_CAPT                (idx, [1:   4]) = [  1.07858E+16 0.02077  9.93978E-03 0.02051 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS    (idx, [1:  2])  = [ 500414 5.00000E+05 ];
BALA_SRC_NEUTRON_NXN     (idx, [1:  2])  = [ 0 2.42732E+01 ];
BALA_SRC_NEUTRON_VR      (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT     (idx, [1:  2])  = [ 500414 5.00024E+05 ];

BALA_LOSS_NEUTRON_CAPT    (idx, [1:  2])  = [ 257778 2.57571E+05 ];
BALA_LOSS_NEUTRON_FISS    (idx, [1:  2])  = [ 219350 2.19185E+05 ];
BALA_LOSS_NEUTRON_LEAK    (idx, [1:  2])  = [ 23286 2.32674E+04 ];
BALA_LOSS_NEUTRON_CUT     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_ERR     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT     (idx, [1:  2])  = [ 500414 5.00024E+05 ];

BALA_NEUTRON_DIFF         (idx, [1:  2])  = [ 0 -6.98492E-10 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   6]) = [  3.00000E+07 0.0E+00  3.00000E+07 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_POWDENS               (idx, [1:   6]) = [  9.26200E-03 2.6E-09  9.26200E-03 2.6E-09  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   6]) = [  2.30902E+18 0.00011  2.30902E+18 0.00011  0.00000E+00 0.0E+00 ];
TOT_FISSRATE              (idx, [1:   6]) = [  9.21441E+17 2.3E-05  9.21441E+17 2.3E-05  0.00000E+00 0.0E+00 ];
TOT_CAPTRATE              (idx, [1:   6]) = [  1.08468E+18 0.00286  6.78715E+17 0.00329  4.05967E+17 0.00391 ];
TOT_ABSRATE               (idx, [1:   6]) = [  2.00612E+18 0.00155  1.60016E+18 0.00139  4.05967E+17 0.00391 ];
TOT_SRCRATE               (idx, [1:   6]) = [  2.10399E+18 0.00156  2.10399E+18 0.00156  0.00000E+00 0.0E+00 ];
TOT_FLUX                  (idx, [1:   6]) = [  1.93584E+21 0.00225  5.31401E+18 0.00172  1.93052E+21 0.00225 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  9.79666E+16 0.00714 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  2.10409E+18 0.00156 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  7.94475E+20 0.00228 ];
INI_FMASS                 (idx, 1)        =  3.23904E+03 ;
TOT_FMASS                 (idx, 1)        =  3.23531E+03 ;
INI_BURN_FMASS            (idx, 1)        =  3.23904E+03 ;
TOT_BURN_FMASS            (idx, 1)        =  3.23531E+03 ;

% Six-factor formula:

SIX_FF_ETA                (idx, [1:   2]) = [  1.71264E+00 0.00120 ];
SIX_FF_F                  (idx, [1:   2]) = [  7.68993E-01 0.00090 ];
SIX_FF_P                  (idx, [1:   2]) = [  8.47846E-01 0.00062 ];
SIX_FF_EPSILON            (idx, [1:   2]) = [  1.03189E+00 0.00038 ];
SIX_FF_LF                 (idx, [1:   2]) = [  9.99792E-01 1.9E-05 ];
SIX_FF_LT                 (idx, [1:   2]) = [  9.53663E-01 0.00033 ];
SIX_FF_KINF               (idx, [1:   2]) = [  1.15214E+00 0.00154 ];
SIX_FF_KEFF               (idx, [1:   2]) = [  1.09851E+00 0.00155 ];

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.50589E+00 0.00014 ];
FISSE                     (idx, [1:   2]) = [  2.03209E+02 2.3E-05 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.09860E+00 0.00160  6.82466E-02 0.00155  4.10089E-04 0.02678 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.09851E+00 0.00155 ];
COL_KEFF                  (idx, [1:   2]) = [  1.09851E+00 0.00155 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.09851E+00 0.00155 ];
ABS_KINF                  (idx, [1:   2]) = [  1.15214E+00 0.00154 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.89991E+01 0.00019 ];
IMP_ALF                   (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  1.12449E-07 0.00364 ];
IMP_EALF                  (idx, [1:   2]) = [  2.00000E+01 0.0E+00 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  8.36643E-03 0.04506 ];
IMP_AFGE                  (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% Forward-weighted delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 6 ;
FWD_ANA_BETA_ZERO         (idx, [1:  14]) = [  5.28479E-03 0.01909  1.44125E-04 0.11075  8.96505E-04 0.04403  9.51514E-04 0.04417  2.01950E-03 0.03031  8.77071E-04 0.04606  3.96069E-04 0.06889 ];
FWD_ANA_LAMBDA            (idx, [1:  14]) = [  4.97357E-01 0.02924  2.43252E-03 0.10596  2.33769E-02 0.03142  8.63050E-02 0.03142  2.83363E-01 0.01293  6.03943E-01 0.03200  1.20406E+00 0.05854 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  14]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  14]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Adjoint weighted time constants using Nauchi's method:

IFP_CHAIN_LENGTH          (idx, 1)        = 15 ;
ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  1.23040E-03 0.00351  1.23045E-03 0.00352  1.12420E-03 0.04579 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  1.35028E-03 0.00308  1.35033E-03 0.00308  1.23568E-03 0.04583 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  14]) = [  5.96556E-03 0.02691  1.75868E-04 0.15528  1.08429E-03 0.06131  1.10591E-03 0.06358  2.22465E-03 0.04402  9.49252E-04 0.07297  4.25589E-04 0.10466 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  14]) = [  4.66254E-01 0.04531  1.33260E-02 0.00029  3.25471E-02 0.00118  1.20228E-01 0.00113  3.02233E-01 0.00048  8.50198E-01 0.00020  2.85238E+00 0.00150 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  1.20483E-03 0.00840  1.20547E-03 0.00843  4.99597E-04 0.10348 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  1.32223E-03 0.00819  1.32294E-03 0.00822  5.46321E-04 0.10285 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  14]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  14]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  14]) = [  5.75331E-03 0.08301  1.84145E-04 0.47365  1.04772E-03 0.19022  1.03407E-03 0.20393  2.11329E-03 0.15124  8.28526E-04 0.20223  5.45566E-04 0.33650 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  14]) = [  5.09508E-01 0.10221  1.33360E-02 0.0E+00  3.26350E-02 0.00197  1.20357E-01 0.00245  3.01832E-01 0.00118  8.50090E-01 0.00040  2.85300E+00 0.0E+00 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  1.21781E-03 0.00230 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  1.33652E-03 0.00165 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  6.01781E-03 0.01608 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -4.95099E+00 0.01626 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  1.67242E-06 0.00057 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  3.01051E-05 0.00046  3.01054E-05 0.00046  2.97843E-05 0.00729 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  1.76686E-03 0.00202  1.76723E-03 0.00203  1.70376E-03 0.02926 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  8.56027E-01 0.00059  8.55687E-01 0.00061  1.08922E+00 0.03263 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.01004E+01 0.04567 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  3.77564E+02 0.00158  3.51054E+02 0.00193 ];

