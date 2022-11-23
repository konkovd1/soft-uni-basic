record_to_be_beaten_in_seconds = float(input())
distance_in_meters = float(input())
time_for_swimming_per_meter = float(input())

time_for_passing_distance = distance_in_meters*time_for_swimming_per_meter
delay = int(distance_in_meters/15)*12.5
needed_time = time_for_passing_distance+delay

total_time = abs(record_to_be_beaten_in_seconds - needed_time)

if record_to_be_beaten_in_seconds <= needed_time:
    print(f"No, he failed! He was {total_time:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {needed_time:.2f} seconds.")
