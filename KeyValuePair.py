class KeyValuePair():
	"""
	"""

	def __init__(self, key, value):
		"""
		"""
		self.key = key
		self.value = value

	def to_dict(self):
		d = {self.key: self.value }
		return d
