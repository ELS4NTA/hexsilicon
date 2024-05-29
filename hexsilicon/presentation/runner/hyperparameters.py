from idlelib.tooltip import Hovertip

import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class Hyperparameters(ttk.Frame):

    def __init__(self, master=None, hyperparams=None):
        super().__init__(master)
        self.master = master
        self.values = {}
        self.start_values = {}
        self.hyperparams = hyperparams
        self.set_hyperparams_widgets(hyperparams)
        self.create_widgets()

    def create_widgets(self):
        self.btn_group = ttk.Frame(self)
        self.reset_btn = ttk.Button(self.btn_group, text="Reiniciar", bootstyle=PRIMARY, command=self.reset_hyperparams)
        self.update_btn = ttk.Button(self.btn_group, text="Actualizar", bootstyle=SECONDARY, command=self.update_hyperparams)
        self.reset_btn.pack(side=LEFT, expand=YES, ipady=5, ipadx=15, padx=2)
        self.update_btn.pack(side=LEFT, expand=YES, ipady=5, ipadx=15, padx=2)
        self.btn_group.pack(side=BOTTOM, expand=YES, fill=BOTH, padx=100, pady=10)

    def set_hyperparams_widgets(self, hyperparams):
        for hyperparam in hyperparams.keys():
            data = hyperparams[hyperparam]
            self.start_values[hyperparam] = data["value"]

            container = ttk.Frame(self)
            label = ttk.Label(container, text=data["name"], bootstyle=PRIMARY)
            Hovertip(container, data["description"])
            min_label = ttk.Label(container, text=data["range"][0])
            max_label = ttk.Label(container, text=data["range"][1])
            current_value_str = ttk.StringVar(value=data["value"])

            if isinstance(data["value"], int):
                current_value_var = ttk.IntVar(value=data["value"])
            else:
                current_value_var = ttk.DoubleVar(value=data['value'])

            slider = ttk.Scale(
                master=container,
                orient=HORIZONTAL,
                from_=data["range"][0],
                to=data["range"][1],
                variable=current_value_var,
                command=lambda v, var=current_value_str, d=data: var.set(
                    f"{float(v):.2f}" if not isinstance(d["value"], int) else f"{v.split('.')[0]}")
            )

            current_value_label = ttk.Label(container, textvariable=current_value_str)

            container.pack(padx=10, fill=X)
            label.pack(anchor=N)
            current_value_label.pack(anchor=N)
            min_label.pack(side=LEFT)
            slider.pack(side=LEFT, fill=X, expand=YES, padx=(5, 5))
            max_label.pack(side=LEFT)
            self.values[hyperparam] = [current_value_var, current_value_str]

    def update_hyperparams(self):
        for hyperparam in self.values.keys():
            self.hyperparams[hyperparam]["value"] = self.values[hyperparam][0].get()
            print(f"{hyperparam}: {self.values[hyperparam][0].get()}")

    def reset_hyperparams(self):
        for hyperparam in self.values.keys():
            self.values[hyperparam][0].set(self.start_values[hyperparam])
            self.values[hyperparam][1].set(self.start_values[hyperparam])
        self.update_hyperparams()
