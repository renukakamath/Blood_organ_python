from flask import *
from database import *

public=Blueprint('public',__name__)

@public.route('/')
def publichome():
	return render_template("publichome.html")

@public.route('/login',methods=['get','post'])
def login():
	if 'submit' in request.form:
		uname=request.form['username']
		pas=request.form['password']
		q="select * from login where username='%s' and password='%s'"%(uname,pas)
		res=select(q)
		print(q)
		if res:
			session['login_id']=res[0]['login_id']
			if res[0]['usertype']=="admin":
				return redirect(url_for('admin.adminhome'))
			elif res[0]['usertype']=="donar":
				q="select * from donar where login_id='%s'"%(session['login_id'])
				res=select(q)
				if res:
					session['donar_id']=res[0]['donar_id']
				return redirect(url_for('donar.donarhome'))

			elif res[0]['usertype']=="organization":

				q="select * from organization where login_id='%s'"%(session['login_id'])
				print(q)
				res1=select(q)
				if res1:
					session['organization_id']=res1[0]['organization_id']
					print(session['organization_id'])

				return redirect(url_for('organization.organizationhome'))

			elif res[0]['usertype']=="receiver":
				q="select * from receiver where login_id='%s'"%(session['login_id'])
				res=select(q)
				if res:
					session['receiver_id']=res[0]['receiver_id']
				return redirect(url_for('receiver.receiverhome'))

	return render_template("login.html")


@public.route('/organization',methods=['get','post'])
def organization():
	if 'submit' in request.form:
		name=request.form['name']
		place=request.form['place']
		pincode=request.form['pincode']
		phone=request.form['phone']
		email=request.form['email']
		license=request.form['license']		
		uname=request.form['username']
		pas=request.form['password']
		q="insert into login values(null,'%s','%s','organization')"%(uname,pas)
		id=insert(q)
		q="insert into organization values(null,'%s','%s','%s','%s','%s','%s','%s')"%(id,name,place,pincode,phone,email,license)
		insert(q)
		print(q)
		return redirect(url_for('public.login'))
		print(name,place,pincode,phone,email,license,uname,pas)

	return render_template("organization_reg.html")


@public.route('/donar_reg',methods=['get','post'])
def donar_reg():
	data={}
	q="select * from bloodgroup"
	res=select(q)
	data['type']=res

	if 'submit' in request.form:
		group=request.form['group']
		fname=request.form['fname']
		lname=request.form['lname']
		gender=request.form['gen']
		age=request.form['age']
		pincode=request.form['pincode']
		phone=request.form['phone']
		email=request.form['email']	
		uname=request.form['username']
		pas=request.form['password']
		q="insert into login values(null,'%s','%s','donar')"%(uname,pas)
		id=insert(q)
		q="insert into donar values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(id,group,fname,lname,gender,age,pincode,phone,email)
		insert(q)
		print(q)
		return redirect(url_for('public.login'))
		print(group,fname,lname,gender,age,pincode,phone,email,uname,pas)

	return render_template("donar_reg.html",data=data)



@public.route('/receiver_reg',methods=['get','post'])
def receiver_reg():

	if 'submit' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		house=request.form['house']
		place=request.form['place']
		pincode=request.form['pincode']
		phone=request.form['phone']
		email=request.form['email']	
		uname=request.form['username']
		pas=request.form['password']
		q="insert into login values(null,'%s','%s','receiver')"%(uname,pas)
		id=insert(q)
		q="insert into receiver values(null,'%s','%s','%s','%s','%s','%s','%s','%s')"%(id,fname,lname,house,place,pincode,phone,email)
		insert(q)
		print(q)
		return redirect(url_for('public.login'))
		print(fname,lname,house,place,pincode,phone,email,uname,pas)

	return render_template("receiver_reg.html")

