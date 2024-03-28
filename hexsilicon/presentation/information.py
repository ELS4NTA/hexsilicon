import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from hexsilicon.presentation.history import History
from hexsilicon.presentation.graphic import Graphic

class Information(ttk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):


        self.history_frame = ttk.Labelframe(self, text="Historial")
        self.history = History(self.history_frame)
        self.history.pack(side=TOP)
        self.history_frame.pack(side=TOP, expand=YES, fill=BOTH, padx=100)

        self.graphic_frame = ttk.Labelframe(self, text="Gráfica")
        self.graphic = Graphic(self.graphic_frame)
        self.graphic.pack(side=TOP)
        self.graphic_frame.pack(side=TOP, expand=YES, fill=BOTH, padx=100)

