from hexsilicon.presentation.simulation import Simulation


class Hexsilicon(object):

    def __init__(self):
        app = Simulation()
        app.mainloop()


if __name__ == "__main__":
    hexsilicon = Hexsilicon()
