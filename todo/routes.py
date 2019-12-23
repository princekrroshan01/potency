from flask import render_template,flash,url_for,redirect,request
from todo import app,db
from todo.model import User
from todo.forms import RegistrationForm,LoginForm
from flask_login import login_user

todo={
	'title':'solve one question',
	'priority':'urgent'
}

@app.route('/')
def home():
	return render_template('home.html',todo=todo)



@app.route('/login',methods=['GET','POST'])
def login():
	form=LoginForm()
	if(request.method=='POST'):
		#print(request.form.get('username'))
		user=User.query.filter_by(email=request.form.get('username')).first()
		#print(user)
		if user:
			if user.password==request.form.get('password'):
				#login_user(user)
				return redirect(url_for('home'))
		else:
			print('ll')	
	return render_template('login.html',form=form)

@app.route('/register',methods=['GET','POST'])
def register():
	form=RegistrationForm()
	if(request.method=='POST'):
		username=request.form.get('username')
		email=request.form.get('email')
		password=request.form.get('password')
		confirm=request.form.get('confirm')
		user=User(username=username,email=email,password=password)
		db.session.add(user)
		db.session.commit()	
		print('account created')
		return redirect(url_for('home'))
	return render_template('register.html',form=form)
	
	
	
	
	
	
