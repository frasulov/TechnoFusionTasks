def getXDigitInteger(num, digits=3):
    num = str(num)
    if len(num) < digits:
        difference = digits - len(num)
        return "0"*difference + num
    return num