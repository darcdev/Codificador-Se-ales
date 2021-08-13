from tkinter import *
import tkinter as ttk
from re import search
from PIL import ImageTk, Image
from Plotter import Plotter
from utils.transform import limitBits


class GUI:
    def __init__(self):
        # Ventana Principal
        self.frame = Tk()
        self.plotter = Plotter()
        # Define config window
        self.frame.geometry("500x500")
        self.frame.resizable(width=False, height=False)
        self.frame.title("Codificacion de Señales")
        self.frame.configure(bg="#607d8b")

        # Image
        imagePrincipal = "./img/signal.png"
        openImage = Image.open(imagePrincipal)
        resized_image = openImage.resize((400, 245), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(resized_image)
        self.image = ttk.Label(self.frame, image=img, bg="#607d8b")

        # labels
        self.dataBinary = StringVar(value="")
        self.dataBinary.trace(
            "w", lambda name, index, mode, textGen=self.dataBinary: limitBits(textGen)
        )

        self.errorMessage = StringVar()
        self.title = ttk.Label(
            self.frame, text="Codificación de señales", font=("Courier", 20)
        )
        self.labelCodify = ttk.Label(
            self.frame, text="Digite Una Señal Binaria:", font=("Courier", 12)
        )
        self.errorMessage = ttk.Label(
            self.frame, text=self.errorMessage.get(), bg="#607d8b"
        )
        # buttons
        self.codifyButton = ttk.Button(
            self.frame, text="Codificar", command=self.showGraphs
        )
        # Inputs
        self.dataBinary = ttk.Entry(self.frame, textvariable=self.dataBinary)

        # Blocks
        self.title.pack(side=TOP, padx=15, pady=20)
        self.image.place(x=50, y=50, width=400, height=300)
        self.labelCodify.place(x=90, y=350, width=300, height=30)
        self.dataBinary.place(x=20, y=400, width=300, height=30)
        self.codifyButton.place(x=330, y=400, width=130, height=30)
        self.errorMessage.place(x=20, y=440, width=300, height=30)
        self.frame.mainloop()

    def verifiyDataBinary(self):

        # Borra el contenido que tenga en un momento dado la caja de texto
        regExp = "[a-zA-Z2-9 ]"
        signalData = self.dataBinary.get()
        mensaje = ""

        if search(regExp, signalData) or self.dataBinary.get() == "":
            mensaje = "La información de la señal no es valida"
        elif len(signalData) < 16 or len(signalData) > 16:
            mensaje = "La informacion debe tener 16 bits"
        self.errorMessage.config(text=mensaje, bg="#000", fg="#fff")

        if mensaje != "":
            return True
        else:
            return False

    def showGraphs(self):
        isError = self.verifiyDataBinary()
        signalData = self.dataBinary.get()
        if not isError:
            self.plotter.graph(signalData)
            self.errorMessage.config(text="", bg="#607d8b")
