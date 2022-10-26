from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from board_qna.models import Question
from board_qna.forms import QuestionForm


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
        return redirect('board_qna:detail', question_id=question.id)  # type: ignore
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
        return redirect('board_qna:detail', question_id=question.id)  # type: ignore
    question.delete()
    return redirect('board_qna:index')


@login_required()
def question_vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.user:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다')
    else:
        question.voter.add(request.user)
    return redirect('board_qna:detail', question_id=question.id)  # type: ignore