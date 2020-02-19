from flask import Flask
from flask_mail import Mail


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_Key_1234567890'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = 'anonymousUser'
app.config['MAIL_PASSWORD'] = 'password123'

mail = Mail(app)
from app import views