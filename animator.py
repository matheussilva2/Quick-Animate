import cv2
import glob
import subprocess
import os

class Animator:
	def __init__(self, filename, fps, input_path, output_path, img_filetype="png"):
		self._filename = filename
		self._images = []
		self._input_path = input_path
		self._filename = filename
		self._filetype = img_filetype
		self._size = None
		self._fps = int(fps)

	def render(self):
		if(self.load_images()):
			if(self.generate_video()):
				print("Done! Opening your animation folder.")
				subprocess.call("explorer "+os.getcwd()+"\\video\\output", shell=True)
		else:
			print("I tried to load images, but something gone wrong :(")

	def add_img_to_array(self, img):
		self._images.append(img)

	def get_image(self, position):
		if(position < len(self._images)):
			return self._images[position]
		else:
			return False

	def clear_img_array(self):
		self._images = []
		return true

	def load_images(self):
		path = self._input_path+"\\*."+self._filetype
		print("Loading from " + path)
		images = glob.glob(path)
		for image in images:
			img = cv2.imread(image)
			height, width, layers = img.shape
			self._size = (width, height)
			self.add_img_to_array(img)
		return True

	def generate_video(self):
		try:
			video = cv2.VideoWriter("video/output/"+self._filename+".avi", cv2.VideoWriter_fourcc(*'DIVX'), self._fps, self._size)
			for i in range(len(self._images)):
				video.write(self.get_image(i))
			video.release()
			return True
		except Exception as e:
			print(e)
			return False