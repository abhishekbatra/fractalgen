#!/usr/bin/env python

from cairorenderer import CairoRenderer
from lsystem import LSystem
from basicoperation import BasicOperation

import gtk
import math

def main():
	window = gtk.Window()
	
	oLSystem = LSystem()
	oLSystem.axiom = "F"
	oLSystem.rules["F"] = "F+F-F-F+F"
	oLSystem.operations = {
		"F" : BasicOperation("drawForward", 20),
		"+" : BasicOperation("turnACCW", (math.pi)/2),
		"-" : BasicOperation("turnCCW", (math.pi)/2)
	}
	oLSystem.setLevel(5)
	
	oRenderer = CairoRenderer(oLSystem)
	window.add(oRenderer)
	window.connect("destroy", gtk.main_quit)
	window.show_all()
	
	gtk.main()
	
if __name__ == "__main__":
	main()