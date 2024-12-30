import numpy as np
import cv2
from scipy.interpolate import splprep, splev
from scipy.signal import savgol_filter

PIXELS_TO_METERS = 0.0002645833 
distance_dict = {}

"""Function to Interpolate Trajectory"""
def interpolate_trajectory(centroidarr):
    if len(centroidarr) < 2:
        return centroidarr
    centroidarr = np.array(centroidarr)
    tck, u = splprep([centroidarr[:, 0], centroidarr[:, 1]], s=0)
    unew = np.linspace(0, 1, num=100)  # Número ajustável de pontos interpolados
    new_points = splev(unew, tck)
    return list(zip(new_points[0], new_points[1]))

"""Function to Calculate Distance"""
def calculate_distance(centroidarr):
    interpolated = interpolate_trajectory(centroidarr)
    distance = 0.0
    for i in range(1, len(interpolated)):
        x1, y1 = interpolated[i - 1]
        x2, y2 = interpolated[i]
        distance += np.hypot(x2 - x1, y2 - y1) * PIXELS_TO_METERS
    return distance

"""Function to Save Distance to a File"""
def save_distance_to_file(save_dir, track_id, distance):
    if track_id not in distance_dict:
        distance_dict[track_id] = 0.0
    distance_dict[track_id] += distance
    
    # Sobrescrever o arquivo com a distância acumulada para cada ID
    with open(f"{save_dir}/distances.txt", "w") as f:
        for id, dist in distance_dict.items():
            f.write(f"ID {id} Distance: {dist:.2f} meters\n")

"""Function to Calculate Instantaneous Speed"""
def calculate_instantaneous_speed(centroidarr, frame_times):
    speeds = []
    for i in range(1, len(centroidarr)):
        x1, y1 = centroidarr[i - 1]
        x2, y2 = centroidarr[i]
        distance = np.hypot(x2 - x1, y2 - y1) * PIXELS_TO_METERS
        time_diff = frame_times[i] - frame_times[i - 1]  # Intervalo de tempo real
        if time_diff > 0:
            speeds.append(distance / time_diff)
    return speeds

"""Function to Calculate Average Speed"""
def calculate_average_speed(speeds):
    if len(speeds) == 0:
        return 0
    return sum(speeds) / len(speeds)

"""Function to Calculate Instantaneous Acceleration"""
def calculate_instantaneous_acceleration(speeds, fps):
    smoothed_speeds = savgol_filter(speeds, window_length=5, polyorder=2)  # Suaviza velocidades
    accelerations = []
    for i in range(1, len(smoothed_speeds)):
        acceleration = (smoothed_speeds[i] - smoothed_speeds[i - 1]) * fps
        accelerations.append(acceleration)
    return accelerations

"""Function to Calculate Average Acceleration"""
def calculate_average_acceleration(accelerations):
    if len(accelerations) == 0:
        return 0
    return sum(accelerations) / len(accelerations)

"""Function to Calculate Direction Changes"""
def calculate_direction_changes(centroidarr, min_vector_magnitude=1e-6):
    direction_changes = []
    for i in range(2, len(centroidarr)):
        x1, y1 = centroidarr[i - 2]
        x2, y2 = centroidarr[i - 1]
        x3, y3 = centroidarr[i]
        v1 = np.array([x2 - x1, y2 - y1])
        v2 = np.array([x3 - x2, y3 - y2])
        if np.linalg.norm(v1) < min_vector_magnitude or np.linalg.norm(v2) < min_vector_magnitude:
            continue
        angle = np.arccos(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))
        direction_changes.append(np.degrees(angle))
    return direction_changes

"""Function to Calculate Total Area Covered"""
def calculate_total_area(centroidarr):
    if len(centroidarr) < 3:
        return 0
    points = np.unique((np.array(centroidarr) * PIXELS_TO_METERS).astype(np.float32), axis=0)
    hull = cv2.convexHull(points)
    return cv2.contourArea(hull)

"""Function to Calculate Stop Time"""
def calculate_stop_time(speeds, fps, threshold=0.1):
    stop_time = 0
    for speed in speeds:
        if speed < threshold:
            stop_time += 1 / fps
    return stop_time