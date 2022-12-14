from django import forms
from .models import Question, Answer


class QuestionForm(forms.ModelForm):
    """form for create question"""

    class Meta:
        """class for set metadata to question model"""

        model = Question  # model to use
        fields = ['subject', 'content']  # field for QuestionForm from Question model
        labels = {
            'subject': '제목',
            'content': '내용'
        }


class AnswerForm(forms.ModelForm):
    """form for create answer"""

    class Meta:
        """class for set metadata to answer model"""

        model = Answer
        fields = ['content']
        labels = {
            'content': '답변 내용',
        }