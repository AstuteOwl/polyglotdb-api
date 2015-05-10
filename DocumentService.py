
class DocumentService():
	"""
	"""

	def __init__(self):
		"""
		Create a new Document Service
		"""
		pass

	def get_document(self, identifier):
		"""
		Looks up the document by identifier and returns it.
		:param identifier: the id of the document to retrieve
		:return: the document
		"""
		return {identifier: "a document"}


	def create(self, document):
		"""
		Create a document and return the id
		:param document: the document to create.
		:return: the id of the document
		"""
		return "1234"
