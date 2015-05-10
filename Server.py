import falcon
from wsgiref import simple_server
import KeyValue

api = application = falcon.API()

keyValue = KeyValue.Resource()

api.add_route('/kv/{key}', keyValue)
api.add_route('/kv', keyValue)

if __name__ == '__main__':
	httpd = simple_server.make_server('0.0.0.0', 5000, api)
	httpd.serve_forever()
