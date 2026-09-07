'''
要求实现以下功能，全部用 print 输出结果

1. 已知距离 3200 米，用时 4.5 分钟，计算车速（km/h），保留 2 位小数
2. 把这个车速转换成 m/s，保留 3 位小数
3. 已知限速 50 km/h，判断上面的车速是否超速（用比较运算符，输出 True/False）
4. 计算超速百分比：(实际车速 - 限速) / 限速 * 100，保留 1 位小数
5. 用 f-string 输出一句完整的话，例如："实测车速 42.67 km/h（11.852 m/s），限速 50 km/h，是否超速：False"
'''
def calculate_speed_kmh(distance_m, time_min):
    distance_km = distance_m / 1000
    time_hour = time_min / 60
    speed_kmh = distance_km / time_hour
    return speed_kmh

def calculate_speed_ms(distance_m, time_min):
    time_s = time_min * 60
    speed_ms = distance_m / time_s
    return speed_ms

def is_overspeed(speed_kmh):
    return speed_kmh > 50

def percent_overspeed(speed_kmh):
    percentage = (speed_kmh - 50) / 50 * 100
    return percentage

distance = 3200
time = 4.5
speed_km_per_hour = calculate_speed_kmh(distance, time)
speed_m_per_s = calculate_speed_ms(distance, time)
is_overspeed_now = is_overspeed(speed_km_per_hour)
percentage_overspeed = percent_overspeed(speed_km_per_hour)
print(f"实测车速{speed_km_per_hour:.2f}km/h({speed_m_per_s:.3f}m/s),"
      f"限速50km/h,是否超速:{is_overspeed_now}")