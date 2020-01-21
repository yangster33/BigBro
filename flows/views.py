from django.shortcuts import render
from django.views.generic import ListView, TemplateView

# Create your views here.
from costs.middleware import ArchivesMixin
from costs.models import Costs
from .models import WeekendCostsFlows


class FlowsView(ArchivesMixin, ListView):
    template_name = 'index_flows.html'
    model = Costs
    paginate_by = 20

    def get_queryset(self):
        qs = Costs.objects.all()
        return qs.filter(account=self.request.user)


    def get_context_data(self, **kargs):

        context = super().get_context_data(**kargs)

        print(context['page_obj'].number)


        
        return context
