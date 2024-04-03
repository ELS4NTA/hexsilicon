import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class Control(ttk.Labelframe):

    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()
        self.configure(text="Control")

    def create_widgets(self):
        self.back_button = ttk.Button(self, text="Back")
        self.start_button = ttk.Button(self, text="Start", command=self.master.start_execution)
        self.stop_button = ttk.Button(self, text="Stop")
        self.reset_button = ttk.Button(self, text="Reset")
        self.back_button.pack(side=LEFT, padx=10)
        self.start_button.pack(side=LEFT, padx=10)
        self.stop_button.pack(side=LEFT, padx=10)
        self.reset_button.pack(side=LEFT, padx=10)