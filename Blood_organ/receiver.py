from flask import *
from database import *

receiver=Blueprint('receiver',__name__)

@receiver.route('/receiverhome')
def receiverhome():
	return render_template("receiverhome.html")

@receiver.route('/receiver_request')
def receiver_request():
	data={}
	q="SELECT * FROM bloodgroup INNER JOIN blood_request USING(group_id)where receiver_id='%s'"%(session['receiver_id'])
	res=select(q)
	data['bld']=res
	return render_template("receiver_request.html",data=data)

@receiver.route('/receiver_organ_req')
def receiver_organ_req():
	data={}
	q="SELECT * FROM organ INNER JOIN organ_request USING(organ_id)where receiver_id='%s'"%(session['receiver_id'])
	res=select(q)
	data['bld']=res
	return render_template("receiver_organ_req.html",data=data)