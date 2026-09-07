def calculate_speed(distance_km, time_str):
    time_min = float(time_str)
    time_hour = time_min / 60
    speed = distance_km / time_hour
    return speed

distance = 12.5
time_taken = "18"
result = calculate_speed(distance, time_taken)
print(f"average speed is {result:.2f} km/h")