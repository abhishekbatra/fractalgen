from abc import ABCMeta, abstractmethod

class AbstractRenderer:
    __metaclass__ = ABCMeta

    @abstractmethod
    def drawForward(self, context, length):
        return NotImplemented

    @abstractmethod
    def moveForward(self, context, length):
        return NotImplemented

    @abstractmethod
    def turnCCW(self,context, radians):
        return NotImplemented

    @abstractmethod
    def turnACCW(self, context, radians):
        return NotImplemented

    @abstractmethod
    def setLineWidth(self, pixels):
        return NotImplemented

    @abstractmethod
    def setColor(self, r, g, b, a):
        return NotImplemented

	@abstractmethod
	def setMoveLength(self, length):
		return NotImplemented