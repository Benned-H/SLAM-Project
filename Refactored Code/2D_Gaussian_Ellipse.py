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