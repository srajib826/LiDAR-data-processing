import open3d as o3d
import numpy as np

# Load point cloud

pcd = o3d.io.read_point_cloud("pcd3.ply")

# Preprocess the point cloud (e.g., downsample, remove noise)
pcd = pcd.voxel_down_sample(voxel_size=0.05)
pcd, ind = pcd.remove_statistical_outlier(nb_neighbors=20, std_ratio=2.0)

# Cluster the point cloud to find different objects
labels = np.array(pcd.cluster_dbscan(eps=0.2, min_points=10))


# Find the cluster that represents the car
max_label = labels.max()
print(f"point cloud has {max_label + 1} clusters")

# Assuming the car is the largest cluster (you might need more logic here)
largest_cluster_index = np.argmax(np.bincount(labels[labels >= 0]))
car_points = np.asarray(pcd.points)[labels == largest_cluster_index]

# Calculate the centroid of the car
car_centroid = car_points.mean(axis=0)

# Measure the distance from the origin (LiDAR sensor) to the car centroid
distance = np.linalg.norm(car_centroid)
print(f"Distance to the object: {distance:.2f} meters")
