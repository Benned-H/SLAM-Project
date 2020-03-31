# Working with multivariate Gaussians
# Author: Benned Hedegaard 3/27/2020
# Last revised 3/27/2020

from time import sleep
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d

class Gaussian_2D:
	def __init__(self, _mu, _cov_matrix):
		self.mu = _mu
		self.cov_matrix = _cov_matrix

	def p(self, x):
		part1 = 1.0 / np.sqrt(np.linalg.det(2*np.pi*self.cov_matrix))
		sigma_inv = np.linalg.inv(self.cov_matrix)
		matrix_product = np.matmul(np.transpose(x-self.mu), np.matmul(sigma_inv, (x-self.mu)))
		part2 = np.exp(-0.5*matrix_product)
		return part1*part2

def main():
	mean = np.array([0,0])
	cov = np.array([[1,0],
					[0,1]])
	g = Gaussian_2D(mean, cov)

	fig = plt.figure()
	ax = plt.axes(projection="3d")

	increments = 100
	xs = np.linspace(-10, 10, increments)
	ys = np.linspace(-10, 10, increments)
	X, Y = np.meshgrid(xs, ys)

	Z = np.zeros((increments,increments))
	for i,x in enumerate(xs):
		for j,y in enumerate(ys):
			point = np.array([x,y])
			Z[i,j] = g.p(point)

	ax.plot_wireframe(X,Y,Z)
	ax.set_xlabel('x')
	ax.set_ylabel('y')
	ax.set_zlabel('z')
	plt.show()

if __name__ == "__main__":
	main()