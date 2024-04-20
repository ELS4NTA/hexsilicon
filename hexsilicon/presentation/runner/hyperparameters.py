import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class Hyperparameters(ttk.Frame):

    def __init__(self, master=None, hyperparams=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        self.place_widgets()
        self.set_hyperparams(hyperparams)

    def create_widgets(self):
        self.hyperparameters_frame = ttk.Labelframe(self, text="Hiperparámetros")

        self.btn_group = ttk.Frame(self)
        self.reset_btn = ttk.Button(self.btn_group, text="Reiniciar", bootstyle="primary")
        self.update_btn = ttk.Button(self.btn_group, text="Actualizar", bootstyle="secondary")
        self.reset_btn.pack(side=LEFT, expand=YES, ipady=5, ipadx=15)
        self.update_btn.pack(side=LEFT, expand=YES, ipady=5, ipadx=15)

    def place_widgets(self):
        self.hyperparameters_frame.pack(side=TOP, expand=YES, fill=BOTH, padx=100, pady=100)
        self.btn_group.pack(side=BOTTOM, expand=YES, fill=BOTH, padx=100)

    def set_hyperparams(self, hyperparams):
        # clear hyperparameters_frame
        for widget in self.hyperparameters_frame.winfo_children():
            widget.destroy()

        for hyperparameter, value in hyperparams.items():
            ttk.Label(self.hyperparameters_frame, text=hyperparameter).pack()
            ttk.Scale(self.hyperparameters_frame, variable=ttk.DoubleVar(), from_=value[1], to=value[2],
                      orient="horizontal",
                      value=value[0]).pack()

        self.hyperparameters_frame.pack(side=TOP, expand=YES, fill=BOTH, padx=100, pady=100)
