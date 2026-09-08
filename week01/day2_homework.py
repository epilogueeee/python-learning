speeds = [45, 62, 38, 71, 55, 83, 29, 67, 51, 44,
          76, 33, 58, 91, 42, 65, 37, 79, 48, 56]
speed_limit = 50

#count overspeed vehicle number
def count_overspeed(speeds, speed_limit):
    n_os = 0
    n_tt = 0
    for s in speeds:
        if s > speed_limit:
            n_os += 1
        n_tt += 1
    os_per = n_os / n_tt
    return n_os, os_per

n_os_1, os_per_1 = count_overspeed(speeds, speed_limit)
print(f"{n_os_1} vehicles overspeed, the percentage is {os_per_1:.1f}")

#find max and min of speeds
def find_max_min(speeds):
    max = speeds[0]
    min = speeds[0]
    for i in speeds:
        if i > max:
            max = i
        if i < min:
            min = i
    return max, min

max, min = find_max_min(speeds)
print(f"max speed is {max}, min speed is {min}")

#count by interval
def count_interval(speeds):
    interval_1 = 0
    interval_2 = 0
    interval_3 = 0
    interval_4 = 0
    interval_5 = 0
    for i in speeds:
        if i < 20:
            interval_1 += 1
        elif i < 40:
            interval_2 += 1
        elif i < 60:
            interval_3 += 1
        elif i < 80:
            interval_4 += 1
        else:
            interval_5 += 1
    return interval_1, interval_2, interval_3, interval_4, interval_5

val_1, val_2, val_3, val_4, val_5 = count_interval(speeds)
print(f"[0, 20): {'*' * val_1} {val_1} vehicles\n"
      f"[20, 40): {'*' * val_2} {val_2} vehicles\n"
      f"[40, 60): {'*' * val_3} {val_3} vehicles\n"
      f"[60, 80): {'*' * val_4} {val_4} vehicles\n"
      f"[80,   ): {'*' * val_5} {val_5} vehicles")

#locate overspeed vehicle
def locate_os(speeds, speed_limit):
    for i, s in enumerate(speeds, start = 1):
        if s > speed_limit:
            print(f"the overspeed vehicle is number {i}, speed is {s}, over {s - speed_limit} km/h")
    return

locate_os(speeds, speed_limit)