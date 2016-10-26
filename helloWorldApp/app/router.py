from flask import render_template
from app.model import Module

def router(app):
	#Routes
	@app.route('/')
	def home():
			module = Module()
			modules = module.getModules();
	 		return render_template('home.html',modules = modules)

	# Sample HTTP error handling
	@app.errorhandler(404)
	def not_found(error):
		return render_template('404.html'), 404

