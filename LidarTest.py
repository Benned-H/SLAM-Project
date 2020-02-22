import PyLidar3
import time

lidar = PyLidar3.YdLidarX4("/dev/ttyUSB0")

if(lidar.Connect()):
    print(lidar.GetDeviceInfo())
    gen = lidar.StartScanning()
    t = time.time() # start time
    while (time.time() - t) < 5: # scan for 30sec
        print(next(gen))
        time.sleep(0.5)
    lidar.StopScanning()
    
    lidar.Disconnect()
    print("Device disconnected")
else:
    print("Error connecting to device")