#Login credentila Checking 
from bottle import Bottle, run, get,route, static_file, view, template,  post, request,template,redirect,response
@route ('/admin')
def uploadZipp():
	return template('login')