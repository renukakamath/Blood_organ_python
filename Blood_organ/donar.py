from flask import *
from database import *

donar=Blueprint('donar',__name__)

@donar.route('/donarhome')
def donarhome():
	return render_template("donarhome.html")

@donar.route('/donar_blood_request',methods=['get','post'])
def donar_blood_request():
	data={}
	q="select * from bloodgroup"
	res1=select(q)
	data['blood']=res1
	q="select * from receiver"
	res=select(q)
	data['rece']=res

	if 'submit' in request.form:
		receiver=request.form['receiver']
		blood=request.form['bld']
		required=request.form['required']
		q="insert into blood_request  values(null,'%s','%s','%s',now(),'pending')"%(receiver,blood,required)
		insert(q)
		return redirect(url_for('donar.donar_blood_request'))


	q="SELECT * FROM blood_request INNER JOIN receiver USING(receiver_id) INNER JOIN bloodgroup USING(group_id)"
	res1=select(q)
	data['bld']=res1

	return render_template("donar_blood_request.html",data=data)


@donar.route('/donar_organ_request',methods=['get','post'])
def donar_organ_request():
	data={}
	q="select * from organ"
	res1=select(q)
	data['orga']=res1
	q="select * from receiver"
	res=select(q)
	data['rece']=res

	if 'submit' in request.form:
		receiver=request.form['receiver']
		organ=request.form['org']
		required=request.form['required']
		q="insert into organ_request  values(null,'%s','%s','%s',now(),'pending')"%(receiver,organ,required)
		insert(q)
		return redirect(url_for('donar.donar_organ_request'))


	q="SELECT * FROM organ_request INNER JOIN receiver USING(receiver_id) INNER JOIN organ USING(organ_id)"
	res1=select(q)
	data['bld']=res1

	return render_template("donar_organ_request.html",data=data)

@donar.route('/donar_view_req_msg')
def donar_view_req_msg():
	data={}
	q="SELECT * FROM blood_req_msg INNER JOIN bloodgroup USING(group_id)"
	res=select(q)
	data['requ']=res

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None

	if action=="update":
		q="update blood_req_msg set donar_id='%s' where message_id='%s'"%(session['donar_id'],id)
		update(q)
		return redirect(url_for('donar.donar_view_req_msg'))
		
	
	return render_template("donar_view_req_msg.html",data=data)