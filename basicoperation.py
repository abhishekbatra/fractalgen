from abstractrenderer import AbstractRenderer

class BasicOperation:
	def __init__(self, name, values):
		self.name = name
		self.values = values

gBasicOperations = {
	"drawForward" 	: AbstractRenderer.drawForward,
	"moveForward" 	: AbstractRenderer.moveForward,
	"turnCCW"		: AbstractRenderer.turnCCW,
	"turnACCW"		: AbstractRenderer.turnACCW,
	"setLineWidth"	: AbstractRenderer.setLineWidth,
	"setColor"		: AbstractRenderer.setColor
}