__author__ = 'aamir'
from django.views.generic import TemplateView

from django.views.generic.base import View


class IndexView(TemplateView,View):
    template_name = 'base.html'

