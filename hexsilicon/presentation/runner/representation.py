import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class Representation(ttk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
    
    def create_widgets(self):
        self.btn_group = ttk.Frame(self)
        self.reset_btn = ttk.Button(self.btn_group, text="Algo")
        self.reset_btn.pack(side=LEFT, expand=YES, ipady=5, ipadx=15, padx=2)
        self.btn_group.pack(side=BOTTOM, expand=YES, fill=BOTH, padx=100, pady=10)
