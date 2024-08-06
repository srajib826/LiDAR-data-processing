import PyLidar3
import time
import datetime 
import sys

port = "/dev/ttyUSB0" 

Obj = PyLidar3.YdLidarX4(port) #PyLidar3.your_version_of_lidar(port,chunk_size)
start_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
print(f"Stat Time :{start_time}")
file_path = f"/home/rajib/LiDAR-data-processing/ydlidar-X4/{start_time}.txt"
# gn_t = 1.46 m, gn_t = 4.03

# give input in min.
capture_time = 0
if len(sys.argv) > 1:
    capture_time = int(sys.argv[1])*60
else :
    capture_time = 10*60   # default time is 10 min.

print(capture_time)


if(Obj.Connect()):
    print(Obj.GetDeviceInfo())
    gen = Obj.StartScanning()
    t = time.time() # start time 
    final_data = {}
    with open(file_path, "w") as f:
        while (time.time() - t) < capture_time: 
            time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            final_data = {"timestamp":time_stamp}
            final_data.update(next(gen))
            f.write(f"{str(final_data)}\n")
            time.sleep(0.5)
    Obj.StopScanning()
    Obj.Disconnect()
    end_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"End Time :{end_time}")
    print("Done\n")
else:
    print("Error connecting to device")