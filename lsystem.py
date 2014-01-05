#!/usr/bin/env python

from basicoperation import gBasicOperations, BasicOperation
from abstractrenderer import AbstractRenderer

class LSystem:
	def __init__(self):
		self.operations = {}
		self.axiom = None
		self.rules = {}
		self.levels = []
	
	def getNextOperationSequence(self, sequence):
		next_sequence = str()
		for symbol in sequence:
			try:
				replacement_string = self.rules[symbol]
			except KeyError:
				replacement_string = symbol
			finally:
				next_sequence += replacement_string
		return next_sequence
			
	def draw(self, context, renderer):
		for sequence in self.levels:
			self.drawSequence(context, renderer, sequence)
	
	def drawSequence(self, context, renderer, sequence):
		for symbol in sequence:
			operation = self.operations[symbol]
			operationMethod = gBasicOperations[operation.name]
			(getattr(renderer, operation.name))(context, operation.values)
			
	def setLevel(self, number):
		seq = self.axiom
		if seq is not None:
			self.levels.append(seq)
		for i in range(1, number):
			seq = self.getNextOperationSequence(seq)
			if seq is not None:
				self.levels.append(seq)
		

import unittest

class TestLSystem(unittest.TestCase):
	"""
	A
	AB
	ABBA
	ABBABAAB
	ABBABAABBAABABBA
	ABBABAABBAABABBABAABABBAABBABAAB
	ABBABAABBAABABBABAABABBAABBABAABBAABABBAABBABAABABBABAABBAABABBA
	"""
	def test_levelgen(self):
		lsys = LSystem()
		lsys.axiom = "A"
		lsys.rules["A"] = "AB"
		lsys.rules["B"] = "BA"
		lsys.operations = {
			"A" : BasicOperation("drawForward", 5),
			"B" : BasicOperation("moveForward", 5)
		}
		lsys.setLevel(7)
		self.assertEqual(lsys.levels[6], "ABBABAABBAABABBABAABABBAABBABAABBAABABBAABBABAABABBABAABBAABABBA")

#unittest.main()