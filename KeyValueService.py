class KeyValueService():
	"""
	"""

	def __init__(self):
		"""
		Create a new Key Value Pair
		"""
		pass

	@staticmethod
	def get_key(key):
		"""
		Looks up the key pair value by key and returns it.
		:param key: the key to retrieve
		:return: the key value pair
		"""
		return {"1234":"A blob o text"}

	@staticmethod
	def create(key_value_pair):
		"""
		Create a key value pair and return the key
		:param key_value_pair: the kvp to create.
		:return: the key of the key value pair
		"""
		return "1234"
