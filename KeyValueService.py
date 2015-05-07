import redis
import Settings
from KeyValuePair import KeyValuePair

class KeyValueService():
	"""
	"""

	def __init__(self):
		"""
		Create a new Key Value Pair
		"""
		self.redis_server = redis.StrictRedis(host=Settings.redis_server, port=Settings.redis_port, db=Settings.redis_db)

	def get_key(self, key):
		"""
		Looks up the key pair value by key and returns it.
		:param key: the key to retrieve
		:return: the key value pair
		"""
		value = self.redis_server.get(key)
		if not value:
			return None

		return KeyValuePair(key, value)


	def create(self, key_value_pair):
		"""
		Create a key value pair and return the key
		:param key_value_pair: the kvp to create.
		:return: the key of the key value pair
		"""
		self.redis_server.set(key_value_pair.key, key_value_pair.value)
		return key_value_pair.key
