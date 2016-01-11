from State import *

class FunctionState(State):

	"""
	A function state is a 'normal' state.

	:version: 2015-12-07
	:author: Kai Hartung & Lukas Block
	"""

	def __init__(self, manager, uri = None, isBlank = False, blankNodeId = None):
		"""
		 Constructor - Should never be called from outside the model framework.

		@param ModelManager manger : The parent element (if one exists).
		@param string uri :
		@param bool isBlank :
		@param string blankNodeId :
		@return  :
		@author
		"""
		State.__init__(self, manager, uri, isBlank, blankNodeId)

		self._fireChangeEvents = True
		self.fireChangeEvent()



