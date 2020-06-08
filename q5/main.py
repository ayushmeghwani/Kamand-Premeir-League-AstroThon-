# all imports below
import requests
import datetime
from bs4 import BeautifulSoup
import os
import matplotlib
import matplotlib.pyplot as plt


from astropy.io import fits
from astropy.utils.data import get_pkg_data_filename

"""
Any extra lines of code (if required)
as helper for this function.
"""

class ScraperXRT:
	'''
	Description
	-----------
	A class to scrap XRT files from the telescope archive.
	'''

	def __init__(self, typeof_file, startime, endtime):
		'''
		Parameters
		----------
		typeof_file: A `string`
		startime: A `~datetime.datetime` instance
		endtime: A `~datetime.datetime` instance
		'''
		self.typeof_file = typeof_file
		self.startime = startime
		self.endtime = endtime

	def query(self):
		'''
		Returns
		-------
		A `list` of strings of URLs.
		'''

		URL = 'http://solar.physics.montana.edu/HINODE/XRT/QL/syn_comp_fits/'
		page = requests.get(URL)

		soup = BeautifulSoup(page.content, 'html.parser')

		table = soup.find('table')
		i=0
		urls = [];

		a=self.typeof_file
		b=self.startime
		c=self.endtime



		for link in table.find_all('a'):
		    	#name = link.find('a')
			if link.get_text().startswith("XRT"):
				#print link
				#print link.get_text()
				name_mod = link.get_text()[4:-7].split("_")
				#print name_mod
				file_time = datetime.datetime.strptime(name_mod[-2]+name_mod[-1],'%Y%m%d%H%M%S')
				#print file_time
				if len(name_mod)==4:
			    		file_name = name_mod[0]+"_"+name_mod[1]
				else:
					file_name = name_mod[0]
				#print file_name
				if file_time >= b and file_time <= c and a==file_name:
			    		urls.append(link['href'])
		return urls

	def get(self):
		'''
		Returns
		-------
		A `list` of strings for files.
		'''
		urls = query()
		downloads=[]
		for url in urls:
			name = url.split('/')[-1]
			#print url
			r = requests.get(url, allow_redirects=True)
			open(name, 'wb').write(r.content)
			location=os.getcwd() + '/' + name
			downloads.append(location)

		return downloads

	def view(self, filepath):
		'''
		Parameters
		----------
		filepath: A `string` representing absolute path of file in system.

		Returns
		-------
		An instance of `matplotlib.image.AxesImage`, returned using `plt.imshow(data)`.
		'''
		image_file = get_pkg_data_filename(filepath)
		fits.info(image_file)
		image_data = fits.getdata(image_file, ext=0)
		#print(image_data.shape)
		plt.figure()
		plt.imshow(image_data, cmap='gray')
		plt.colorbar()

		return NotImplementedError
