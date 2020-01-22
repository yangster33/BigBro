import datetime

from django.shortcuts import render
from django.views.generic import ListView, TemplateView

# Create your views here.
from costs.middleware import ArchivesMixin
from costs.models import Costs
from .models import WeekendCostsFlows
from costs.timetraveler import which_week


class FlowsView(ArchivesMixin, ListView):
    template_name = 'index_flows.html'
    model = Costs
    paginate_by = 20

    def get_queryset(self):
        qs = Costs.objects.all()
        return qs.filter(account=self.request.user)

    def get_context_data(self, **kargs):

        context = super().get_context_data(**kargs)

        myflows = WeekendCostsFlows.objects.filter(
            flow__contains=self.request.user._wrapped.username)
        flows_costs_list = [v.costs_set.all() for v in myflows]
        
        context.update({"myflows":myflows})
        context.update({"flows_costs_list":flows_costs_list})
        print(flows_costs_list)
        return context
