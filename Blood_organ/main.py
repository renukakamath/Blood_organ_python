from flask import Flask 
from public import public
from admin import admin
from organization import organization
from donar import donar
from receiver import receiver


app=Flask(__name__)
app.secret_key='hellooo'

app.register_blueprint(public)
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(organization,url_prefix='/organization')
app.register_blueprint(donar,url_prefix='/donar')
app.register_blueprint(receiver,url_prefix='/receiver')

app.run(debug=True,port=5001)