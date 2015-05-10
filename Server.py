import falcon
from wsgiref import simple_server
import KeyValue
import Document

api = application = falcon.API()

keyValue = KeyValue.Resource()
document = Document.Resource()

#KeyValue Pair
api.add_route('/kv/{key}', keyValue)
api.add_route('/kv', keyValue)

#Documents
api.add_route('/document/{identifier}', document)
api.add_route('/document', document)


if __name__ == '__main__':
	httpd = simple_server.make_server('0.0.0.0', 5000, api)
	httpd.serve_forever()
