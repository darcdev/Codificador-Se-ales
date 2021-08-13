def splitBits(bits):
    return [int(char) for char in bits]


def limitBits(textGen):
    if len(textGen.get()) > 0:
        # donde esta el :5 limitas la cantidad d caracteres
        textGen.set(textGen.get()[:16])
