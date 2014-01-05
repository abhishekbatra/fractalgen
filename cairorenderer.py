from abstractrenderer import AbstractRenderer
import gtk
from lsystem import LSystem
import math

class Color:
	def __init__(self):
		self.r = 0
		self.g = 0
		self.b = 0
		self.a = 0
		
class CairoRenderer(gtk.DrawingArea):
	
	def __init__(self, oLSystem):
		gtk.DrawingArea.__init__(self)
		self.connect("expose_event", self.expose)
		self.oLSystem = oLSystem
		self.color = Color()
		self.line_width = 0
		self.direction = 0
		self.current_point = 0, 0
	
	def expose(self, widget, event):
		self.context = widget.window.cairo_create()
		self.context.rectangle(event.area.x, event.area.y, event.area.width, event.area.height)
		self.context.clip()
		self.draw(self.context)
		
		return False
	
	def draw(self, context):
		
		rect = self.get_allocation()
		
		screen = self.get_screen()
		screen_width, screen_height = screen.get_width(), screen.get_height()
		print "screen_width, screen_height ", screen_width, screen_height
		current_width, current_height = self.get_size_request()
		print "rect.width, rect.height", rect.width, rect.height
		
		self.context.scale(200/screen_width, 200/screen_width)
		
		self.context.move_to(rect.x+50, rect.y+50)
		self.current_point = rect.x+50, rect.y+50
		context.set_source_rgb(1, 1, 1)
		context.fill_preserve()
		context.set_source_rgb(0, 0, 0)
		self.oLSystem.draw(context, self)
		
	def drawForward(self, context, length):
		self.context.move_to(*(self.current_point))
		final_point = self.current_point[0] + length * math.cos(self.direction), self.current_point[1] + length * math.sin(self.direction)
		self.current_point = final_point
		context.line_to(*final_point)
		context.stroke()

	def moveForward(self, context, length):
		final_point = self.current_point[0] + length * math.cos(self.direction), self.current_point[1] + length * math.sin(self.direction)
		self.current_point = final_point
		
	def turnCCW(self, context, radians):
		self.direction -= radians
		
	def turnACCW(self, context, radians):
		self.direction += radians
	
	def setLineWidth(self, pixels):
		self.line_width = pixels 
	
	def setColor(self, context, r, g, b, a):
		self.color.r = r
		self.color.g = g
		self.color.b = b
		self.color.a = a
		
	def shift_origin(point, new_origin):
		point.x += new_origin.x
		point.y += new_origin.y
		
		return point
	
AbstractRenderer.register(CairoRenderer)