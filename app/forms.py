from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField, SelectField, FileField
from flask_wtf.file import FileAllowed, FileRequired, DataRequired

class ReviewForm(FlaskForm):
    name = StringField('Ваше имя', validators=[DataRequired(message="Поле не должно быть пустым")])
    text = TextAreaField('Текст отзыва', validators=[DataRequired(message="Поле не должно быть пустым")])
    score = SelectField('Оценка', choices=[(i, i) for i in range(1, 11)])
    submit = SubmitField('Добавить отзыв')


class MovieForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired(message="Поле не должно быть пустым")])
    description = TextAreaField('Описание', validators=[DataRequired(message="Поле не должно быть пустым")])
    image = FileField('Изображение',
                      validators=[FileRequired(message='Поле не должно быть пустым'),
                                  FileAllowed(['jpg', 'jpeg', 'png'], message='Неверный формат файла')])
    submit = SubmitField('Добавить фильм')