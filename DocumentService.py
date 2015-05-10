import couchdb
import Settings
import uuid
from couchdb.http import ResourceNotFound

class DocumentService():
	"""
	"""

	def __init__(self):
		"""
		Create a new Document Service
		"""
		self.server = couchdb.Server(url=Settings.couchdb_connection, full_commit=True,)
		try:
			self.database = self.server[Settings.couchdb_database]
		except ResourceNotFound:
			self.database = self.server.create(Settings.couchdb_database)

	def get_document(self, identifier):
		"""
		Looks up the document by identifier and returns it.
		:param identifier: the id of the document to retrieve
		:return: the document
		"""
		document = self.database.get(id=identifier, default=None)
		return document


	def create(self, document):
		"""
		Create a document and return the id
		:param document: the document to create.
		:return: the id of the document
		"""
		id = uuid.uuid4()
		document['_id'] = str(id)
		self.database.save(document)

		return id
