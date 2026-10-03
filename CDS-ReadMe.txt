J/A+A/650/A201     10 parsec sample in the Gaia era first update  (Reyle+, 2021)
================================================================================
The 10 parsec sample in the Gaia era.
    Reyle C., Jardine K., Fouque P., Caballero J.A., Smart R.L., Sozzetti A.
    <Astron. Astrophys. 650, A201 (2021)>
    =2021A&A...650A.201R        (SIMBAD/NED BibCode)
================================================================================
ADC_Keywords: Stars, nearby ; Parallaxes, trigonometric ; Proper motions ;
              Photometry, infrared ; Optical ; Exoplanets
Keywords: stars: nearby - stars: parallaxes - stars: late-type -
          stars: planetary systems - Galaxy: solar neighbourhood -
          Galaxy: stellar content - catalogues

Abstract:
    The nearest stars provide a fundamental constraint for our
    understanding of stellar physics and the Galaxy. The nearby sample
    serves as an anchor where all objects can be seen and understood with
    precise data. This work is triggered by the most recent data release
    of the astrometric space mission Gaia and uses its unprecedented high
    precision parallax measurements to review the census of objects within
    10pc.

    The first aim of this work was to compile all stars and brown dwarfs
    within 10pc observable by Gaia and compare it with the Gaia Catalogue
    of Nearby Stars as a quality assurance test. We complement the list to
    get a full 10 pc census, including bright stars, brown dwarfs, and
    exoplanets.

    We started our compilation from a query on all objects with a parallax
    larger than 100 mas using the Set of Identifications, Measurements,
    and Bibliography for Astronomical Data database (SIMBAD). We completed
    the census by adding companions, brown dwarfs with recent parallax
    measurements not in SIMBAD yet, and vetted exoplanets. The compilation
    combines astrometry and photometry from the recent Gaia Early Data
    Release 3 with literature magnitudes, spectral types, and
    line-of-sight velocities.

    We give a description of the astrophysical content of the 10pc sample.
    We find a multiplicity frequency of around 27%. Among the stars and
    brown dwarfs, we estimate that around 61% are M stars and more than
    half of the M stars are within the range from M3.0 V to M5.0 V. We
    give an overview of the brown dwarfs and exoplanets that should be
    detected in the next Gaia data releases along with future
    developments.

    We provide a catalogue of 541 stars, brown dwarfs, and exoplanets in
    339 systems, within 10pc from the Sun. This list is as volume-complete
    as possible from current knowledge and it provides benchmark stars
    that can be used, for instance, to define calibration samples and to
    test the quality of the forthcoming Gaia releases. It also has a
    strong outreach potential.

Description:
    We provide a catalogue of 541 stars, brown dwarfs, and exoplanets in
    339 systems, within 10 pc from the Sun. Astrometry, photometry,
    spectral types, and line-of-sight velocities are given when available.
    This list is as volume-complete as possible from current knowledge and
    provides benchmark stars that can be used, for instance, to define
    calibration samples and to test the quality of the forthcoming Gaia
    releases. It also has a strong outreach potential.

    Table A1 was updated on 06-Feb-2023.

    This work is an update of the 10pc sample that used the unprecedented
    high precision parallax measurements from the early third data release
    of the astrometric space mission Gaia. We review this census, all
    updates being related to close binaries, brown dwarfs and exoplanets.
    We provide a new catalogue of 541 stars, brown dwarfs, and exoplanets
    in 336 systems within 10 pc from the Sun. This list is as
    volume-complete as possible from current knowledge and it provides a
    list of benchmark stars. We also explore the new products made
    available in the most recent third Gaia data release.

    The catalogue contains 541 stars, brown dwarfs, and exoplanets in 354
    systems, closer than 10pc from the Sun.

File Summary:
--------------------------------------------------------------------------------
 FileName     Lrecl  Records   Explanations
--------------------------------------------------------------------------------
ReadMe           80        .   This file
tablea1.dat     945      562   The 10 pc catalogue (update version, 25-Aug-2023)
--------------------------------------------------------------------------------

See also:
   https://gruze.org/10pc : This catalog
   https://gucds.inaf.it  : GUCDS Home Page
   https://zenodo.org/record/7576096 : Update description

Byte-by-byte Description of file: tablea1.dat
--------------------------------------------------------------------------------
   Bytes Format Units    Label     Explanations
--------------------------------------------------------------------------------
   1-  4  I4    ---      Seq       Running number for object
   6-  9  I4    ---      Sys       Running number for system
  11- 39  A29   ---      Name      Name of the system
  41- 46  A6    ---      ObjType   Type of the object (1)
  48- 76  A29   ---      ObjName   Name of the object
  79- 91  F13.9 deg      RAdeg     Right ascension in ICRS at Epoch
  94-106  F13.9 deg      DEdeg     Declination in ICRS at Epoch
 108-113  F6.1  yr       Epoch     Epoch for position
 115-122  F8.4  mas      plx       Parallax
 124-131  F8.4  mas    e_plx       ?=- Parallax uncertainty
 133-163  A31   ---    r_plx       Reference for the parallax
 165-180  F16.9 mas/yr   pmRA      ?=- Proper motion in right ascension,
                                     pmRA*cosDE
 182-197  F16.9 mas/yr e_pmRA      ?=- Proper motion uncertainty in
                                    right ascension
 199-214  F16.9 mas/yr   pmDE      ?=- Proper motion in declination
 216-231  F16.9 mas/yr e_pmDE      ?=- Proper motion uncertainty in declination
 233-262  A30   ---    r_pmDE      Reference for proper motion
 264-271  F8.3  km/s     RV        ?=- Line-of-sight velocity
 273-280  F8.4  km/s   e_RV        ?=- Line-of-sight velocity uncertainty
 282-300  A19   ---    r_RV        Reference for line-of-sight velocity
 302-309  A8    ---      SpType    Spectral type
 311-335  A25   ---    r_SpType    Reference for spectral type
 337-348  A12   ---      SpMethod  Method used to derive the spectral type
 350-351  I2    ---      GCode     [2/20]? Code for Gmag origin (2)
 353-361  F9.6  mag      Gmag      ?=- Gaia G band magnitude measured, given
                                    only if GCode is 2 or 3
 363-368  F6.2  mag      Gest      ?=- Gaia G band magnitude estimated, given
                                    only if GCode is 10 or 20
 370-378  F9.6  mag      GBPmag    ?=- Gaia BP band magnitude measured, given
                                    only if GCode is 2 or 3
 380-388  F9.6  mag      GRPmag    ?=- Gaia RP band magnitude measured, given
                                    only if GCode is 2 or 3
 390-396  F7.3  mag      Umag      ?=- U band magnitude
 398-404  F7.3  mag      Bmag      ?=- B band magnitude
 406-412  F7.3  mag      Vmag      ?=- V band magnitude
 414-420  F7.3  mag      Rmag      ?=- R band magnitude
 422-428  F7.3  mag      Imag      ?=- I band magnitude
 430-436  F7.3  mag      Jmag      ?=- J band magnitude
 438-444  F7.3  mag      Hmag      ?=- H band magnitude
 446-452  F7.3  mag      Ksmag     ?=- Ks band magnitude
 454-474  A21   ---    r_Sys       Reference for multiplicity or exoplanets
     476  I1    ---      Nexopl    ? Number of confirmed exoplanets
 478-496  I19   ---      GaiaDR2   ?=- Gaia DR2 identifier
 498-516  I19   ---      GaiaEDR3  ?=- Gaia EDR3 identifier
 518-543  A26   ---      SIMBAD    Name resolved by SIMBAD
 545-561  A17   ---      Common    Common name
 563-572  A10   ---      GJ        Gliese & Jahreiss catalogue identifier,
 574-585  A12   ---      HD        Henry Draper catalogue identifier
 587-596  A10   ---      HIP       Hipparcos catalogue identifier
 598-945  A348  ---      Com       Additional comments on exoplanets,
                                    multiplicity, etc


--------------------------------------------------------------------------------
Note (1): Type of the object as follows:
    *      = Star
    LM     = low mass star
    BD     = brown dwarf
    WD     = white dwarf
    Planet = Planet
Note (2): Code for Gmag origin as follows:
    2 = if G from Gaia DR2
    3 = if G from Gaia EDR3
   10 = if G derived from spectral type
   20 = for spectral type >T6 (arbitrarily set to absolute Gmag=25)
--------------------------------------------------------------------------------

Acknowledgements:
    Celine Reyle, celine.reyle(at)obs-besancon.fr

History:
    30-Jun-2021: on-line version
    06-Feb-2023: update
    25-Aug-2023: update

================================================================================
(End)   Celine Reyle [OSU THETA, UBFC], Patricia Vannier [CDS]       30-Apr-2021
