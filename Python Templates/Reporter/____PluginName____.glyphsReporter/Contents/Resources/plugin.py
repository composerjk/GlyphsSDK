# encoding: utf-8
from __future__ import division, print_function, unicode_literals

###########################################################################################################
#
#
#	Reporter Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Reporter
#
#
###########################################################################################################

import objc
from GlyphsApp import *
from GlyphsApp.plugins import *

class ____PluginClassName____(ReporterPlugin):

	@objc.python_method
	def settings(self):
		self.menuName = Glyphs.localize({
			'en': 'My Plugin',
			'de': 'Mein Plugin',
			'fr': 'Ma extension',
			'es': 'Mi plugin',
			'pt': 'Meu plug-in',
			})
		self.generalContextMenus = [{
			'name': Glyphs.localize({
				'en': 'Do something',
				'de': 'Tu etwas',
				'fr': 'Faire quelque chose',
				'es': 'Hacer algo',
				'pt': 'Faça alguma coisa',
				}), 
			'action': self.doSomething_
			}]

	@objc.python_method
	def foreground(self, layer):
		NSColor.blueColor().set()
		NSBezierPath.fillRect_(layer.bounds)
		self.drawTextAtPoint(layer.parent.name, NSPoint(0, 0))

	@objc.python_method
	def inactiveLayer(self, layer):
		NSColor.redColor().set()
		if layer.paths:
			layer.bezierPath.fill()
		if layer.components:
			for component in layer.components:
				component.bezierPath.fill()

	@objc.python_method
	def preview(self, layer):
		NSColor.blueColor().set()
		if layer.paths:
			layer.bezierPath.fill()
		if layer.components:
			for component in layer.components:
				component.bezierPath.fill()
	
	def doSomething_(self, sender):
		print('Just did something')

	@objc.python_method
	def conditionalContextMenus(self):

		# Empty list of context menu items
		contextMenus = []

		# Execute only if layers are actually selected
		if Glyphs.font.selectedLayers:
			layer = Glyphs.font.selectedLayers[0]
			
			# Exactly one object is selected and it’s an anchor
			if len(layer.selection) == 1 and type(layer.selection[0]) == GSAnchor:
					
				# Add context menu item
				contextMenus.append({
					'name': Glyphs.localize({
						'en': 'Do something else',
						'de': 'Tu etwas anderes',
						'fr': 'Faire aute chose',
						'es': 'Hacer algo más',
						'pt': 'Faça outra coisa',
						}), 
					'action': self.doSomethingElse_
					})

		# Return list of context menu items
		return contextMenus

	def doSomethingElse_(self, sender):
		print('Just did something else')

	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
