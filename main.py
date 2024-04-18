import json

f = open("octalData.json")
octalData = json.load(f)

f2 = open("hexaData.json")
hexaData = json.load(f2)
# make each class separately (Binary, Decimal, Octal, HexaDecimal)
# define a function that performs each conversion from each class
#   e.g in Binary class ( binary to octal)
# let user choose from which to which to convert
# take proper input from the user
# display the equivalent

# the Binary class


class Binary():
    def __init__(self, binary):
        self.binary = binary

    def toDecimal(self):
        binary = self.binary
        if "." in binary:
            beforePoint, afterPoint = binary.split(".")
        else:
            beforePoint = binary
            afterPoint = ""
        # for pre-decimal point part
        decimal = 0
        for i in range(len(beforePoint)-1, -1, -1):
            if beforePoint[i] == "1":
                power = len(beforePoint)-1-i
                decimal += 2**power

        # for after decimal point part
        power = -1
        for bit in afterPoint:
            if bit == "1":
                decimal += 2**power
            power -= 1

        return decimal

    def toOctal(self):
        binary = self.binary

        if "." in binary:
            beforePoint, afterPoint = binary.split(".")
        else:
            beforePoint = binary
            afterPoint = ""
        octal = ""

        while len(beforePoint) != 0:
            if len(beforePoint) >= 3:
                key = beforePoint[-3:]
                octal += octalData[key]
                beforePoint = beforePoint[:-3]
            else:
                while len(beforePoint) != 3:
                    beforePoint = "0" + beforePoint

        octal = octal[::-1] + "."

        while len(afterPoint) != 0:
            if len(afterPoint) >= 3:
                key = afterPoint[:3]
                octal += octalData[key]
                if len(afterPoint) > 3:
                    afterPoint = afterPoint[3:]
                else:
                    break
            else:
                if len(afterPoint) != 0:
                    afterPoint += "0"
        return octal

    def toHexaDecimal(self):
        binary = self.binary

        if "." in binary:
            beforePoint, afterPoint = binary.split(".")
        else:
            beforePoint = binary
            afterPoint = ""
        hexa = ""

        while len(beforePoint) != 0:
            if len(beforePoint) >= 4:
                key = beforePoint[-4:]
                hexa += hexaData[key]
                beforePoint = beforePoint[:-4]
            else:
                while len(beforePoint) != 4:
                    beforePoint = "0" + beforePoint

        hexa = hexa[::-1] + "."

        while len(afterPoint) != 0:
            if len(afterPoint) >= 4:
                key = afterPoint[:4]
                hexa += hexaData[key]
                if len(afterPoint) > 4:
                    afterPoint = afterPoint[4:]
                else:
                    break
            else:
                if len(afterPoint) != 0:
                    afterPoint += "0"
        return hexa


class Decimal():
    def __init__(self, decimal):
        self.decimal = decimal

    def toBinary(self):
        decimal = self.decimal

        if "." in decimal:
            beforePoint, afterPoint = decimal.split(".")
        else:
            beforePoint = decimal
            afterPoint = "0"

        # for beforePoint
        binary = ""

        beforePoint = int(beforePoint)
        if beforePoint == 0:
            binary += "0"
        while beforePoint != 0:
            binary += str(beforePoint % 2)
            beforePoint = int(beforePoint/2)
        binary = binary[::-1]

        # for afterPoint

        carries = ""
        afterPoint = float("0." + afterPoint)
        for i in range(7):
            if afterPoint == 0.00:
                break
            if afterPoint == 1.00:
                carries += str(afterPoint)[0]
                break
            afterPoint *= 2
            if afterPoint > 1:
                carries += str(afterPoint)[0]
                afterPoint = float(afterPoint)-1
            elif afterPoint < 1:
                carries += str(afterPoint)[0]

        binary = binary + "." + carries
        return binary

    def toOctal(self):
        decimal = self.decimal
        if "." in decimal:
            beforePoint, afterPoint = decimal.split(".")
        else:
            beforePoint = decimal
            afterPoint = "0"

        # for beforePoint
        octal = ""

        beforePoint = int(beforePoint)
        if beforePoint == 0:
            octal += "0"
        while beforePoint != 0:
            octal += str(beforePoint % 8)
            beforePoint = int(beforePoint/8)
        octal = octal[::-1]

        # for afterPoint

        carries = ""
        afterPoint = float("0." + afterPoint)
        for i in range(5):
            if afterPoint == 0.00:
                break
            if float(str(afterPoint)[2:]) == 0.00:
                carries += str(afterPoint)[0]
                break
            afterPoint *= 8

            carries += str(afterPoint)[0]
            afterPoint = float(afterPoint)-float(str(afterPoint)[0])

        octal = octal + "." + carries
        return octal

    def toHexaDecimal(self):
        decimal = self.decimal

        if "." in decimal:
            beforePoint, afterPoint = decimal.split(".")
        else:
            beforePoint = decimal
            afterPoint = "0"

        # for beforePoint
        hexa = ""

        beforePoint = int(beforePoint)
        if beforePoint == 0:
            hexa += "0"
        while beforePoint != 0:
            remainder = beforePoint % 16
            if remainder >= 10:
                hexa += hexaData[str(remainder)]
            else:
                hexa += str(remainder)
            beforePoint = int(beforePoint/16)
        hexa = hexa[::-1]

        # for afterPoint

        carries = ""

        afterPoint = float("0." + afterPoint)
        for i in range(5):

            if float(afterPoint) == 0.00:
                break
            if float(str(afterPoint)[str(afterPoint).index(".")+1:]) == 0.00:
                if int(str(afterPoint)[:str(afterPoint).index(".")]) >= 10:
                    carries += hexaData[str(afterPoint)
                                        [:str(afterPoint).index(".")]]

                else:
                    carries += str(afterPoint)[:str(afterPoint).index(".")]
            else:
                afterPoint = str(float(afterPoint) * 16)
                if int(str(afterPoint)[:str(afterPoint).index(".")]) >= 10:

                    carries += hexaData[str(afterPoint)
                                        [:str(afterPoint).index(".")]]

                else:
                    carries += str(afterPoint)[:str(afterPoint).index(".")]

            afterPoint = float(afterPoint)-float(str(afterPoint)
                                                 [:str(afterPoint).index(".")])

        hexa = hexa + "." + carries
        return hexa


class Octal():
    def __init__(self, octal):
        self.octal = octal

    def toBinary(self):
        octal = self.octal

        if "." in octal:
            beforePoint, afterPoint = octal.split(".")
        else:
            beforePoint = octal
            afterPoint = ""
        binary = ""

        # for the before Point

        for n in beforePoint:
            binary += octalData[n]
        # binary = binary[::-1]

        # for the after point
        after = ""
        for n in afterPoint:
            after += octalData[n]

        binary = binary + "." + after
        return binary

    def toDecimal(self):
        octal = self.octal

        if "." in octal:
            beforePoint, afterPoint = octal.split(".")
        else:
            beforePoint = octal
            afterPoint = ""
        # for pre-decimal point part
        decimal = 0
        power = 0
        for i in range(len(str(beforePoint))-1, -1, -1):
            decimal += (int(beforePoint[i])*(8**power))
            power += 1

        # for after decimal point part
        power = -1
        for i in range(len(str(afterPoint))):
            decimal += int(afterPoint[i])*(8**power)
            power -= 1

        return decimal

    def toHexaDecimal(self):
        octal = self.octal

        binary = self.toBinary()

        bnr = Binary(binary)
        hexa = bnr.toHexaDecimal()
        return hexa


class HexaDecimal():
    def __init__(self, hexa):
        self.hexa = hexa

    def toBinary(self):
        hexa = self.hexa

        if "." in hexa:
            beforePoint, afterPoint = hexa.split(".")
        else:
            beforePoint = hexa
            afterPoint = ""
        # for pre-decimal point part
        binary = ""
        for i in range(len(beforePoint)):
            binary += hexaData[beforePoint[i]]
        binary += "."
        for i in range(len(afterPoint)):
            binary += hexaData[afterPoint[i]]

        return binary

    def toDecimal(self):
        hexa = self.hexa

        hexadict = {
            "A": "10",
            "B": "11",
            "C": "12",
            "D": "13",
            "E": "14",
            "F": "15"
        }

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
        return decimal

    def toOctal(self):
        hexa = self.hexa

        binary = self.toBinary()
        bnr = Binary(binary)
        octal = bnr.toOctal()
        return octal
