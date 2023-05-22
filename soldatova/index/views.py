from django.shortcuts import render
from django.views import generic
from .models import MainHeader, Reviews, Block2Content, Block3Content


# Create your views here.


class IndexView(generic.TemplateView):
    template_name = 'index/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Reviews.objects.order_by('-date_join').all()[:5]
        context['block2'] = Block2Content.objects.all()[:3]
        context['block3'] = Block3Content.objects.get(pk=1)
        return context
