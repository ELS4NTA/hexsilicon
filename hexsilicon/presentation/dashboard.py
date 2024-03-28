import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from hexsilicon.presentation.hyperparameters import Hyperparameters
from hexsilicon.presentation.information import Information


class Dashboard(ttk.Notebook):

    def __init__(self, master=None):
        super().__init__(master, bootstyle="primary")
        info_frame = Information(self)
        info_frame.pack(fill=BOTH, expand=YES)
        self.add(info_frame, text='Information')

        hyper_frame = Hyperparameters(self)
        hyper_frame.pack(fill=BOTH, expand=YES)
        self.add(hyper_frame, text='Hyperparams')
