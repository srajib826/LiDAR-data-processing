import PyLidar3
import time
import datetime # Time module

port = "com9" #windows

Obj = PyLidar3.YdLidarX4(port) #PyLidar3.your_version_of_lidar(port,chunk_size) 
file_path = r"C:\LiDAR-data-processing\ydlidar-X4\ydlidar_data_trunk3_gnt=4.txt"
# gn_t = 1.46 m, gn_t = 4.03

if(Obj.Connect()):
    print(Obj.GetDeviceInfo())
    gen = Obj.StartScanning()
    t = time.time() # start time 
    final_data = {}
    with open(file_path, "w") as f:
        while (time.time() - t) < 15: #scan for 30 seconds
            time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            final_data = {"timestamp":time_stamp}
            final_data.update(next(gen))
            f.write(f"{str(final_data)}\n")
            time.sleep(0.5)
    Obj.StopScanning()
    Obj.Disconnect()
    print("Done\n")
else:
    print("Error connecting to device")