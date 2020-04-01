import os
from shutil import copyfile
import time
import config

class Observer:
	def __init__(self, filename, filetype):
		self._filename = filename
		self._filetype = "."+filetype
		self._last_modified = None

	def observe(self):
		print(f"Observing {self._filename + self._filetype}")
		try:
			self._last_modified = os.stat(self._filename+self._filetype).st_mtime
			while True:	
				new_modified = os.stat(self._filename+self._filetype).st_mtime
				if(new_modified != self._last_modified):
					self._last_modified = new_modified
					print("The file was modified")
					#Copying files
					new_filename = config.image_output_path+"/"+self._filename+"_"+str(time.time())+self._filetype
					copyfile(self._filename+self._filetype, new_filename)
				time.sleep(0.1)
		except Exception as e:
			print("Something gone wrong :(")
			print(e)
			print("I'll keep observing")
			self.observe()