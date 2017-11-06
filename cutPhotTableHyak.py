
# from __future__ import printfunction
from astropy.io import ascii

# read in the massive phot table
#t = ascii.read('/Users/mwilde/Data/PHAT/table5.dat')
# t = ascii.read('/astro/users/mwilde/Data/PHAT/phat_test.dat')
# t = ascii.read('phat_test.dat')
t = ascii.read('table5.dat')
# t = ascii.read('/Users/mwilde/Data/PHAT/phat_test.dat')
print(len(t)) # see how big it is

# cut to find agb
lum_cut = t["F160Wmag"] < 18.2
tmpTable = t[lum_cut]

del t, lum_cut

color_cut =  tmpTable["F110Wmag"] - tmpTable["F160Wmag"] > 0.9
agbTable = tmpTable[color_cut]

del tmpTable, color_cut

print(len(agbTable))
# agbTable.write('agbTable.hd5', format='ascii.ipac', overwrite=False)
# agbTable.write('/Users/mwilde/Data/PHAT/agbTable_test.hdf5', path='data')
# agbTable.write('agbTable_test.hdf5', path='data', overwrite=True)
agbTable.write('agbTable_Full.hdf5', path='data', overwrite=True)

# print(t[:10])