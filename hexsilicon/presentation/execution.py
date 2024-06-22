import time

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.toast import ToastNotification

from hexsilicon.presentation.runner.evironment import Environment
from hexsilicon.presentation.runner.graphic import Graphic
from hexsilicon.presentation.runner.history import History
from hexsilicon.presentation.runner.hyperparameters import Hyperparameters
from hexsilicon.presentation.runner.representation import Representation


class Execution(ttk.Frame):

    def __init__(self, master=None, hyperparams=None, visualization=None):
        super().__init__(master)
        self.hyperparams = hyperparams
        self.visualization = visualization
        self.widget_frames = []
        self.create_widgets()

    def create_widgets(self):
        self.columnconfigure(0, weight=4)
        self.columnconfigure(1, weight=1)
        self.create_control_buttons()
        self.create_dashboard()
        self.create_environment()

    def create_control_buttons(self):
        self.control_frame = ttk.Labelframe(self, text="Control")
        self.back_button = ttk.Button(self.control_frame, text="Atras", command=self.return_to_config)
        self.start_button = ttk.Button(self.control_frame, text="Iniciar", command=self.start_execution)
        self.stop_button = ttk.Button(self.control_frame, text="Detener", command=self.stop_execution)
        self.reset_button = ttk.Button(self.control_frame, text="Reiniciar", command=self.reset_execution)
        self.back_button.pack(side=LEFT, padx=10)
        self.start_button.pack(side=LEFT, padx=10)
        self.stop_button.pack(side=LEFT, padx=10)
        self.reset_button.pack(side=LEFT, padx=10)
        self.control_frame.grid(column=0, row=0, sticky=EW, pady=10, padx=10, ipady=10, ipadx=10)
        self.widget_frames.append(self.control_frame)

    def create_dashboard(self):
        self.dashboard_notebook = ttk.Notebook(self, bootstyle="primary")
        self.create_information()
        self.hyper_frame = Hyperparameters(self.dashboard_notebook, self.hyperparams, self.gauge)
        self.representation = Representation(self.dashboard_notebook, self.gauge)
        self.info_frame.pack(fill=BOTH, expand=YES)
        self.hyper_frame.pack(fill=BOTH, expand=YES)
        self.representation.pack(fill=BOTH, expand=YES)
        self.dashboard_notebook.add(self.info_frame, text='Información')
        self.dashboard_notebook.add(self.hyper_frame, text='Hiperparametros')
        self.dashboard_notebook.add(self.representation, text='Representación')
        self.dashboard_notebook.grid(column=1, row=0, rowspan=2, sticky=NS, pady=10, padx=10)
        self.widget_frames.append(self.dashboard_notebook)

    def create_information(self):
        self.info_frame = ttk.Frame(self.dashboard_notebook)
        sf = ScrolledFrame(self.info_frame)
        sf.pack(fill=BOTH, expand=YES)
        self.values_frame = ttk.Labelframe(sf, text="Valores")
        self.history_frame = ttk.Labelframe(sf, text="Historial")
        self.graphic_frame = ttk.Labelframe(sf, text="Gráfica")
        self.gauge = ttk.Floodgauge(self.values_frame, bootstyle=PRIMARY, length=100, mask='Iteración {}', )
        self.objective = ttk.Label(self.values_frame, bootstyle="inverse-primary", text=self.master.objective(), anchor=CENTER)
        self.func_val = ttk.Label(self.values_frame, bootstyle="inverse-primary", text="Fun", anchor=CENTER)
        self.history = History(self.history_frame, self.func_val)
        self.graphic = Graphic(self.graphic_frame, self.visualization)
        self.values_frame.pack(side=TOP, fill=BOTH, expand=YES, padx=10)
        self.objective.pack(side=LEFT, ipadx=10, ipady=15, padx=10)
        self.func_val.pack(side=LEFT, ipadx=10, ipady=15, padx=10)
        self.gauge.pack(side=LEFT, fill=X, expand=YES, padx=10)
        self.history.pack(side=TOP)
        self.graphic.pack(side=TOP)
        self.values_frame.pack(side=TOP, fill=BOTH, expand=YES, padx=10)
        self.history_frame.pack(side=TOP, expand=YES, fill=BOTH, padx=10)
        self.graphic_frame.pack(side=TOP, expand=YES, fill=BOTH, padx=10)

    def create_environment(self):
        self.environment = Environment(self)
        self.environment.grid(column=0, row=1, sticky=NSEW, pady=10, padx=10)
        self.widget_frames.append(self.environment)

    def return_to_config(self):
        self.master.stop_execution()
        self.master.restore_configuration()

    def start_execution(self):
        self.start_button.configure(state="disabled")
        self.master.start_execution()

    def stop_execution(self):
        ToastNotification(title="Información", message="Ejecución del algoritmo detenida", duration=3000).show_toast()
        self.master.stop_execution()
        self.stop_button.configure(text="Continuar", command=self.resume_execution)

    def resume_execution(self):
        ToastNotification(title="Información", message="Continuando ejecución del algoritmo", duration=3000).show_toast()
        self.master.resume_execution()
        self.stop_button.configure(text="Detener", command=self.stop_execution)

    def reset_execution(self):
        self.master.stop_execution()
        self.master.start_simulation()
