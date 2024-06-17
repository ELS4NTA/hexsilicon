from hexsilicon.presentation.simulation import Simulation


class Hexsilicon:
    """
    A class to encapsulate the Hexsilicon application.

    This class initializes the Hexsilicon application by creating an instance
    of the Simulation class from the hexsilicon.presentation.simulation module
    and then enters the main application loop by calling the mainloop method
    on the Simulation instance.
    """

    def __init__(self):
        app = Simulation()
        app.mainloop()


if __name__ == "__main__":
    hexsilicon = Hexsilicon()
