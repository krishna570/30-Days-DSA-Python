import math

ab = int(input())
bc = int(input())
angle_deg = round(math.degrees(math.atan2(ab, bc)))
print(f"{angle_deg}\xb0")
