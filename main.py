# Dictionaries
# KEY : VALUE
d = {"Helsinki": "HEL", "Saigon": "SGN"}
print(d)
d["Budapest"] = "BUD"
print(d)
print(d["Helsinki"])

## Delete Element

del d["Budapest"]
print(d)
if "Helsinki" in d:
    print ("Helsinki vorhanden")

print(d["Saigon"])
print(d.get("Saigon"))
