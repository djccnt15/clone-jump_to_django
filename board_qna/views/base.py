from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from board_qna.models import Question


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