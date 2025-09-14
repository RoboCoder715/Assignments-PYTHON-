import numpy as np

data = np.genfromtxt("robot_path.csv", delimiter=",", skip_header=1, usecols=(0, 1))
x = data[:, 0]
y = data[:, 1]

distances = np.sqrt(np.diff(x)**2 + np.diff(y)**2)
total_distance = np.sum(distances)

dist_origin = np.sqrt(x**2 + y**2)
farthest_index = np.argmax(dist_origin)
farthest_point = (x[farthest_index], y[farthest_index])
farthest_distance = dist_origin[farthest_index]

positions = [tuple(pos) for pos in data]
visited = len(positions) != len(set(positions))

print(f"Total distance traveled by the robot: {total_distance}")
print(f"Farthest point from origin is {farthest_point} with distance {farthest_distance}")
print(f"Did the robot revisit a position? {'Yes' if visited else 'No'}")

with open("robot_results.txt", "w") as f:
    f.write(f"Total distance traveled by the robot: {total_distance}\n")
    f.write(f"Farthest point from origin: {farthest_point} with distance {farthest_distance}\n")
    f.write(f"Did the robot revisit a position? {'Yes' if visited else 'No'}\n")
