import numpy as np


class Encoder:
    def encodeNRZL(self, data):
        nrzl = np.logical_xor(data, 1)
        return nrzl

    def encodeNRZI(self, data):
        memory = data[0]
        signal = []
        for index in range(len(data)):
            if data[index] == 1 and index != 0:
                memory = int(memory != 1)
                signal.append(memory)
            else:
                signal.append(memory)
        return signal

    def encodeBIPAMI(self, data):
        memory = 1
        signal = []
        for index in range(len(data)):
            if data[index] == 1 and memory == 1:
                signal.append(memory)
                memory = 0
            elif data[index] == 1 and memory == 0:
                signal.append(memory)
                memory = 1
            else:
                signal.append(0.5)
        return signal

    def encodePseudoTern(self, data):
        memory = 1
        signal = []
        for index in range(len(data)):
            if data[index] == 0 and memory == 1:
                signal.append(memory)
                memory = 0
            elif data[index] == 0 and memory == 0:
                signal.append(memory)
                memory = 1
            else:
                signal.append(0.5)
        return signal

    def encodeManchester(self, data):
        signal = []
        for index in range(len(data)):
            if (index + 1) % 2 == 0:
                signal.append(data[index])
            elif data[index] == 0:
                signal.append(1)
            elif data[index] == 1:
                signal.append(0)
        return signal

    def encodeManchesterDif(self, data):
        memory = data[0]
        signal = []
        for index in range(len(data)):
            if index == 0:
                signal.append(memory)
            elif (index + 1) % 2 == 0:
                signal.append(1 - memory)
                memory = 1 - memory
            elif data[index] == 0:
                signal.append(1 - memory)
                memory = 1 - memory
            elif data[index] == 1:
                signal.append(memory)
        return signal
