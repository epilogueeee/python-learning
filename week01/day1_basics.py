#变量与类型
speed = 60
distance = 1.5
road_name = "zhongshanlu"
is_congested = True
print(type(speed))

#类型转换
speed_str = "60"
speed_num = int(speed_str)
print(speed_str + "1")
print(speed_num + 1)

#f-string格式化
name = "zhongshanlu"
v = 47.3826
print(f"{name}的平均车速是{v} km/h")  #第一个f是formatted，一个标记，表示{}里面是变量或一些表达式，f必须紧贴""的内容
print(f"{name}的平均车速是{v:.2f} km/h")
print(f"{name}的平均车速是{v:.1f} km/h")