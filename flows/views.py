from django.shortcuts import render
from django.views.generic import ListView, TemplateView

# Create your views here.
from costs.middleware import ArchivesMixin
from costs.models import Costs
from .models import WeekendCostsFlows


class FlowsView(ArchivesMixin, TemplateView):
    template_name = 'index_flows.html'


    def get_context_data(self, **kargs):

        context = super().get_context_data(**kargs)

        
        return context
