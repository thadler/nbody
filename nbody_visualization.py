import os
import numpy as np
import matplotlib.pyplot as plt

# very dirty and memory intensive - but idfc
def save_video(positions, path="/home/thomas/Desktop/nbody/position_vids/"):
	size = max(np.max(np.array(positions)), -np.min(np.array(positions)))+1
	for i in xrange(len(positions)):
		if i%50==0: print i
		fig, ax = plt.subplots(nrows=1, ncols=1); ax.set_xlim(xmin=-size, xmax=size); ax.set_ylim(ymin=-size, ymax=size)
		ax.scatter(positions[i][:,0], positions[i][:,1])
		fig.savefig(path+'img'+str(i))
		plt.close(fig)
	print "making video..."
	os.system('avconv -i ' +path+'"img%d.png" -r 50 -c:v libx264 -crf 20  -pix_fmt yuv420p '+path+'img.mov')
	for i in xrange(len(positions)): os.system("rm "+path+"img"+str(i)+".png")
