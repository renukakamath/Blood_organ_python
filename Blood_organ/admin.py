from flask import *
from database import *

admin=Blueprint('admin',__name__)

@admin.route('/adminhome')
def adminhome():
	return render_template("adminhome.html")

@admin.route('/admin_manage_blood',methods=['get','post'])
def admin_manage_blood():
	data={}
	q="select * from bloodgroup"
	res=select(q)
	data['group']=res

	if 'submit' in request.form:
		group=request.form['group']
		desc=request.form['desc']
		q="insert into bloodgroup values(null,'%s','%s')"%(group,desc)
		insert(q)

		return redirect(url_for('admin.admin_manage_blood'))

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']

	else:
		action=None

	if action=="update":
		q="select * from bloodgroup where group_id='%s'"%(id)
		res=select(q)
		data['up']=res

	if 'update' in request.form:
		group=request.form['group']
		desc=request.form['desc']
		q="update bloodgroup set group_name='%s',group_description='%s' where group_id='%s'"%(group,desc,id)
		update(q)
		return redirect(url_for('admin.admin_manage_blood'))

	return render_template("admin_manage_blood.html",data=data)

@admin.route('/admin_manage_organ',methods=['get','post'])
def admin_manage_organ():
	data={}
	q="select * from organ"
	res=select(q)
	data['organ']=res

	if 'submit' in request.form:
		organ=request.form['organ']
		detail=request.form['detail']
		q="insert into organ values(null,'%s','%s')"%(organ,detail)
		insert(q)

		return redirect(url_for('admin.admin_manage_organ'))

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']

	else:
		action=None

	if action=="update":
		q="select * from organ where organ_id='%s'"%(id)
		res=select(q)
		data['up']=res

	if 'update' in request.form:
		organ=request.form['organ']
		detail=request.form['detail']
		q="update organ set organ_name='%s',organ_details='%s' where organ_id='%s'"%(organ,detail,id)
		update(q)
		return redirect(url_for('admin.admin_manage_organ'))

	return render_template("admin_manage_organ.html",data=data)

@admin.route('/admin_view_organization')
def admin_view_organization():
	data={}
	q="select * from organization"
	res=select(q)
	data['org']=res

	return render_template("admin_view_organization.html",data=data)


@admin.route('/admin_view_donar')
def admin_view_donar():
	data={}
	q="select * from donar"
	res=select(q)
	data['donar']=res

	return render_template("admin_view_donar.html",data=data)



@admin.route('/admin_view_receiver')
def admin_view_receiver():
	data={}
	q="select * from receiver"
	res=select(q)
	data['receiver']=res

	return render_template("admin_view_receiver.html",data=data)


@admin.route('/admin_view_request')
def admin_view_request():
	data={}
	q="select * from blood_request"
	res=select(q)
	data['request']=res

	return render_template("admin_view_request.html",data=data)