from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm

# Create your views here.


def index(request):
    """
    index view for question_list
    """

    page = request.GET.get(key='page', default='1')  # get value of 'page' from HTTP Request
    question_list = Question.objects.order_by('-id').exclude()  # order by id desc
    paginator = Paginator(object_list=question_list, per_page=10)  # number of object per page
    page_obj = paginator.get_page(number=page)  # page to return
    total_pages = paginator.num_pages  # get number of total pages
    context = {'question_list': page_obj, 'total_pages': total_pages}  # total_page is for template filter
    return render(request=request, template_name='board_qna/question_list.html', context=context)


def detail(request, question_id):
    """
    view for details of each question
    """

    question = get_object_or_404(Question, pk=question_id)  # returns 404 instead of 500 when requested not existing question_id
    context = {'question': question}
    return render(request, 'board_qna/question_detail.html', context)


@login_required()
def answer_create(request, question_id):
    """
    view for create answer
    """

    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)  # temporal saving with commit=False option
            answer.user = request.user  # 'request.user' returns current login user
            answer.date_create = timezone.now()  # add time data to form
            answer.question = question
            answer.save()
            return redirect('board_qna:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'board_qna/question_detail.html', context)


@login_required()
def question_create(request):
    """
    view for create question
    """

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


@login_required()
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.user:  # blocking invalid approach
        messages.error(request, '수정 권한이 없습니다')
        return redirect('board_qna:detail', question_id=question.id)
    if request.method == "POST":
        form = QuestionForm(data=request.POST, instance=question)  # override instance with requested POST
        if form.is_valid():
            question = form.save(commit=False)
            question.date_modify = timezone.now()  # add current time to form
            question.save()
            return redirect('board_qna:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)  # fill form with current context
    context = {'form': form}
    return render(request, 'board_qna/question_form.html', context)


@login_required()
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.user:
        messages.error(request, '삭제 권한이 없습니다')
        return redirect('board_qna:detail', question_id=question.id)
    question.delete()
    return redirect('board_qna:index')


@login_required()
def answer_modify(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.user:
        messages.error(request, '수정 권한이 없습니다')
        return redirect('board_qna:detail', question_id=answer.question.id)
    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.date_modify = timezone.now()
            answer.save()
            return redirect('board_qna:detail', question_id=answer.question.id)
    else:
        form = AnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'board_qna/answer_form.html', context)


@login_required()
def answer_delete(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.user:
        messages.error(request, '삭제 권한이 없습니다')
    else:
        answer.delete()
    return redirect('board_qna:detail', question_id=answer.question.id)