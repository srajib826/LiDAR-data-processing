import PyLidar3
import time
import datetime # Time module
#Serial port to which lidar connected, Get it from device manager windows
#In linux type in terminal -- ls /dev/tty* 
# port = input("Enter port name which lidar is connected:") #windows
#port = "/dev/ttyUSB0" #linux
port = "com13"
Obj = PyLidar3.YdLidarX4(port) #PyLidar3.your_version_of_lidar(port,chunk_size) 
# file_path = r"C:\LiDAR-data-processing\ydlidar-X4\ydlidar_data.txt"

#obj2 = PyLidar3. YdLidarG4(port)


if(Obj.Connect()):
    print(Obj. GetCurrentFrequency())
    print(Obj.GetDeviceInfo())
    gen = Obj.StartScanning()
    t = time.time() # start time 
    # with open(file_path, "w") as f:
    final_data = {}
    while (time.time() - t) < 5: #scan for 30 seconds
        time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        final_data = {"timestamp":time_stamp}
        final_data.update(next(gen))
        print(f"{final_data}\n")
        break
        time.sleep(0.5)
    Obj.StopScanning()
    Obj.Disconnect()
else:
    print("Error connecting to device")