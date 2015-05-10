import falcon
import json
from DocumentService import DocumentService


class Resource(object):

	def on_get(self, req, resp, identifier=None):
		"""
		Handle getting a document resource by identifier.
		:param req: the request.
		:param resp: the response.
		:param identifier: the id of the document to find.
		:return: a document, 401 on any verb but put with no id, 404 otherwise.
		"""
		if not identifier:
			raise falcon.HTTPMethodNotAllowed({'PUT'})

		service = DocumentService()
		document = service.get_document(identifier)
		if document:
			resp.body = json.dumps(document)
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
			document = json.loads(raw_json, 'utf-8')
		except ValueError:
			raise falcon.HTTPError(falcon.HTTP_753,
									'Malformed JSON',
									'Could not decode the request body. The '
									'JSON was incorrect.')
		service = DocumentService()
		key = service.create(document)

		resp.location = '/document/' + str(key)
		resp.status = falcon.HTTP_201
