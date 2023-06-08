names = ["Ash", "David", "Elena", "Karen"]
places = {
    "david" : "Earth",
    "jim" : "Mars",
    "Ken" : "Pluto" 
}

seperator = "/"
print(seperator.join(names))

print(seperator.join(places),"are in", seperator.join(places.values()))
