import importlib
import pkgutil
from threading import Thread

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from hexsilicon.presentation.configuration import Configuration
from hexsilicon.presentation.execution import Execution


class Simulation(ttk.Window):

    def __init__(self):
        super().__init__()
        self.modules = self.load_modules("hexsilicon.swarms")
        self.modules.extend(self.load_modules("hexsilicon.problems"))
        self.modules.extend(self.load_modules("hexsilicon.presentation.visualization"))
        self.configuration = None
        self.execution = None
        self.swarm = None
        self.algorithm = None
        self.problem = None
        self.swarm_class = None
        self.algorithm_class = None
        self.problem_class = None

        self.swarm_thread = None
        self.execution_thread = None
        self.configure_window()
        self.create_widgets()

    def configure_window(self):
        self.title("Hexsilicon")
        self.resizable(True, True)
        self.state("zoomed")
        self.iconbitmap("icons/icon.ico")
        self.iconbitmap(default="icons/icon.ico")

    def create_widgets(self):
        self.configuration = Configuration(master=self)
        self.configuration.pack()

    def start_simulation(self, swarm="", algorithm="", problem="", context=""):
        self.configuration.pack_forget() if self.configuration.winfo_ismapped() else None
        self.execution.destroy() if self.execution else None
        self.instance_for_execution(swarm, algorithm, problem, context)
        self.execution = Execution(master=self, hyperparams=self.swarm.get_hyperparams(), visualization=self.get_class(self.swarm.problem.get_description()['class_visualization']))
        self.swarm.subscribe(self.execution.history)
        self.swarm.subscribe(self.execution.graphic)
        self.swarm.subscribe(self.execution.environment)
        self.swarm.subscribe(self.execution.representation)
        self.execution.pack(expand=YES, fill=BOTH)

    def load_modules(self, package):
        if isinstance(package, str):
            package = importlib.import_module(package)
        submodules = []
        for loader, module_name, is_pkg in pkgutil.walk_packages(package.__path__, package.__name__ + '.'):
            # Load the module
            module = importlib.import_module(module_name)
            if is_pkg:  # If module is a package, load its submodules
                submodules.extend(self.load_modules(module))
            else:  # If not a package, add the module to the list
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
        self.configuration.pack()

    def instance_for_execution(self, swarm, algorithm, problem, context):
        if swarm or algorithm or problem:
            self.swarm_class = self.get_class(swarm)
            self.algorithm_class = self.get_class(algorithm)
            self.problem_class = self.get_class(problem)
            self.problem = self.problem_class(context)
        del self.swarm
        self.swarm = self.swarm_class(self.algorithm_class, self.problem)

    def start_execution(self):
        self.swarm.generate_swarm()
        self.swarm_thread = Thread(target=self.swarm.metaheuristic, daemon=True)
        self.swarm_thread.start()

    def stop_execution(self):
        self.swarm_thread.stop()

    def objective(self):
        return "Minimizar" if self.swarm.problem.is_minimization() else "Maximizar"
