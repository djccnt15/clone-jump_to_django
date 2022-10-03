from django.shortcuts import render
from config import urls

# Create your views here.


def index(request):
    context = {'url_list': urls.urlpatterns}
    return render(request, 'homepage/index.html', context)