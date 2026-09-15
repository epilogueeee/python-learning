line = "  08:30:15 , 2 , CAR , 62.5  \n"

parts = line.rstrip("\n").split(",")
cleaned = []
for p in parts:
    cleaned.append(p.strip().lower())

time = cleaned[0]
hms = time.split(":")
seconds = 3600 * int(hms[0]) + 60 * int(hms[1]) + int(hms[2])

joint = "|".join(cleaned)

is_car = "car" in line.lower()

print(cleaned)
print(seconds)
print(joint)
print(is_car)
print(f"{float(cleaned[3]):>8.2f}")