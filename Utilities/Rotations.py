import numpy as np

def create_rotation_matrix(a,b,g):
	"""
	Inputs: Yaw (alpha), pitch (beta), and roll (gamma) angles.
	Returns the 3x3 rotation matrix for the given yaw, pitch, and roll values.
	Formula from Planning Algorithms by Steven M. LaValle.
	"""
	matrix = np.array([	[np.cos(a)*np.cos(b),	np.cos(a)*np.sin(b)*np.sin(g)-np.sin(a)*np.cos(g),	np.cos(a)*np.sin(b)*np.cos(g)+np.sin(a)*np.sin(g)],
						[np.sin(a)*np.cos(b),	np.sin(a)*np.sin(b)*np.sin(g)+np.cos(a)*np.cos(g),	np.sin(a)*np.sin(b)*np.cos(g)-np.cos(a)*np.sin(g)],
						[-np.sin(b),			np.cos(b)*np.sin(g),								np.cos(b)*np.cos(g)]	])

	return matrix

def create_quaternion(r):
	"""
	Input: An RPY rotation matrix r.
	Returns the unit quaternion representation of the rotation.
	Formula from Lecture 4 of ECE 232, Spring 2020 taught by Thomas Howard.
	"""
	if r.shape != (3,3):
		print("Invalid input given!")
		return

	eta = np.sqrt(r[0,0]+r[1,1]+r[2,2]+1)/2
	vector = np.array([		np.sign(r[2,1]-r[1,2])*np.sqrt(r[0,0]-r[1,1]-r[2,2]+1)/2,
							np.sign(r[0,2]-r[2,0])*np.sqrt(r[1,1]-r[2,2]-r[0,0]+1)/2,
							np.sign(r[1,0]-r[0,1])*np.sqrt(r[2,2]-r[0,0]-r[1,1]+1)/2	])

	check = np.sqrt(eta**2 + vector[0]**2 + vector[1]**2 + vector[2]**2)
	print("\nChecking unit quaternion:", check)

	return (eta,vector)

def find_RPY(r):
	"""
	Input: An RPY rotation matrix r.
	Returns the roll, pitch, and yaw corresponding to the rotation matrix.
	Formula from Planning Algorithms by Steven M. LaValle.

	Assumes that r[0,0] and r[2,2] != 0, which I'm not sure how to deal with.
	"""

	a = np.arctan2(r[1,0], r[0,0])
	b = np.arctan2(-r[2,0], np.sqrt(r[2,1]**2+r[2,2]**2))
	g = np.arctan2(r[2,1],r[2,2])

	return (a,b,g)


def main():
	# Proof-of-concept: Does my code work with the identity rotation?
	m0 = create_rotation_matrix(0,0,0)
	q0 = create_quaternion(m0)
	print("\nIdentity rotation debug:")
	print(m0,q0)

	# Problem 1: (a,b,g) = (pi/6, 0, 0)
	m1 = create_rotation_matrix(np.pi/6,0,0)
	q1 = create_quaternion(m1)
	print("\nProblem 1:")
	print(m1,q1)

	# Problem 2: (a,b,g) = (pi/6, -pi/9, -pi/7)
	m2 = create_rotation_matrix(np.pi/6,-np.pi/9,-np.pi/7)
	q2 = create_quaternion(m2)
	print("\nProblem 2:")
	print(m2,q2)

	# Problem 3: R is given. Find RPY and quaternion.
	m3 = np.array([	[0.6533, -0.6533, -0.3827],
					[-0.2706, 0.2706, -0.9239],
					[0.7071, 0.7071, 0.0000]	])
	rpy3 = find_RPY(m3)
	q3 = create_quaternion(m3)
	print("\nProblem 3:")
	print(rpy3,q3)


if __name__ == "__main__":
	main()