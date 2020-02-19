from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import TextAreaField
from wtforms.validators import DataRequired
from wtforms.validators import Email


class ContactForm(FlaskForm):
    name = StringField('name',validators = [DataRequired()])
    email = StringField('email',validators = [DataRequired(),Email()])
    subject = StringField('subject',validators = [DataRequired()])
    message = TextAreaField('message',validators = [DataRequired()])
    