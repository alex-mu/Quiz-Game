from dataclasses import field
from email import message
from typing_extensions import Self
from flask_wtf import FlaskForm as Form
from wtforms import RadioField
from wtforms.validators import ValidationError
from random import randrange


class CorrectAnswer(object):
    def __init__(self, answer):
        self.answer = answer
def __call__(self, form, field):
        message = 'Incorrect answer.'
if field.data != Self.answer:
            raise ValidationError(message)
class PopQuiz(Form):
    class Meta:
        csrf = False
    q1 = RadioField(
        "The answer to question one is False.",
        choices=[('True', 'True'), ('False', 'False')],
        validators=[CorrectAnswer('False')]
        )