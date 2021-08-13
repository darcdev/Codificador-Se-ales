import numpy as np
import matplotlib.pyplot as plt
from utils.transform import splitBits
from Encoder import Encoder


class Plotter:
    def __init__(self):
        self.TYPES_SIGNALS = [
            "MANCHESTER DIFERENCIAL",
            "MANCHESTER",
            "PSEUDOTERNARIA",
            "BIPOLAR-AMI",
            "NRZI",
            "NRZ-L",
        ]
        self.encoder = Encoder()

    def drawLines(self, ax, pos, *args, **kwargs):
        if ax == "x":
            for p in pos:
                plt.axvline(p, *args, **kwargs)
        else:
            for p in pos:
                plt.axhline(p, *args, **kwargs)

    def drawLabels(self, bits):

        # Labels axes x,y
        for tbit, bit in enumerate(bits):
            plt.text(tbit + 0.4, 12, str(bit))

        for itype, type in enumerate(self.TYPES_SIGNALS):
            plt.text(-3, (itype * 2) + 0.5, str(type))

        plt.gca().axis("off")

    def graph(self, bits):
        # Create a Label in New window

        # Split signal in bits
        signal = splitBits(bits)

        # Signal Trasnformed
        data = np.repeat(signal, 2)
        nrzl = np.array(self.encoder.encodeNRZL(data))
        nrzi = np.repeat(self.encoder.encodeNRZI(signal), 2)
        bipami = np.repeat(self.encoder.encodeBIPAMI(signal), 2)
        pseudoTern = np.repeat(self.encoder.encodePseudoTern(signal), 2)
        manchester = np.array(self.encoder.encodeManchester(data))
        manchesterDif = np.array(self.encoder.encodeManchesterDif(data))

        # Values Axe x
        t = 0.5 * np.arange(len(data))

        # Divisor lines axes x,y
        self.drawLines("x", range(16), color=".5", linewidth=2, linestyle="--")
        self.drawLines(
            "y",
            [0.5, 2.5, 4.5, 6.5, 8.5, 10.5],
            color=".5",
            linewidth=2,
            linestyle="--",
        )

        plt.step(t, nrzl + 10, "red", linewidth=2, where="post")
        plt.step(t, nrzi + 8, "red", linewidth=2, where="post")
        plt.step(t, bipami + 6, "red", linewidth=2, where="post")
        plt.step(t, pseudoTern + 4, "red", linewidth=2, where="post")
        plt.step(t, manchester + 2, "red", linewidth=2, where="post")
        plt.step(t, manchesterDif, "red", linewidth=2, where="post")

        plt.ylim([-1, 12])

        self.drawLabels(bits)

        plt.show()
