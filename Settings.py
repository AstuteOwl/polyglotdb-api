# Redis Server Configs
redis_server = 'polyglotdbdocker_redis_1'
redis_port = 6379
redis_db = 0

#CounchDb Server Configs
couchdb_server = 'polyglotdbdocker_couchdb_1'
couchdb_port = 5984
couchdb_connection = 'http://{}:{}'.format(couchdb_server, couchdb_port)
couchdb_database = 'nodonkeys'
