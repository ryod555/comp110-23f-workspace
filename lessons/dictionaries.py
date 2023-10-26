"""Dictionaries lesson."""

flavors: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}

print("Made my dictionary.")
print(flavors)

flavors["mint"] = 3
print("added mint.")
print(flavors)

flavors.pop("mint")
print("removed mint.")
print(flavors)

print(flavors["chocolate"])
flavors["vanilla"] = 10
print(flavors["vanilla"])

"chocolate" in flavors

if "mint" in flavors:
    print(flavors["mint"])
else:
    print("no orders of mint baby grl")

for key in flavors:
    print(f"{key} has {flavors[key]} orders.")