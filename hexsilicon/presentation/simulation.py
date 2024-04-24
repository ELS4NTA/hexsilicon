import importlib
import pkgutil

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from hexsilicon.presentation.configure_simulation import SimulationConfigure
from hexsilicon.presentation.execution import Execution


class Simulation(ttk.Window):

    def __init__(self):
        super().__init__()
        self.title("Configuración de la Simulación")
        self.modules = self.load_modules("hexsilicon.swarms")
        self.modules.extend(self.load_modules("hexsilicon.problems"))
        self.configuration = None
        self.execution = None
        self.swarm = None
        self.algorithm = None
        self.problem = None
        self.context = None
        self.configure_window()
        self.create_widgets()

    def configure_window(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = int(screen_width * 0.6)
        window_height = int(screen_height * 0.6)
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.resizable(False, False)

    def create_widgets(self):
        self.configuration = SimulationConfigure(master=self)
        self.configuration.pack()

    def start_simulation(self, swarm, algorithm, problem, context):
        self.configuration.pack_forget() if self.configuration.winfo_ismapped() else None
        self.title("Ejecución de la Simulación")
        self.swarm = swarm
        self.algorithm = algorithm
        self.problem = problem
        self.context = context
        self.instance_for_execution()
        self.execution = Execution(master=self, hyperparams=self.swarm.get_hyperparams())
        self.swarm.subscribe(self.execution.history)
        self.swarm.subscribe(self.execution.graphic)
        self.swarm.subscribe(self.execution.environment)
        self.execution.pack(expand=YES, fill=BOTH)

    def load_modules(self, package):
        if isinstance(package, str):
            package = importlib.import_module(package)
        submodules = []
        for loader, module_name, is_pkg in pkgutil.walk_packages(package.__path__, package.__name__ + '.'):
            # Cargar el módulo (o submódulo)
            module = importlib.import_module(module_name)
            if is_pkg:
                # Si es un paquete, recursivamente cargar submódulos
                submodules.extend(self.load_modules(module))
            else:
                # Si no es un paquete, añadir a la lista de submódulos
                submodules.append(module)
        return submodules

    def get_descriptions(self, class_name):
        clz = self.get_class(class_name)
        descriptions = [subclass.get_description() for subclass in clz.__subclasses__()]
        return descriptions

    def get_class(self, class_name):
        clz = next((getattr(module, class_name) for module in self.modules if hasattr(module, class_name)), None)
        return clz

    def restore_configuration(self):
        self.execution.pack_forget() if self.execution.winfo_ismapped() else None
        self.title("Configuración de la Simulación")
        self.configuration.pack()

    def instance_for_execution(self):
        swarm_class = self.get_class(self.swarm)
        algorithm_class = self.get_class(self.algorithm)
        problem_class = self.get_class(self.problem)
        self.problem = problem_class(self.context)
        self.swarm = swarm_class(algorithm_class, self.problem)
        # context_class = self.get_class(self.context)
        
    def start_execution(self):
        self.swarm.generate_swarm()
        self.swarm.metaheuristic()