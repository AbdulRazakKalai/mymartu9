from bottle import Bottle, run, get,route, static_file, view, template,  post, request,template,redirect,response
from query.admin_query import *
from login import *
import os,csv,xlrd

#Route File ,linked in all other python Files

#admin Route for admin level
@route('/adminindex')
#@route('/hello/<name>')
def adminindex():
    return template('index')
########################################################################################
#Validating the usename and pasword
@route ('/validateLogin',method="POST")
def validateLogin():
	userName = request.forms.userName;
	passWord = request.forms.passWord;
	admin_query = admin_querys();
	res = admin_query.adminAuth(userName,passWord)
	if (res):
		return ("True")
	else:
		return ("False")

#######################################################################################
  #@route : upload zipp  
  #@param1 : file 
  #@param2  : category
  #@response : True / False (sucess / failur)

@route ('/uploadZippImage', method="POST")
def uplodZippImage():
  category = request.forms.get('category')
  upload = request.files.get('files')
  print 'category',category,upload
  name ,ext = os.path.splitext(upload.filename)
  save_to_path = os.getcwd() +"/"+"tmp/{category}".format(category=category)
  print 'save_to_path:',save_to_path
  if not os.path.exists(save_to_path):
      os.makedirs(save_to_path)
  file_path = "{path}/{file}".format(path=save_to_path, file=upload.filename)
  print 'file_path:',file_path
  if(os.path.exists(file_path)):
    return 'False'
  else:
    upload.save(file_path)
    admin_query = admin_querys();
    res = admin_query.addProduct(category,upload.filename)
    return 'True'

####################################
  #@route : changePassword  
  #@param1 : oldPassword
  #@param2  : newPassword
  #@response : True / False (sucess / failur)
@route ('/changePassword', method="POST")
def changePassword ():
  print 'calling post'
  oldPassword = request.forms.oldPassword
  newPassword = request.forms.newPassword
  #print 'res',oldPassword,newPassword
  admin_query = admin_querys();
  res = admin_query.changepswd(oldPassword,newPassword)
  print 'the res',res
  if res:
    return 'True'
  else:
    return 'False'
#######################################################################################
  #@route : uploadDataFile 
  #@param1 : file
  #@response : True / False (sucess / failur)
@route ('/uploadDataFile', method="POST")
def uploadDataFile ():
  print 'uploading data file'
  upload = request.files.get('files')
  name ,ext = os.path.splitext(upload.filename)
  save_to_path = os.getcwd() +os.path.sep+"tmp"
  file_path = "{path}/{file}".format(path=save_to_path, file=upload.filename)
  upload.save(file_path)
  book = xlrd.open_workbook(file_path)
  first_sheet = book.sheet_by_index(0)
  #print first_sheet.row_values(0)
  cell = first_sheet.cell(0,0)
  print cell
  print cell.value
  
  


#######################################################################################
@route ('/signup.html')
def uploadZipp():
	return template('signup')	
#index route for user Level
@route('/')
#@route('/hello/<name>')
def hello():
	return template('userindex')

@route ('/uploadzip.html')
def uploadZipp():
	return template('uploadzip')


@route ('/uploaddata.html')
def uploadZipp():
	return template('uploaddata')


@route ('/edit.html')
def uploadZipp():
	return template('edit')


@route ('/delete.html')
def uploadZipp():
	return template('delete')


@route ('/view-details.html')
def uploadZipp():
	return template('view-details')


@route ('/changepswd.html')
def uploadZipp():
	return template('changepswd.html')

	
	
#manging route
@get("/static/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="static")
@get("/fonts/<filepath:re:.*\.(eot|otf|svg|ttf|woff|woff2?)>")
def font(filepath):
    return static_file(filepath, root="fonts")

@get("/images/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root="images")

@get("/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="js")
@get("/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="js")


run(host='localhost', port=8080, debug=True)



