import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt
from nbody_visualization import save_video
import systems_importer

class NBody:
	def __init__(self, timestep=0.1, masses=None, positions=None, velocities=None):
		assert len(masses)==len(positions)==len(velocities), "inputs are not of same length"
		self.n  = len(masses)
		self.ts = timestep
		self.m  = masses     if masses is not None     else np.zeros((self.n, ))
		self.s  = positions  if positions is not None  else np.zeros((self.n,3)) # s[1].shape = (3,)
		self.v  = velocities if velocities is not None else np.zeros((self.n,3))
		
	def one_timestep(self):
		s, v, m, ts = self.s, self.v, self.m, self.ts
		s_next = deepcopy(s); v_next = deepcopy(v)
		G = 6.67408e-11
		for i in xrange(self.n):
			acc = 0
			for j in xrange(self.n):
				if i==j: continue
				direction = s[j]-s[i]
				dist = np.sqrt( np.sum(direction**2) )
				acc += G*m[j]*direction / (dist*dist*dist)
			s_next[i] += ts*v[i] # note: velocity from !former! timestep
			v_next[i] += ts*acc
		self.s = s_next
		self.v = v_next
	
	def updating_plot(self, steps_per_plot=1): # not memory intense
		size = int(max(np.max(np.array(positions)), -np.min(np.array(positions)))*1.3)
		plt.ion()
		while True:
			plt.axis([-size,size,-size,size])
			for i in xrange(steps_per_plot): self.one_timestep()
			plt.scatter(self.s[:,0], self.s[:,1])
			plt.show()
			plt.pause(0.00001)
			plt.clf()

	def many_steps(self, steps): # for saving videos
		positions, velocities = [deepcopy(self.s)], [deepcopy(self.v)]
		for i in xrange(steps): self.one_timestep(); positions+=[deepcopy(self.s)]; velocities+=[deepcopy(self.v)]
		return positions, velocities

	

if __name__=='__main__':
	masses, positions, velocities = systems_importer.solar_system(first_n=9)
	masses, positions, velocities = systems_importer.sun_mercury_venus_earth_mars()
	
	nbody = NBody(timestep=5e3, masses=masses, positions=positions, velocities=velocities)
	nbody.updating_plot(steps_per_plot=150)
	#positions, velocities = nbody.many_steps(30000)
	#save_video(positions)
















