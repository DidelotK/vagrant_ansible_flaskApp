import sqlite3


class Module:

	def __init__(self):
		self.database = sqlite3.connect('helloWorldApp.db', timeout=1, check_same_thread=False)
		self.database.text_factory = bytes
		self.cursor = self.database.cursor()
		self.createTable()
		self.addModules()


	def createTable(self):
		self.cursor.execute('''DROP TABLE IF EXISTS deployed_modules''')
		self.cursor.execute('''CREATE TABLE deployed_modules
		(id INTEGER PRIMARY KEY, Nom TEXT)''')

	def addModule(self, Nom):
		self.cursor.execute('''INSERT INTO deployed_modules (Nom)
		VALUES (?)''',(Nom,))

	def addModules(self):
		modules = ['Nginx', 'SQlite', 'Supervisord', 'Gunicorn', 'Flask']
		for module in modules:
			self.addModule(module)

	def getModules(self):
		self.cursor.execute('SELECT Nom FROM deployed_modules')
		module = self.cursor.fetchall()
		return [i[0] for i in module]

	def __del__(self):
		self.cursor.close()
