import py2neo

py2neo.Graph('bolt://neo4j:neo4j@localhost:7687').delete_all()
