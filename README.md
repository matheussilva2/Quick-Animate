# Quick Animate
Make your animation quickly by using your favorite drawing software.

<h1>Requirements</h1>
Python3++
opencv-python 4.2.0.32

<h1>How to use</h1>
<h2>1 - Installing</h2>
<ol>
<li>Install dependences by executing python pip install -r requirements.txt
or just install opencv-python 4.2.0.32</li>
</ol>

<h2>2 - Watching image file</h2>
<ol>
<li> Open main.py</li>
<li> Select <b>1 - Observe a File</b></li>
<li> Type the filename <b>without filetype</b></li>
<li> Type filetype <b>without dot (.)</b>. For example jpg</li>
</ol>
Now your file will begin observed. Every time when you save your file, a copy will be created at images/output

<h2>3 - Rendering your animation</h2>
<ol>
<li>Open main.py</li>
<li>Select <b>2 - Render an animation</b></li>
<li>Animator will ask you if you really want to render your animation. Type Y or N.</li>
<li>Type what is the filetype of your images.</li>
<li>Type the filename of your animation</li>
<li>Type the framerate of your animation</li>
<li>Wait while your animation is created.</li>
</ol>
When your animation is done, the animation folder will be opened. You can find it by accessing ./video/output/

<h2>Notes</h2>
Your images should have the same size (The size (width, height) of your animation will be the same of last image loaded).
Your images should have the same type.
You can change the output folders by editing config.py.
