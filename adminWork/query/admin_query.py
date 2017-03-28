import os
import sys
import uuid
import json
import datetime
import psycopg2.extras
import psycopg2
class admin_querys:
   def __init__ (self, dbname = 'martu9',user= "martu9" ,password= "martu9.123" ,host="localhost",port=5432):
      self.dbconn = psycopg2.connect(dbname=dbname,user=user ,password=password ,host=host,port=port)
      self.cur =  self.dbconn.cursor(cursor_factory=psycopg2.extras.DictCursor)
      psycopg2.extras.register_uuid()
	#add this part of code When required 
	#Log in auth check 
	#@param1 : userNmae
	#@param2 : passWord
	#return : True / False
	#def adimAuth(self,user,passWord):
	#   pass
   def adminAuth(self,userNmae,passWord):
	 userNmae = userNmae
	 passWord = passWord
	 data = {'userNmae':userNmae,'passWord':passWord}
	 select_stmt = "SELECT * FROM {} WHERE username = %(userNmae)s and password = %(passWord)s ".format('adminLogin')
	 self.cur.execute(select_stmt, data)
   	 result = self.cur.fetchone()
   	 #print "result:",result
   	 return result

   def addProduct(self,category,filename):
	 data = [filename,category] 
	 sql = ("INSERT INTO productList (product_id,category) ""VALUES (%s, %s)")
	 result = self.cur.execute(sql,data)
	 self.dbconn.commit()
   
   def changepswd(self,newPswd,oldPswd):
     data = {'newPswd':newPswd,'oldPswd':oldPswd}
     select_stmt = "select * from {} where password = %(oldPswd)s".format('adminLogin')
     self.cur.execute(select_stmt,data)
     result = self.cur.fetchone()
     print 'res',result
     if result == None:
     	return False
     print 'myresult',result
     sql = "UPDATE {} set password = %(newPswd)s where password = %(oldPswd)s".format('adminLogin')
     result = self.cur.execute(sql,data)
     result = self.dbconn.commit()
     #print 'result:::::::::::::',result
     return True
