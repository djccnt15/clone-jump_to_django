from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from board_qna.models import Question, Answer
from board_qna.forms import AnswerForm


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
            return redirect('board_qna:detail', question_id=question.id)  # type: ignore
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'board_qna/question_detail.html', context)


@login_required()
def answer_modify(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.user:
        messages.error(request, '수정 권한이 없습니다')
        return redirect('board_qna:detail', question_id=answer.question.id)  # type: ignore
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
    return redirect('board_qna:detail', question_id=answer.question.id)  # type: ignore


@login_required()
def answer_vote(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user == answer.user:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다')
    else:
        answer.voter.add(request.user)
    return redirect('board_qna:detail', question_id=answer.question.id)  # type: ignore