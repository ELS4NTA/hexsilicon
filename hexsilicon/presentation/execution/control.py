import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class Control(ttk.Labelframe):

    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()
        self.configure(text="Control")

    def create_widgets(self):
        self.back_button = ttk.Button(self, text="Atras")
        self.start_button = ttk.Button(
            self, text="Iniciar", command=self.master.start_execution)
        self.stop_button = ttk.Button(self, text="Detener")
        self.reset_button = ttk.Button(self, text="Reiniciar")
        self.back_button.pack(side=LEFT, padx=10)
        self.start_button.pack(side=LEFT, padx=10)
        self.stop_button.pack(side=LEFT, padx=10)
        self.reset_button.pack(side=LEFT, padx=10)
