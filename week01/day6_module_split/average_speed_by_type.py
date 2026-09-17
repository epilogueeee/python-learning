from traffic_io import read_records

def average_speed_by_type(records: list) -> dict:
    """return avrage speed of each type vehicle"""
    result_speeds = {}
    result = {}
    for row in records:
        vehicle_type = row["vehicle_type"]
        speed = row["speed"]
        result_speeds.setdefault(vehicle_type, []).append(speed)
    for vehicle_type, speeds in result_speeds.items():
        result[vehicle_type] = sum(speeds) / len(speeds)
    return result

if __name__ == "__name__":

    data_path =r"C:\Users\HSC\PyLearning\python-learning\traffic_raw.csv"
    records = read_records(data_path)
    print(average_speed_by_type(records))
