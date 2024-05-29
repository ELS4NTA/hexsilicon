import ttkbootstrap as ttk
from ttkbootstrap.constants import *

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
        self.control_frame.grid(column=0, row=0, sticky=NW)
        self.widget_frames.append(self.control_frame)

    def create_dashboard(self):
        self.dashboard_notebook = ttk.Notebook(self, bootstyle="primary")
        self.create_information()
        self.hyper_frame = Hyperparameters(self.dashboard_notebook, self.hyperparams)
        self.representation = Representation(self.dashboard_notebook)
        self.info_frame.pack(fill=BOTH, expand=YES)
        self.hyper_frame.pack(fill=BOTH, expand=YES)
        self.representation.pack(fill=BOTH, expand=YES)
        self.dashboard_notebook.add(self.info_frame, text='Información')
        self.dashboard_notebook.add(self.hyper_frame, text='Hiperparametros')
        self.dashboard_notebook.add(self.representation, text='Representación')
        self.dashboard_notebook.grid(column=1, row=0, rowspan=2, sticky=E)
        self.widget_frames.append(self.dashboard_notebook)

    def create_information(self):
        self.info_frame = ttk.Frame(self.dashboard_notebook)
        self.history_frame = ttk.Labelframe(self.info_frame, text="Historial")
        self.graphic_frame = ttk.Labelframe(self.info_frame, text="Gráfica")
        self.history = History(self.history_frame)
        self.graphic = Graphic(self.graphic_frame, self.visualization)
        self.history.pack(side=TOP)
        self.graphic.pack(side=TOP)
        self.history_frame.pack(side=TOP, expand=YES, fill=BOTH, padx=100)
        self.graphic_frame.pack(side=TOP, expand=YES, fill=BOTH, padx=100)

    def create_environment(self):
        self.environment = Environment(self)
        self.environment.grid(column=0, row=1, sticky=N)
        self.widget_frames.append(self.environment)

    def return_to_config(self):
        self.master.restore_configuration()

    def start_execution(self):
        self.master.start_execution()

    def stop_execution(self):
        pass

    def reset_execution(self):
        for frame in self.widget_frames:
            frame.destroy()
        self.create_widgets()
