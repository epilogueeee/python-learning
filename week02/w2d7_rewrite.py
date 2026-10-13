speeds = [62.5, 45.0, 78.3, 55.1, 91.2, 38.7, 66.0, 59.9]
times  = ["08:30:15", "08:30:22", "08:30:31", "08:30:40",
          "08:31:02", "08:31:15", "08:31:33", "08:31:50"]

# A1
result = []
for s in speeds:
    if s >= 60:
        result.append(round(s - 60, 1))

result_new = [round(s - 60, 1) for s in speeds if s >= 60]
assert result == result_new

# A2
result = []
for t, s in zip(times, speeds):
    result.append(f"{t} {'⚠' if s > 80 else '·'} {s}")

result_new = [f"{t} {'⚠' if s > 80 else '·'} {s}" for t, s in zip(times, speeds)]
assert result == result_new

# A3
result = {}
for i, s in enumerate(speeds, 1):
    result[i] = s / 3.6

result_new = {i: s / 3.6 for i, s in enumerate(speeds, 1)}
assert result == result_new

# A4
result = set()
for t in times:
    result.add(t[:5])

result_new = set(t[:5] for t in times)
assert result == result_new

# A5
total = 0
for s in speeds:
    if s < 50:
        total += 1

total_new = sum(1 for s in speeds if s < 50)
assert result == result_new