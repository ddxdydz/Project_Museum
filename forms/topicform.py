from csv import reader

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, FileField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed


class TopicForm(FlaskForm):
    title = StringField('Название темы', validators=[DataRequired()])
    text = TextAreaField('Текст темы')
    img = FileField('Добавить фото', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Опубликовать тему')
