speeds = [45, 62, 38, 71, 55, 83, 29, 67, 51, 44,
          76, 33, 58, 91, 42, 65, 37, 79, 48, 56]
speed_limit = 50

#count overspeed vehicle number
def count_overspeed(speeds, speed_limit):
    n_os = 0
    for s in speeds:
        if s > speed_limit:
            n_os += 1
    os_per = n_os / len(speeds) * 100
    return n_os, os_per

n_os_1, os_per_1 = count_overspeed(speeds, speed_limit)
print(f"{n_os_1} vehicles overspeed, the percentage is {os_per_1:.1f}")

#find max and min of speeds
def find_max_min(speeds):
    max_speed = speeds[0]
    min_speed = speeds[0]
    for i in speeds:
        if i > max_speed:
            max_speed = i
        if i < min_speed:
            min_speed = i
    return max_speed, min_speed

max_speed, min_speed = find_max_min(speeds)
print(f"max speed is {max_speed}, min speed is {min_speed}")

#count by interval
def count_interval(speeds, bounds):
    count = [0] * (len(bounds) + 1)
    for s in speeds:
        for i, upper in enumerate(bounds):
            if s < upper:
                count[i] += 1
                break
        else:
            count[-1] += 1
    return count

bounds = [20, 40, 60, 80]
labels = ["[ 0, 20)", "[20, 40)", "[40, 60)", "[60, 80)", "[80,  ∞)"]
counts = count_interval(speeds, bounds)
for lb, c in zip(labels, counts):
    print(f"{lb}: {'*' * c} {c} vehicles")

#locate overspeed vehicle
def locate_os(speeds, speed_limit):
    for i, s in enumerate(speeds, start=1):
        if s > speed_limit:
            print(f"the overspeed vehicle is number {i}, speed is {s}, over {s - speed_limit} km/h")
    return

locate_os(speeds, speed_limit)