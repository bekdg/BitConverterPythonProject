import json
f = open("hexaData.json")
hexaData = json.load(f)

hexadict = {
    "A": "10",
    "B": "11",
    "C": "12",
    "D": "13",
    "E": "14",
    "F": "15"
}
hexa = input("Hexa Decimal: ")

if "." in hexa:
    beforePoint, afterPoint = hexa.split(".")
else:
    beforePoint = hexa
    afterPoint = ""
# for pre-decimal point part
decimal = 0
power = 0
for i in range(len(str(beforePoint))-1, -1, -1):
    try:
        decimal += (int(beforePoint[i])*(16**power))
    except:
        decimal += (int(hexadict[beforePoint[i]])*(16**power))
    power += 1

# for after decimal point part
power = -1
for i in range(len(str(afterPoint))):
    try:
        decimal += (int(beforePoint[i])*(16**power))
    except:
        decimal += (int(hexadict[beforePoint[i]])*(16**power))
    power -= 1

print(decimal)
