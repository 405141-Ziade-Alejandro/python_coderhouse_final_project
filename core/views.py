from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class AboutView(TemplateView):
    template_name = 'core/about.html'


def index(request):
    return render(request, 'core/index.html')
