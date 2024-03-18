import tkinter as tk
import hyperparameters
import configure_simulation

class Simulation(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Configuración de la Simulación")
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
        problems = Problems()
        self.simulation = configure_simulation.SimulationConfigure(master=self, problems=problems)

# De donde salen los problemas?
class Problems:
    def get_problems(self):
        return ["Problema 1", "Problema 2", "Problema 3"]
    
if __name__ == "__main__":
    app = Simulation()
    app.mainloop()
