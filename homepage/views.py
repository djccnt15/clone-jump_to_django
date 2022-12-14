from django.shortcuts import render
from config import urls

# Create your views here.


def index(request):
    """index view for main page"""

    context = {'url_list': urls.urlpatterns}  # get url list from config
    return render(request, 'homepage/index.html', context)