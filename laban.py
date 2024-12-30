import numpy as np
from extract import (
    calculate_instantaneous_speed,
    calculate_average_speed,
    calculate_instantaneous_acceleration,
    calculate_average_acceleration,
    calculate_direction_changes,
    calculate_total_area,
    calculate_stop_time
)

class LabanMovementAnalysis:
    def __init__(self, trajectories, fps):
        self.trajectories = trajectories
        self.fps = fps

    def analyze_effort(self):
        efforts = []
        for trajectory in self.trajectories:
            effort = self.calculate_effort(trajectory)
            efforts.append(effort)
        return efforts

    def calculate_effort(self, trajectory):
        speeds = calculate_instantaneous_speed(trajectory, self.fps)
        avg_speed = calculate_average_speed(speeds)
        accelerations = calculate_instantaneous_acceleration(speeds, self.fps)
        avg_acceleration = calculate_average_acceleration(accelerations)
        direction_changes = calculate_direction_changes(trajectory)
        total_area = calculate_total_area(trajectory)
        stop_time = calculate_stop_time(speeds, self.fps)

        effort = {
            "speeds": speeds,
            "avg_speed": avg_speed,
            "accelerations": accelerations,
            "avg_acceleration": avg_acceleration,
            "direction_changes": direction_changes,
            "total_area": total_area,
            "stop_time": stop_time
        }
        return effort

    def interpret_effort(self, efforts):
        interpretations = []
        for effort in efforts:
            interpretation = self.interpret_single_effort(effort)
            interpretations.append(interpretation)
        return interpretations

    def interpret_single_effort(self, effort):
        interpretation = {
            "speed": self.interpret_speed_effort(effort["avg_speed"]),
            "acceleration": self.interpret_acceleration_effort(effort["avg_acceleration"]),
            "direction_changes": self.interpret_direction_changes(effort["direction_changes"]),
            "total_area": self.interpret_total_area(effort["total_area"]),
            "stop_time": self.interpret_stop_time(effort["stop_time"])
        }
        return interpretation

    def interpret_speed_effort(self, avg_speed):
        return "Fast" if avg_speed > 1.0 else "Slow"

    def interpret_acceleration_effort(self, avg_acceleration):
        return "High" if avg_acceleration > 0.5 else "Low"

    def interpret_direction_changes(self, direction_changes):
        return "Frequent" if len(direction_changes) > 10 else "Infrequent"

    def interpret_total_area(self, total_area):
        return "Large" if total_area > 10.0 else "Small"

    def interpret_stop_time(self, stop_time):
        return "Long" if stop_time > 5.0 else "Short"

