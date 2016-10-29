
import numpy as np

def sun_earth():
	masses     = np.array([1.99e30, 5.97e24],       dtype=np.float)
	positions  = np.array([[0,0,0], [149.6e9,0,0]], dtype=np.float)
	velocities = np.array([[0,0,0], [0,3e4,0]],     dtype=np.float)
	return masses, positions, velocities

def sun_mercury_venus_earth_mars():
	return solar_system(first_n=5)

def solar_system(first_n=9):
	masses     = np.array([1.99e30, 3.285e23,      4.867e24,      5.97e24,       6.417e23,     1898.2e24,     568.34e24,     8.68e25,       1.024e26]    [:first_n], dtype=np.float)
	positions  = np.array([[0,0,0], [57.91e9,0,0], [108.2e9,0,0], [149.6e9,0,0], [228e9,0,0],  [778.5e9,0,0], [1.43e12,0,0], [2.87e12,0,0], [4.5e12,0,0]][:first_n], dtype=np.float)
	velocities = np.array([[0,0,0], [0,48e3,0],    [0,35.02e3,0], [0,3e4,0],     [0,2.41e4,0], [0,1.31e4,0],  [0,9.68e3,0],  [0,6.8e3,0],   [0,5.4e3,0]] [:first_n], dtype=np.float)
	return masses, positions, velocities


