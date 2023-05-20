from django.shortcuts import render
from django.views import generic
from .models import MainHeader, Reviews


# Create your views here.


class IndexView(generic.TemplateView):
    template_name = 'index/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Reviews.objects.order_by('-date_join').all()[:5]
        return context
