from django import forms
from .models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question  # model to use
        fields = ['subject', 'content']  # field for QuestionForm from Question model
        labels = {
            'subject': '제목',
            'content': '내용'
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변 내용',
        }