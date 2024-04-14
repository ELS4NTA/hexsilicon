import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from hexsilicon.presentation.administration.hyperparameters import \
    Hyperparameters
from hexsilicon.presentation.execution.administration.information import \
    Information


class Dashboard(ttk.Notebook):

    def __init__(self, master=None):
        super().__init__(master, bootstyle="primary")
        self.info_frame = Information(self)
        self.info_frame.pack(fill=BOTH, expand=YES)
        self.add(self.info_frame, text='Información')

        self.hyper_frame = Hyperparameters(self)
        self.hyper_frame.pack(fill=BOTH, expand=YES)
        self.add(self.hyper_frame, text='Hiperparametros')

    def get_history_frame(self):
        return self.info_frame.history

    def get_graphic_frame(self):
        return self.info_frame.graphic

    def set_hyperparams(self, hyperparams):
        self.hyper_frame.set_hyperparams(hyperparams)
