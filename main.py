# COLOR DATA PRACTICE

import json

# Load Color Data from JSON file
file = open("color-data.json", "r")
dataStr = file.read()
file.close()

color_data = json.loads(dataStr)

# 1
def displaycolor():
    for color in color_data:
        print(color["name"], color["family"])

# 2
def abovetwohund():
    for color in color_data:
        if color["brightness"] >= 200:
            print(color["name"], color["brightness"])

# 3
def redorpink():
    rorp = 0
    for color in color_data:
        if color["family"] == "Red" or color["family"] == "Pink":
            rorp += 1
    print(rorp)

# 4
def famsearch():
    num = 0
    whichfam = input("What color family would you like to search?")
    for i in range (len(color_data)):
        if color_data[i]["family"] == whichfam:
            num += 1
            print(color_data[i]["name"], color_data[i]["family"])
    print(num)

# 5
def letsearch():
    letnum = 0
    whichlet = input("What letter would you like to search for?")
    for color in color_data:
        if whichlet == color["name"][0]:
            letnum += 1
            print(color["name"])
    print(letnum)


# Extra 
# for color in color_data:
#     color["name"] = color["name"].upper()

# for color in color_data:
#     print(color["name"])
