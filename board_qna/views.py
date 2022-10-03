from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponseNotAllowed
from .models import Question
from .forms import QuestionForm, AnswerForm

# Create your views here.


def index(request):  # index view for question_list
    question_list = Question.objects.order_by('-date_create')  # order by date_create desc
    context = {'question_list': question_list}
    return render(request, 'board_qna/question_list.html', context)


def detail(request, question_id):  # view for each question
    question = get_object_or_404(Question, pk=question_id)  # returns 404 instead of 500 when requested not existing question_id
    context = {'question': question}
    return render(request, 'board_qna/question_detail.html', context)


def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.date_create = timezone.now()
            answer.question = question
            answer.save()
            return redirect('board_qna:detail', question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question': question, 'form': form}
    return render(request, 'board_qna/question_detail.html', context)


def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)  # temporal saving with commit=False option
            question.user = request.user  # 'request.user' returns current login user
            question.date_create = timezone.now()  # add time data to form
            question.save()
            return redirect('board_qna:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'board_qna/question_form.html', context)