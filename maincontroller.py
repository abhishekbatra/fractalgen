from lsystem import LSystem
import pygtk
import gtk

class FracGenController:
    def __init__(self, renderer):
        self.lsys = LSystem()