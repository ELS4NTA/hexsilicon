import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from hexsilicon.presentation.observer import Observer


class Environment(Observer, ttk.Labelframe):



    def __init__(self, master=None) -> ttk.Frame:
        super().__init__(master)
        self.create_widgets()
        self.configure(text="Environment")

    def create_widgets(self):

        self.environment_label = ttk.Label(self, text="Environment")
        self.environment_label.pack(side=LEFT, padx=10)

        self.show_btn = ttk.Button(
            self, text="Not show", bootstyle="primary", command=self.toggle_frame)
        self.show_btn.pack()

    def toggle_frame(self):
        if self.environment_label.winfo_ismapped():
            self.environment_label.pack_forget()
            self.show_btn.config(text="Show")
        else:
            self.environment_label.pack(expand=YES, fill=BOTH)
            self.show_btn.config(text="Not show")

    def update(self, *args, **kwargs):
        pass
