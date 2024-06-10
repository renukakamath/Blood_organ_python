from flask import *
from database import *

organization=Blueprint('organization',__name__)

@organization.route('/organizationhome')
def organizationhome():
	return render_template("organizationhome.html")

@organization.route('/org_view_blood')
def org_view_blood():
	data={}
	q="select * from bloodgroup"
	res=select(q)
	data['blood']=res
	return render_template("org_view_blood.html",data=data)

@organization.route('/org_view_organ')
def org_view_organ():
	data={}
	q="select * from organ"
	res=select(q)
	data['organ']=res
	return render_template("org_view_organ.html",data=data)

@organization.route('/org_view_donar')
def org_view_donar():
	data={}
	q="select * from donar"
	res=select(q)
	data['donar']=res
	return render_template("org_view_donar.html",data=data)

@organization.route('/org_organ_request')
def org_organ_request():
	id=request.args['id']
	data={}
	q="SELECT * FROM organ_request INNER JOIN receiver USING(receiver_id) INNER JOIN organ USING(organ_id) INNER JOIN donar ON organ.organ_id=donar.donar_id where donar_id='%s'"%(id)
	res1=select(q)
	data['bld']=res1

	return render_template("org_organ_request.html",data=data)


@organization.route('/org_blood_request')
def org_blood_request():
	id=request.args['id']
	data={}
	q="SELECT * FROM blood_request INNER JOIN receiver USING(receiver_id) INNER JOIN bloodgroup USING(group_id) INNER JOIN donar USING (group_id) where donar_id='%s'"%(id)
	res1=select(q)
	data['bld']=res1

	return render_template("org_blood_request.html",data=data)

@organization.route('/org_blood_req_msg',methods=['get','post'])
def org_blood_req_msg():
	data={}
	q="select * from bloodgroup"
	res=select(q)
	data['blood']=res

	if 'submit' in request.form:
	
		group=request.form['bld']
		unit=request.form['unit']
		desc=request.form['desc']
		q="insert into blood_req_msg values(null,0,'%s','%s','%s')"%(group,unit,desc)
		insert(q)
		return redirect(url_for('organization.org_blood_req_msg'))


	q="SELECT * FROM blood_req_msg INNER JOIN bloodgroup USING(group_id)"
	res=select(q)
	data['requ']=res

	return render_template("org_blood_req_msg.html",data=data)

@organization.route('/org_view_blood_req')
def org_view_blood_req():
	data={}
	q="select * from blood_request inner join bloodgroup using(group_id)"
	res=select(q)
	data['bld']=res

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']

	else:
		action=None

	if action=='update':
		q="update blood_request set status='accept' where request_id='%s'"%(id)
		update(q)
		return redirect(url_for('organization.org_view_blood_req'))

	if action=='delete':
		q="delete * from blood_request where request_id='%s'"%(id)
		delete(q)
		return redirect(url_for('organization.org_view_blood_req'))
		
	return render_template("org_view_blood_req.html",data=data)

@organization.route('/org_view_receiver')
def org_view_receiver():
	id=request.args['id']
	data={}
	q="select * from receiver where receiver_id='%s'"%(id)
	res=select(q)
	data['receiver']=res
	return render_template("org_view_receiver.html",data=data)

# @organization.route('/org_send',methods=['get','post'])
# def org_send():
# 	if 'submit' in request.form:
# 		re=request.form['replay']
# 		q="update blood_request set status='%s' where request_id='%s'"%(re,id)
# 		update(q)
# 	return render_template("org_send.html")

@organization.route('/org_view_organ_request')
def org_view_organ_request():
	data={}
	q="select * from organ_request inner join organ using(organ_id)"
	res=select(q)
	data['bld']=res

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']

	else:
		action=None

	if action=='update':
		q="update organ_request set status='accept' where organ_request_id='%s'"%(id)
		update(q)
		return redirect(url_for('organization.org_view_organ_request'))

	if action=='delete':
		q="delete * from organ_request where organ_request_id='%s'"%(id)
		delete(q)
		return redirect(url_for('organization.org_view_organ_request'))

	return render_template("org_view_organ_request.html",data=data)
