from animator import Animator
import config

def start():
	confirm = str(input("Do you want to render your animation? (Y/N)\n> ")).upper()
	if(confirm == "Y"):
		img_filetype = str(input("The filetype of my images is: "))
		filename = str(input("The filename will be: "))
		fps = int(input("Frame Rate (FPS): "))
		print("OK! Wait while i'm creating your animation.")
		animator = Animator(filename, fps, config.image_output_path, config.video_output_path, img_filetype)
		animator.render()
	else:
		pass

start()