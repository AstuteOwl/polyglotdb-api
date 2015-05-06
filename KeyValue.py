import falcon
import json
from KeyValueService import KeyValueService


class Resource(object):

	def on_get(self, req, resp, key=None):
		"""
		Handle getting a key value resource by key.
		:param req: the request.
		:param resp: the response.
		:param key: the key to find.
		:return: a key value pair or 404
		"""
		if not key:
			raise falcon.HTTPMethodNotAllowed({'PUT'})

		key = KeyValueService.get_key(key=key)
		if key:
			resp.body = json.dumps(key)
			resp.status = falcon.HTTP_200
		else:
			resp.status = falcon.HTTP_404

	def on_put(self, req, resp):
		"""
		Handle when a new key value resource is posted.
		:param req: the http request object.
		:param resp: the http response object.
		:return: 201 with the location header if successful, 4xx otherwise.
		"""
		try:
			raw_json = req.stream.read()
		except Exception:
			raise falcon.HTTPError(falcon.HTTP_748,
									'Read Error',
									'Could not read the request body. Must be '
									'them ponies again.')

		try:
			key_value_pair = json.loads(raw_json, 'utf-8')
		except ValueError:
			raise falcon.HTTPError(falcon.HTTP_753,
									'Malformed JSON',
									'Could not decode the request body. The '
									'JSON was incorrect.')

		key = KeyValueService.create(key_value_pair)

		resp.location = '/kv/' + key
		resp.status = falcon.HTTP_201
