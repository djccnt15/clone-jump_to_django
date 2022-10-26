from django.urls import path

from .views import *

app_name = 'board_qna'

urlpatterns = [
    path('', base.index, name='index'),  # name parameter is to set name of url variable for template
    path('<int:question_id>/', base.detail, name='detail'),  # url for listing board_qna
    path('question/create/', question.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', question.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', question.question_delete, name='question_delete'),
    path('question/vote/<int:question_id>/', question.question_vote, name='question_vote'),
    path('answer/create/<int:question_id>/', answer.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/', answer.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', answer.answer_delete, name='answer_delete'),
    path('answer/vote/<int:answer_id>/', answer.answer_vote, name='answer_vote'),
]