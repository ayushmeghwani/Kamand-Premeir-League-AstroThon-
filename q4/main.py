# all imports below
from datetime import datetime
from astropy.coordinates import EarthLocation
#from astropy.time import Time
from astropy import units as u
from astropy.coordinates import AltAz
from astropy.coordinates import SkyCoord
"""
Any extra lines of code (if required)
as helper for this function.
"""

startobs = datetime(2000, 1, 1, 0, 0, 0) #replace it by the time when Saturn will be just visible
endobs = datetime(2020, 1, 1) #replace it by the time when Saturn is no longer visible from SAC terrace

def findSaturn(obstime):
	'''
	Parameters
	----------
	obstime : A `~datetime.datetime` instance.
	
	Returns
	-------
	A `tuple` of two floats.
	'''
	sky=SkyCoord(227.67229951*u.deg, -15.67282015*u.deg, frame='icrs')
	gravity = EarthLocation(lat=31.781016*u.deg, lon=76.994292*u.deg, height=1000*u.m)
	coord=sky.transform_to(AltAz(obstime=obstime,location=gravity))
	return (coord.alt,coord.az)
#print(findSaturn(datetime(2000, 1, 1, 0, 0, 0)))
