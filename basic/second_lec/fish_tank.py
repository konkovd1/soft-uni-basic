length = int(input())
width = int(input())
height = int(input())
filled_tank = float(input()) / 100

capacity = length * width * height
capacity_in_liters = capacity * 0.001
needed_liters = capacity_in_liters * (1 - filled_tank)

print(needed_liters)
