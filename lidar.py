# YdLidar Test Code
# Author: Benned Hedegaard

from PyLidar3 import YdLidarX4

def main():
	port = ""
	chunk_size = 6000
	lidar = YdLidarX4(chunk_size)

	print("Connect:",lidar.Connect())

	generator = lidar.StartScanning()
	print("Health Status:",lidar.GetHealthStatus())

if __name__ == "__main__":
	main()