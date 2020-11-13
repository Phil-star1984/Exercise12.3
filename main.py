from functions import number_of_steps

x = (float(input("How many meters did you walk?: ")))
y = (float(input("How long is your step in meters?: ")))

print(f"It took you ", number_of_steps(distance_walked = x, length_of_step = y ), "steps to your finish.")
