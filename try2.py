import json

f3 = open("hexaData.json")
hexaData = json.load(f3)
carries = ""
octal_bit = ""
afterPoint = "0.85"


for i in range(5):
    if float(afterPoint) == 0.00:
        break
    if float(str(afterPoint)[str(afterPoint).index(".")+1:]) == 0.00:

        if int(str(afterPoint)[:str(afterPoint).index(".")]) >= 10:
            carries += octalData[str(afterPoint)[:str(afterPoint).index(".")]]
        else:
            carries += str(afterPoint)[:str(afterPoint).index(".")]
        break
    afterPoint = str(float(afterPoint) * 8)

    carries += octal_bit
    # print(octal_bit)
    afterPoint = float(afterPoint)-float(str(afterPoint)
                                         [:str(afterPoint).index(".")])
print(carries)
