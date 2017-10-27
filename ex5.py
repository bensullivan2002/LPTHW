name = "Zed A. Shaw"
age = 35
height = 74
height_cm = round((height * 2.54), 1)
weight = 180
weight_kg = round((weight * 0.45), 1)
eyes = "Blue"
teeth = "White"
hair = "Brown"

print(f"Let's talk about {name}.")
print(f"He's {height_cm} centimetres tall.")
print(f"He's {weight_kg} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")


total = round((age + height_cm + weight_kg), 1)
print(f"If I add {age} and {height_cm} and {weight_kg} I get {total}.")
